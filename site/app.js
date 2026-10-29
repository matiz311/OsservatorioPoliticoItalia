(() => {
"use strict";
const $ = id => document.getElementById(id);
const esc = s => String(s ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const label = {measure:"Misura",act:"Atto",government:"Governo",context:"Contesto"};
let records = [], selected = null;
const sourceLink = id => {
 const entry = (window.catalogSources || []).find(s => s.id === id);
 if (!entry || !/^https:\/\//.test(entry.url || "")) return esc(id);
 return '<a href="'+esc(entry.url)+'" target="_blank" rel="noopener noreferrer">'+esc(entry.name || id)+' ↗</a>';
};
const li = values => values && values.length ? "<ul>"+values.map(v=>"<li>"+v+"</li>").join("")+"</ul>" : "<p>Non documentato.</p>";
const display = val => val == null || val === "" ? "Non disponibile" : esc(val);
function detail(item) {
 if(!item) { $("detail").innerHTML="<h3>Seleziona un elemento</h3><p>Apri una scheda per esaminare fonti, rapporti costituzionali e continuità legislativa.</p>"; return; }
 const d=item.data, c=d.constitutional_comparison, parts=[];
 parts.push('<span class="tag">'+esc(label[item.type]||item.type)+'</span><h3>'+esc(d.title||d.name||d.id)+'</h3>');
 parts.push('<dl><dt>ID</dt><dd>'+esc(d.id)+'</dd><dt>Stato</dt><dd>'+display(d.status)+'</dd><dt>Governo</dt><dd>'+display(d.government_id||d.proposed_under_government_id||d.name)+'</dd></dl>');
 if(c){parts.push('<h4>Confronto costituzionale</h4><dl><dt>Esame</dt><dd>'+display(c.review_status)+'</dd><dt>Testo originario</dt><dd>'+display(c.original_constitution_date)+'</dd><dt>Versione applicabile</dt><dd>'+display(c.applicable_version_date)+'</dd></dl>');parts.push('<h4>Articoli interessati</h4>'+li((c.articles||[]).map(a=>esc(a.article)+(a.comparison_notes?' — '+esc(a.comparison_notes):''))));parts.push('<h4>Pronunce della Corte</h4>'+li((c.court_decisions||[]).map(x=>/^https:\/\//.test(x.source_url||"")?'<a href="'+esc(x.source_url)+'" target="_blank" rel="noopener">'+esc(x.reference)+'</a>':esc(x.reference))));}
 if(d.prior_norm_relations)parts.push('<h4>Eredità delle norme precedenti</h4>'+li(d.prior_norm_relations.map(r=>esc(r.relation)+' → '+esc(r.target_id))));
 if(d.government_phases)parts.push('<h4>Fasi tra governi</h4>'+li(d.government_phases.map(g=>esc(g.government_id)+' — '+esc(g.phase))));
 if(d.outcomes)parts.push('<h4>Risultati osservati</h4>'+li(d.outcomes.map(o=>esc(o.indicator)+' — '+esc(o.evaluation_design))));
 if(d.sources)parts.push('<h4>Fonti</h4>'+li(d.sources.map(sourceLink)));
 if(d.start)parts.push('<h4>Periodo</h4><p>'+esc(d.start)+' — '+esc(d.end||"in corso / da confermare")+'</p>');
 if(d.status==="needs_source_enrichment") parts.push('<p><strong>Record incompleto:</strong> fonti e cronologia da verificare.</p>');
 $("detail").innerHTML=parts.join("");
}
function render() {
 const query=$("search").value.trim().toLocaleLowerCase("it");
 const type=$("type").value, status=$("status").value;
 const items=records.filter(x => (type==="all"||type===x.type)&&(status==="all"||status===String(x.data.status||""))&&(!query||JSON.stringify(x.data).toLocaleLowerCase("it").includes(query)));
 $("resultsMeta").textContent=items.length+" record trovati";
 if(!items.length){$("results").innerHTML='<div class="empty">Nessun record corrisponde ai filtri. Il catalogo è ancora in costruzione e non include i dati di esempio.</div>';detail(null);return;}
 $("results").innerHTML=items.map(x=>'<button type="button" class="item'+(x.key===selected?' active':'')+'" data-key="'+esc(x.key)+'"><span class="tag">'+esc(label[x.type]||x.type)+'</span><h3>'+esc(x.data.title||x.data.name||x.data.id)+'</h3><p>'+esc(x.data.status||"Dati in raccolta")+'</p></button>').join("");
 const current=items.find(x=>x.key===selected)||items[0];selected=current.key;detail(current);
 $("results").querySelectorAll("button").forEach(b=>b.addEventListener("click",()=>{selected=b.dataset.key;render();}));
}
async function init(){
 try {
 const res=await fetch("data/catalog.json",{cache:"no-store"});
 if(!res.ok)throw Error("HTTP "+res.status);
 const raw=await res.json();
 window.catalogSources=raw.sources||[];
 records=[...((raw.measures||[]).map(d=>({type:"measure",data:d}))),...((raw.acts||[]).map(d=>({type:"act",data:d}))),...((raw.governments||[]).map(d=>({type:"government",data:d}))),...((raw.contexts||[]).map(d=>({type:"context",data:d})))].map(x=>({...x,key:x.type+":"+x.data.id}));
 for(const [id,category] of [["nMeasures","measure"],["nActs","act"],["nGovernments","government"],["nContexts","context"]]) $(id).textContent=records.filter(x=>x.type===category).length.toLocaleString("it");
 const states=[...new Set(records.map(x=>x.data.status).filter(Boolean))].sort();
 $("status").innerHTML='<option value="all">Tutti gli stati</option>'+states.map(s=>'<option value="'+esc(s)+'">'+esc(s)+'</option>').join("");
 $("dataStatus").textContent="Catalogo disponibile";
 render();
 } catch(e) {$("dataStatus").textContent="Dati non disponibili";$("results").innerHTML='<div class="empty">Il catalogo non è stato caricato. Verifica la pubblicazione GitHub Pages e il workflow di generazione dei dati.</div>';console.error(e);}
}
["search","type","status"].forEach(id=>$(id).addEventListener(id==="search"?"input":"change",render));
init();
})();