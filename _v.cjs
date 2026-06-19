const fs = require('fs');
const g = fs.readFileSync('D:/portfolio/src/collections/gallery.json', 'utf8');
const m = g.match(/\/images\/\d{4}\.webp/g);
console.log('Numeric webp refs:', m ? m.length : 0);
const old = g.match(/\/images\/(posters|live-stream|detail-pages|material-design|brand-design|douyin)/g);
console.log('Old subdir refs:', old ? old.length : 0);
const imgSample = g.match(/"image":\s*"[^"]+"/);
console.log('Sample:', imgSample ? imgSample[0] : 'NONE');
// Check site.js
const siteJS = fs.readFileSync('D:/portfolio/src/config/site.js', 'utf8');
const resume = siteJS.match(/resume:\s*"([^"]+)"/);
console.log('Resume URL:', resume ? resume[1] : 'NONE');
