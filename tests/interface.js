/* DOM-free integration checks. They do not claim visual browser rendering. */
const vm=require('node:vm'),fs=require('node:fs'),path=require('node:path'),assert=require('node:assert/strict');
const root=path.join(__dirname,'..');let html='',dynamic=new Map(),lists={},scrolled='',focused='';
function el(attrs={},id=''){return {dataset:attrs,style:{setProperty(){}},classList:{toggle(){}},setAttribute(){},scrollIntoView(){scrolled=id;},focus(){focused=id;},value:'',textContent:'',onclick:null};}
const staticNodes=new Map(['main','nav','theme','toast','storage-note'].map(k=>[k,el({},k)]));
Object.defineProperty(staticNodes.get('main'),'innerHTML',{get:()=>html,set:v=>{html=v;dynamic=new Map();lists={};}});
const attrs=s=>{const d={};for(const m of s.matchAll(/data-([a-z-]+)="([^"]*)"/g))d[m[1].replace(/-([a-z])/g,(_,c)=>c.toUpperCase())]=m[2];return d;};
function allMarkup(){return html+'\n'+[...dynamic.values()].map(x=>x.innerHTML||'').join('\n');}
const doc={body:el(),querySelector(s){if(s[0]!=='#')return null;const id=s.slice(1);if(staticNodes.has(id))return staticNodes.get(id);if(dynamic.has(id))return dynamic.get(id);const match=allMarkup().match(new RegExp('<[^>]+id="'+id+'"[^>]*>'));if(!match)return null;const node=el({},id);node.value=match[0].match(/value="([^"]*)"/)?.[1]||'';dynamic.set(id,node);return node;},querySelectorAll(s){if(lists[s])return lists[s];const name=s.match(/^\[data-([^\]]+)\]$/)?.[1];if(!name)return [];return [...allMarkup().matchAll(/<[^>]+>/g)].filter(m=>m[0].includes('data-'+name+'=')).map(m=>el(attrs(m[0])));}};
const storage=new Map(),ctx={document:doc,window:{addEventListener(){},scrollTo(){}},location:{hash:'#home'},localStorage:{getItem:k=>storage.get(k)||null,setItem:(k,v)=>storage.set(k,v)},matchMedia:()=>({matches:false}),setTimeout:()=>1,clearTimeout(){},confirm:()=>true,console,Blob,URL};vm.createContext(ctx);for(const file of ['data.js','engine.js','essays.js','visuals.js','app.js'])vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'),ctx,{filename:file});
const go=hash=>{ctx.location.hash=hash;ctx.navigate();};
const click=(action,extras={})=>ctx.practiceClick({target:{closest:()=>({dataset:{action,...extras},disabled:false})}});
const saved=()=>JSON.parse(storage.get('speech-language-exam-v1'));
assert(html.includes('Choose a lecture'));go('#study/1');assert(html.includes('easy to challenging'));assert.equal((html.match(/class="question practice-question/g)||[]).length,20);assert(html.includes('Page 1 of 5'));
const q=ctx.window.COURSE.questions.find(x=>x.lecture===1),wrong=(q.answer+1)%4;
const order=vm.runInContext(`JSON.stringify(session['${q.id}'].order)`,ctx);
click('answer',{qid:q.id,option:String(wrong)});assert(saved().answers[q.id].needsReview);assert.equal(saved().answers[q.id].attempts,1);assert(doc.querySelector('#slot-'+q.id).innerHTML.includes('Revisit this concept'));assert.equal(focused,'feedback-'+q.id);assert.equal(vm.runInContext(`JSON.stringify(session['${q.id}'].order)`,ctx),order);
// Duplicate clicks or a click on the reveal action after scoring cannot add attempts.
click('answer',{qid:q.id,option:String(q.answer)});click('reveal',{qid:q.id});assert.equal(saved().answers[q.id].attempts,1);
// Next stays on the current page until the boundary, then opens its following page.
click('next',{index:'0'});assert.equal(scrolled,'question-'+ctx.window.COURSE.questions.filter(x=>x.lecture===1)[1].id);click('next',{index:'19'});assert(html.includes('Page 2 of 5'));assert.equal(saved().resume.id,ctx.window.COURSE.questions.filter(x=>x.lecture===1)[20].id);
click('page',{page:'4'});assert(html.includes('Questions 81–100'));assert.equal((html.match(/class="question practice-question/g)||[]).length,20);
go('#wrong');assert(html.includes('Revise wrong answers'));assert(html.includes('remaining questions'));assert(!html.includes('Revisit this concept'));click('answer',{qid:q.id,option:String(q.answer)});assert(saved().answers[q.id].correct);assert(!saved().answers[q.id].needsReview);assert.equal(saved().answers[q.id].attempts,2);go('#wrong');assert(html.includes('You are up to date'));
go('#study/2');const q2=ctx.window.COURSE.questions.find(x=>x.lecture===2);click('reveal',{qid:q2.id});assert.equal(Object.keys(saved().answers).length,1);assert(saved().seen.includes(q2.id));click('bookmark',{qid:q2.id});assert(saved().bookmarks.includes(q2.id));go('#bookmarks');assert(html.includes('Your bookmarks'));
// The final page shows the remainder without repeating questions.
go('#study/2');click('page',{page:'4'});assert(html.includes('Questions 81–94'));assert.equal((html.match(/class="question practice-question/g)||[]).length,14);
// All requested sizes render the selected count, preserve the active question and persist.
for(const n of [10,20,50,100]){go('#study/6');doc.querySelector('#practice-page-size').onchange({target:{value:String(n)}});assert.equal((html.match(/class="question practice-question/g)||[]).length,n);assert.equal(storage.get('speech-language-pagesize-v1'),String(n));}
go('#study/6');click('jump',{index:'75'});const beforeSize=saved().resume.id;doc.querySelector('#practice-page-size').onchange({target:{value:'50'}});assert.equal(saved().resume.id,beforeSize);assert.equal(scrolled,'question-'+beforeSize);assert(html.includes('Questions 51–100'));doc.querySelector('#practice-page-size').onchange({target:{value:'20'}});
// Deep links open the correct containing page and focus their target.
const deep=ctx.window.COURSE.questions.filter(x=>x.lecture===3)[45];go('#study/3/'+deep.id);assert(html.includes('Page 3'));assert.equal(scrolled,'question-'+deep.id);
go('#glossary/3');assert(html.includes('Key concepts'));assert(doc.querySelector('#concept-list').innerHTML.includes('phonetics'));go('#sources');assert(html.includes('Important corrections'));go('#progress');assert(html.includes('Keep your work'));doc.querySelector('#theme').onclick();assert.equal(storage.get('speech-language-theme'),'true');
go('#essays');assert(html.includes('Lecture essays'));go('#essays/4');assert(html.includes('Morphology and the organization'));assert(html.includes('essay-section-7'));doc.querySelector('#reader-larger').onclick();assert(JSON.parse(storage.get('speech-language-reader-v1')).size===19);doc.querySelector('#mark-read').onclick();assert(JSON.parse(storage.get('speech-language-reader-v1')).completed.includes(4));go('#glossary/4');assert(doc.querySelector('#concept-list').innerHTML.includes('<svg'));
console.log('PASS: Show 10/20/50/100, saved page size, active-question preservation, instant feedback, duplicate-click guard, stable option order, next-question/page boundaries, final remainder, deep links, revision, bookmarks, essays and glossary.');
