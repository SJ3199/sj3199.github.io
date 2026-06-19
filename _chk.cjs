const g=require('fs').readFileSync('D:/portfolio/src/collections/gallery.json','utf8');
const n=g.match(/\/images\/\d{4}\.webp/g);
const o=g.match(/\/images\/(posters|live-stream|detail-pages|brand-design|material-design|douyin)/g);
console.log('New numeric webp: '+(n?n.length:0));
console.log('Old subdir refs: '+(o?o.length:0));
const m=g.match(/"image"\s*:\s*"[^"]+"/);
if(m) console.log('Sample:', m[0]);
