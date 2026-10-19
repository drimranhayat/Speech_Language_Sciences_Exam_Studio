/* Shared study logic. Answers are stored by canonical option index, never display letter. */
(function(root){
 const shuffle=(items,random=Math.random)=>{const a=[...items];for(let i=a.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[a[i],a[j]]=[a[j],a[i]];}return a;};
 function record(previous,question,selected){if(!Number.isInteger(selected)||selected<0||selected>=question.options.length)throw Error('Invalid answer');const correct=selected===question.answer;return {selected,correct,attempts:(previous?.attempts||0)+1,everWrong:!!previous?.everWrong||!correct,needsReview:!correct,last:Date.now()};}
 function validateBackup(input,questions){if(input.version!==1||!input.answers||typeof input.answers!=='object'||Array.isArray(input.answers))throw Error('This is not a valid Exam Studio backup.');const known=new Map(questions.map(q=>[q.id,q]));const answers={};for(const [id,r] of Object.entries(input.answers)){const q=known.get(id);if(!q)continue;if(!r||!Number.isInteger(r.selected)||r.selected<0||r.selected>3||!Number.isInteger(r.attempts)||r.attempts<1)throw Error('The backup contains an invalid answer.');const correct=r.selected===q.answer;answers[id]={selected:r.selected,correct,attempts:r.attempts,everWrong:!!r.everWrong||!correct,needsReview:!correct,last:Number(r.last)||0};}return {version:1,answers,seen:(Array.isArray(input.seen)?input.seen:[]).filter(id=>known.has(id)),bookmarks:(Array.isArray(input.bookmarks)?input.bookmarks:[]).filter(id=>known.has(id)),resume:input.resume&&known.has(input.resume.id)?{id:input.resume.id,lecture:known.get(input.resume.id).lecture}:null};}
 function pages(length,size=20){
  if(!Number.isInteger(length)||length<0||!Number.isInteger(size)||size<1)throw Error('Invalid page size');
  const result=[];for(let start=0;start<length;start+=size)result.push({start,end:Math.min(length,start+size)});return result;
 }
 const engine={shuffle,record,validateBackup,pages};if(typeof module!=='undefined')module.exports=engine;else root.ExamEngine=engine;
})(typeof window==='undefined'?globalThis:window);
