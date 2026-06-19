/**
 * R2 Image Migration: 167 images → flat numeric webp CDN
 * Phase 1: Convert ALL to webp, upload as images/0001.webp..0167.webp
 *           Delete ALL old R2 objects
 * Output:  _cdn_rename_map.json (oldPath → newCDN)
 */
process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const sharp = require('sharp');

const BASE_DIR = 'D:/portfolio/public/images';
const CDN_BASE = 'https://pub-ea6cf7d0fc18449aa9cce3aee87abf18.r2.dev';
const ACCOUNT_ID = '93eb059c98d30a883375cfaf04bc20e6';
const BUCKET = 'portfolio-images';
const ACCESS_KEY = '6815ea0d79f1f1ef1525a54dc3ad83f6';
const SECRET_KEY = 'ff83432e13e85da51f1b832962d8acafd6026b61db2b2ecd27bb27b874e36b23';
const REGION = 'auto', SERVICE = 's3';
const OLD_KEYS_FILE = 'D:/portfolio/_old_r2_keys.txt';

// SigV4
function sha256(d) { return crypto.createHash('sha256').update(d).digest('hex'); }
function hmac(k, m) { return crypto.createHmac('sha256', k).update(m).digest(); }
function signingKey(ds) {
  return hmac(hmac(hmac(hmac(Buffer.from('AWS4'+SECRET_KEY), ds), REGION), SERVICE), 'aws4_request');
}
function signedReq(method, key, body, ct) {
  const ph = sha256(body);
  const d = new Date();
  const ad = d.toISOString().replace(/[:\-]|\.\d{3}/g,'');
  const ds = ad.substring(0,8);
  const host = `${BUCKET}.${ACCOUNT_ID}.r2.cloudflarestorage.com`;
  const h = { 'Host':host, 'x-amz-content-sha256':ph, 'x-amz-date':ad, 'Content-Type':ct, 'Content-Length':String(body.length) };
  const n = 'content-length;content-type;host;x-amz-content-sha256;x-amz-date';
  const cn = `content-length:${body.length}\ncontent-type:${ct}\nhost:${host}\nx-amz-content-sha256:${ph}\nx-amz-date:${ad}\n`;
  const cr = [method, '/'+key, '', cn, n, ph].join('\n');
  const cs = `${ds}/${REGION}/${SERVICE}/aws4_request`;
  const sts = ['AWS4-HMAC-SHA256', ad, cs, sha256(cr)].join('\n');
  h['Authorization'] = `AWS4-HMAC-SHA256 Credential=${ACCESS_KEY}/${cs}, SignedHeaders=${n}, Signature=${hmac(signingKey(ds), sts).toString('hex')}`;
  return { url: `https://${host}/${key}`, headers: h };
}

// Collect
function* walk(dir, pre='images/') {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory()) yield* walk(path.join(dir, e.name), pre+e.name+'/');
    else yield { oldKey: pre+e.name, localPath: path.join(dir, e.name) };
  }
}

async function run() {
  const files = [...walk(BASE_DIR)].sort((a,b) => a.oldKey.localeCompare(b.oldKey));
  console.log(`Found ${files.length} files\n`);

  const renameMap = {};
  let ok = 0, fail = 0;
  const oldKeysToDelete = [];

  for (let i = 0; i < files.length; i++) {
    const f = files[i];
    const num = String(i+1).padStart(4,'0');
    const newKey = `images/${num}.webp`;
    const newCDN = `${CDN_BASE}/${newKey}`;
    try {
      // Convert to webp @85% quality
      const ext = path.extname(f.localPath).toLowerCase();
      let pipe = sharp(f.localPath);
      const webpBuf = await pipe.webp({ quality: 85 }).toBuffer();

      // Upload
      const { url, headers } = signedReq('PUT', newKey, webpBuf, 'image/webp');
      const resp = await fetch(url, { method: 'PUT', headers, body: webpBuf });
      if (!resp.ok) throw new Error(`HTTP ${resp.status}: ${(await resp.text()).substring(0,100)}`);

      renameMap['/'+f.oldKey] = newCDN;
      oldKeysToDelete.push(f.oldKey);
      ok++;
      process.stdout.write(`\r[${i+1}/${files.length}] OK  ${f.oldKey}  →  ${num}.webp (${webpBuf.length}B)`);
    } catch(e) {
      fail++;
      process.stdout.write(`\r[${i+1}/${files.length}] FAIL ${f.oldKey}: ${e.message}\n`);
    }
  }

  console.log(`\n\n=== Upload: ${ok} OK, ${fail} FAIL ===`);

  // Save rename map
  fs.writeFileSync('D:/portfolio/_cdn_rename_map.json', JSON.stringify(renameMap, null, 2), 'utf8');
  fs.writeFileSync(OLD_KEYS_FILE, oldKeysToDelete.join('\n'), 'utf8');
  console.log(`\nMap: ${Object.keys(renameMap).length} entries → _cdn_rename_map.json`);
  console.log(`Old keys: ${oldKeysToDelete.length} → _old_r2_keys.txt`);

  // Delete old objects
  console.log('\n=== Deleting old R2 objects ===');
  let delOk = 0, delFail = 0;
  for (const oldKey of oldKeysToDelete) {
    try {
      const body = Buffer.alloc(0);
      const { url, headers } = signedReq('DELETE', oldKey, body, 'application/octet-stream');
      const resp = await fetch(url, { method: 'DELETE', headers });
      if (resp.ok || resp.status === 204) { delOk++; }
      else { delFail++; console.log(`DEL FAIL ${oldKey}: ${resp.status}`); }
    } catch(e) { delFail++; console.log(`DEL ERR ${oldKey}: ${e.message}`); }
  }
  console.log(`Delete: ${delOk} OK, ${delFail} FAIL`);

  console.log(`\n✅ Phase 1 complete. CDN: ${CDN_BASE}/images/0001.webp..${String(files.length).padStart(4,'0')}.webp`);
}

run().catch(e => { console.error(e); process.exit(1); });
