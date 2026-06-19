const fs = require('fs');
const path = require('path');

function walk(dir) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (!entry.name.startsWith('.') && entry.name !== 'node_modules' && entry.name !== 'dist' && entry.name !== '.git') {
        results.push(...walk(p));
      }
    } else {
      results.push(p);
    }
  }
  return results;
}

const dirs = ['D:/portfolio/src', 'D:/portfolio/public'];
const extRe = /\.(astro|js|ts|json|css|md|html)$/;
let found = [];

for (const dir of dirs) {
  for (const f of walk(dir)) {
    if (!extRe.test(f)) continue;
    try {
      const content = fs.readFileSync(f, 'utf8');
      const lines = content.split('\n');
      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        if (line.includes('/images/') &&
            !line.includes('pub-ea6cf7d0fc') &&
            !line.includes('astro.build') &&
            !line.includes('authorizing-remote')) {
          const shortPath = f.replace('D:/portfolio/', '');
          found.push(`${shortPath}:${i + 1}: ${line.trim().substring(0, 120)}`);
        }
      }
    } catch (e) {}
  }
}

if (found.length) {
  console.log('===== REMAINING /images/ REFERENCES TO FIX =====\n');
  console.log(found.join('\n'));
  console.log(`\nTotal: ${found.length} references`);
} else {
  console.log('All /images/ references already updated to CDN URLs!');
}
