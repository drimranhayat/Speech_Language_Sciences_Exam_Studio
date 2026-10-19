const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),E=require('../engine.js');
const D=JSON.parse(fs.readFileSync(path.join(__dirname,'../data.json'),'utf8'));
// Every question appears exactly once; page size never exceeds the requested count.
for(const size of [10,20,50,100])for(let n=0;n<=1200;n++){const pages=E.pages(n,size);assert.equal(pages.reduce((s,p)=>s+p.end-p.start,0),n);for(let i=0;i<pages.length;i++){const p=pages[i];assert.equal(p.start,i?pages[i-1].end:0);assert(p.end>p.start&&p.end<=n);assert(p.end-p.start<=size);if(i<pages.length-1)assert.equal(p.end-p.start,size);}}
for(const l of D.lectures){const n=D.questions.filter(q=>q.lecture===l.id).length;for(const size of [10,20,50,100])assert(E.pages(n,size).every(p=>p.end-p.start<=size));}
assert.deepEqual(E.pages(94),[{start:0,end:20},{start:20,end:40},{start:40,end:60},{start:60,end:80},{start:80,end:94}]);assert.deepEqual(E.pages(1),[{start:0,end:1}]);assert.deepEqual(E.pages(0),[]);assert.throws(()=>E.pages(-1));
const q=D.questions[0],record={selected:q.answer,correct:true,attempts:7,everWrong:true,needsReview:false,last:123};const oldBackup={version:1,answers:{[q.id]:record},seen:[q.id],bookmarks:[q.id],resume:{id:q.id,lecture:q.lecture}};assert.deepEqual(E.validateBackup(oldBackup,D.questions),oldBackup);
console.log('PASS: Pagination coverage for all four sizes and all lengths 0–1200, final remainders, small review sets and existing progress-backup compatibility.');
