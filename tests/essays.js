const assert=require('node:assert/strict'),fs=require('node:fs'),path=require('node:path'),vm=require('node:vm');
const root=path.join(__dirname,'..'),essays=JSON.parse(fs.readFileSync(path.join(root,'essays.json'),'utf8')),course=JSON.parse(fs.readFileSync(path.join(root,'data.json'),'utf8'));
assert.equal(essays.length,8);assert.equal(new Set(essays.map(e=>e.lecture)).size,8);
const sources=new Set(course.sources.map(s=>s.id));
for(const e of essays){assert(e.lecture>=1&&e.lecture<=8);assert(e.sections.length>=6);assert(e.sourceIds.every(id=>sources.has(id)));const text=e.sections.flatMap(s=>s.paragraphs).join(' ');assert.equal(text.split(/\s+/).length,e.wordCount);assert(e.wordCount>=850);assert(e.sections.every(s=>s.heading&&s.paragraphs.length>=1));assert(!/TODO|placeholder|citation needed/i.test(text));}
const ctx={window:{}};vm.createContext(ctx);for(const file of ['essays.js','visuals.js'])vm.runInContext(fs.readFileSync(path.join(root,file),'utf8'),ctx);assert.equal(JSON.stringify(ctx.window.LECTURE_ESSAYS),JSON.stringify(essays));
const icons=new Set();for(const c of course.concepts){const markup=ctx.window.StudyVisuals.icon(c.term,c.lecture);assert(markup.includes('<svg'));assert(markup.includes('aria-hidden="true"'));assert(!markup.includes('undefined'));icons.add(markup.match(/<svg.*<\/svg>/)[0]);}assert(icons.size>=15);
const html=fs.readFileSync(path.join(root,'index.html'),'utf8');for(const file of ['data.js','engine.js','essays.js','visuals.js','app.js','styles.css'])assert(html.includes(`"${file}"`));
console.log(`PASS: Eight essays, ${essays.reduce((n,e)=>n+e.wordCount,0).toLocaleString()} words, section/source integrity, JSON parity, all ${course.concepts.length} concept icons, ${icons.size} distinct SVG designs and script references.`);
