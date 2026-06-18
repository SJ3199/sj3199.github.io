const https = require('https');

function checkUrl(url, label) {
  return new Promise((resolve) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => resolve({ label, data }));
    }).on('error', () => resolve({ label, data: '' }));
  });
}

async function main() {
  const r1 = await checkUrl('https://sj3199.github.io/', '首页');
  const r2 = await checkUrl('https://sj3199.github.io/intro/', '个人介绍');
  const r3 = await checkUrl('https://sj3199.github.io/about/', 'AI项目');
  
  [r1, r2, r3].forEach(r => {
    console.log('=== ' + r.label + ' ===');
    const d = r.data;
    // Check active class in nav
    const re = /href="([^"]+)"[^>]*data-i18n-zh="([^"]*)"[^>]*class="([^"]*)"/g;
    let m;
    while ((m = re.exec(d)) !== null) {
      const active = m[3].includes(' active ') || m[3].endsWith(' active');
      console.log('  ' + m[2] + ': ' + (active ? 'ACTIVE ✓' : '-'));
    }
    // Check copyright
    const copyOk = d.includes('© 2026') || d.includes('&copy; 2026');
    console.log('  copyright: ' + (copyOk ? '© OK' : '? BROKEN'));
    // Check about i18n
    if (r.label === 'AI项目') {
      const hasI18n = d.includes('data-i18n="about-title"') && d.includes('data-i18n="about-desc"');
      console.log('  i18n attrs: ' + (hasI18n ? 'OK' : 'MISSING'));
    }
    // Check deploy version
    const buildVer = d.match(/BUILD:\s*([^<]+)/);
    console.log('  build: ' + (buildVer ? buildVer[1] : 'N/A'));
  });
}

main().catch(console.error);
