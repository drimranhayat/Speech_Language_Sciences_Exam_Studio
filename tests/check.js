'use strict';
const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.join(__dirname,'..'),D=JSON.parse(fs.readFileSync(path.join(root,'data.json'),'utf8')),E=require('../engine.js');
assert(D.questions.length>=800);assert.equal(D.lectures.length,8);assert.equal(new Set(D.questions.map(q=>q.id)).size,D.questions.length);
const sourceIds=new Set(D.sources.map(s=>s.id)),cs=new Set(D.concepts.map(c=>c.id));const ranks={Easy:0,Moderate:1,Challenging:2};
for(const l of D.lectures){const qs=D.questions.filter(q=>q.lecture===l.id);assert.equal(qs.length,l.count);assert.equal(D.concepts.filter(c=>c.lecture===l.id).length,l.concepts);assert.deepEqual([...new Set(qs.map(q=>q.difficulty))],['Easy','Moderate','Challenging']);for(let i=1;i<qs.length;i++)assert(ranks[qs[i-1].difficulty]<=ranks[qs[i].difficulty]);assert.equal(new Set(qs.map(q=>q.question)).size,qs.length);}
for(const q of D.questions){assert(q.question.length>20);assert.equal(q.options.length,4);assert.equal(new Set(q.options).size,4);assert(Number.isInteger(q.answer)&&q.answer>=0&&q.answer<4);assert(q.explanation.length>100);assert(q.sourceIds.every(s=>sourceIds.has(s)));assert(!q.conceptId||cs.has(q.conceptId));}
// A wrong answer must remain in revision until a later correct attempt.
const q=D.questions[0],wrong=(q.answer+1)%4;let r=E.record(null,q,wrong);assert(r.needsReview&&r.everWrong);r=E.record(r,q,q.answer);assert(!r.needsReview&&r.everWrong&&r.correct);assert.equal(r.attempts,2);
// All display permutations must preserve the canonical key and saved selection.
function permutations(a){if(!a.length)return [[]];return a.flatMap((v,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[v,...p]));}
for(const order of permutations([0,1,2,3])){const shown=order.map(i=>q.options[i]);const letter=order.indexOf(q.answer);assert.equal(shown[letter],q.options[q.answer]);assert.equal(order[letter],q.answer);}
const backup={version:1,answers:{[q.id]:r,UNKNOWN:r},seen:[q.id,'UNKNOWN'],bookmarks:[q.id],resume:{id:q.id,lecture:99}};const clean=E.validateBackup(backup,D.questions);assert.equal(clean.resume.lecture,q.lecture);assert.equal(Object.keys(clean.answers).length,1);assert.deepEqual(clean.seen,[q.id]);assert.deepEqual(clean.bookmarks,[q.id]);assert.throws(()=>E.validateBackup({version:1,answers:{[q.id]:{selected:5,attempts:1}}},D.questions));
const sandbox={window:{}};vm.runInNewContext(fs.readFileSync(path.join(root,'data.js'),'utf8'),sandbox);assert.equal(sandbox.window.COURSE.questions.length,D.questions.length);assert.equal(JSON.stringify(sandbox.window.COURSE),JSON.stringify(D));
// WCAG normal-text contrast for every coloured lecture tab's white label.
const colors=['#185a91','#6651a5','#006d70','#9b4918','#9a3865','#365f2b','#914620','#4a53a6'];const luminance=hex=>{const a=hex.match(/[0-9a-f]{2}/gi).map(x=>parseInt(x,16)/255).map(v=>v<=.04045?v/12.92:((v+.055)/1.055)**2.4);return .2126*a[0]+.7152*a[1]+.0722*a[2];};for(const c of colors)assert(1.05/(luminance(c)+.05)>=4.5,c);
console.log(`PASS: ${D.questions.length} MCQs, ${D.concepts.length} concepts, all 8 lecture counts, gradual levels, option integrity, all 24 display permutations, wrong-answer correction, backup validation, data parity and tab contrast.`);
