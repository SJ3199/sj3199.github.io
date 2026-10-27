type Original = {url:string;filename:string;width:number;height:number;bytes:number;mime:string};
type View = {image:string;thumbnail?:string};
type Item = {image:string;title:string;description?:string;details?:string;category:string;downloadEnabled?:boolean;original?:Original;wallpaper?:{lock?:View;passcode?:View;width?:number;height?:number}};
const items:Item[]=JSON.parse(document.getElementById('aiGalleryData')?.textContent||'[]');
const dialog=document.getElementById('aiDetail') as HTMLDialogElement;
const image=document.getElementById('aiDetailImage') as HTMLImageElement;
const download=document.getElementById('aiDownload') as HTMLAnchorElement;
const sceneDialog=document.getElementById('aiSceneConfirm') as HTMLDialogElement;
const sceneDownload=document.getElementById('aiSceneDownload') as HTMLAnchorElement;
let scenePreviousOverflow='';
const text=(id:string,value:string)=>{document.getElementById(id)!.textContent=value;};
const tr=(key:string,fallback:string)=>((window as Window & {t?:(key:string)=>string}).t?.(key)||fallback);
let current:Item|undefined;
let previousOverflow='';
const finePointer=window.matchMedia('(hover: hover) and (pointer: fine)');

// Keep an opaque lock-screen underneath. Decode the incoming layer before fading
// it in so a late image response cannot flash an empty frame.
const cards=[...document.querySelectorAll<HTMLElement>('.wallpaper-card')];
const resetCards=()=>cards.forEach(card=>card.classList.remove('is-peeking'));
const warmups=new WeakMap<HTMLElement,()=>Promise<boolean>>();
cards.forEach(card=>{
  const layer=card.querySelector<HTMLImageElement>('.wallpaper-passcode')!;
  let loading:Promise<boolean>|undefined;
  let pointerInside=false;
  let keyboardInside=false;
  const warm=()=>{
    if(!loading){
      layer.src=layer.dataset.src!;
      loading=layer.decode().then(()=>true).catch(()=>{loading=undefined;return false;});
    }
    return loading;
  };
  const peek=async()=>{if(await warm())card.classList.toggle('is-peeking',!dialog.open&&(pointerInside||keyboardInside));};
  warmups.set(card,warm);
  card.addEventListener('pointerenter',event=>{if(event.pointerType==='touch'||!finePointer.matches)return;pointerInside=true;void peek();});
  card.addEventListener('pointerleave',()=>{pointerInside=false;if(!keyboardInside)card.classList.remove('is-peeking');});
  card.addEventListener('focusin',event=>{const target=event.target as HTMLElement;if(target.matches(':focus-visible')){keyboardInside=true;void peek();}});
  card.addEventListener('focusout',()=>{keyboardInside=false;if(!pointerInside)card.classList.remove('is-peeking');});
  dialog.addEventListener('close',()=>{pointerInside=false;keyboardInside=false;card.classList.remove('is-peeking');});
});
if('IntersectionObserver' in window){
  const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){void warmups.get(entry.target as HTMLElement)?.();observer.unobserve(entry.target);}
  }),{rootMargin:'240px'});
  cards.forEach(card=>observer.observe(card));
}

function open(index:number){
  const item=items[index];if(!item)return;
  if(item.category==='ai-scenes'){
    const allowed=!!item.original?.url&&item.downloadEnabled!==false;
    sceneDownload.hidden=!allowed;document.getElementById('aiSceneUnavailable')!.hidden=allowed;
    if(allowed&&item.original){sceneDownload.href=item.original.url;sceneDownload.download=item.original.filename;}else sceneDownload.removeAttribute('href');
    text('aiSceneDownloadStatus','');scenePreviousOverflow=document.body.style.overflow;
    sceneDialog.showModal();document.body.style.overflow='hidden';return;
  }
  current=item;resetCards();
  const width=item.wallpaper?.width||item.original?.width;const height=item.wallpaper?.height||item.original?.height;
  dialog.style.setProperty('--art-ratio',String(width&&height?width/height:9/16));
  image.onload=()=>{if(current===item&&image.naturalWidth&&image.naturalHeight)dialog.style.setProperty('--art-ratio',String(image.naturalWidth/image.naturalHeight));};
  image.src=item.image;image.alt=item.title;
  text('aiDetailTitle',item.title);
  text('aiDownloadStatus','');
  const original=item.original;const allowed=!!original?.url&&item.downloadEnabled!==false;
  document.getElementById('aiFileMeta')!.hidden=!original;
  if(original){
    text('aiFileDimensions',`${original.width} × ${original.height} px`);
    text('aiFileFormat',original.mime.split('/')[1]?.toUpperCase()||'');
    text('aiFileSize',`${(original.bytes/1048576).toFixed(2)} MB`);
  }
  download.hidden=!allowed;document.getElementById('aiNoOriginal')!.hidden=allowed;
  if(allowed&&original){download.href=original.url;download.download=original.filename;}else download.removeAttribute('href');
  previousOverflow=document.body.style.overflow;dialog.showModal();document.body.style.overflow='hidden';
}
document.querySelectorAll<HTMLButtonElement>('.ai-card-open').forEach(button=>button.addEventListener('click',()=>open(Number(button.dataset.index))));
document.querySelectorAll<HTMLButtonElement>('.ai-tab').forEach(button=>button.addEventListener('click',()=>{
  const category=button.dataset.filter;let count=0;resetCards();
  document.querySelectorAll<HTMLButtonElement>('.ai-tab').forEach(tab=>{tab.classList.toggle('active',tab===button);tab.setAttribute('aria-pressed',String(tab===button));});
  document.querySelectorAll<HTMLElement>('.ai-card').forEach(card=>{card.hidden=card.dataset.category!==category;if(!card.hidden)count++;});
  document.getElementById('aiEmpty')!.hidden=count>0;
}));
document.getElementById('aiClose')?.addEventListener('click',()=>dialog.close());
dialog.addEventListener('close',()=>{document.body.style.overflow=previousOverflow;image.removeAttribute('src');current=undefined;});
dialog.addEventListener('click',event=>{if(event.target!==dialog)return;const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();});
download.addEventListener('click',()=>text('aiDownloadStatus',tr('ai-download-started','已请求高清原图，请在浏览器下载列表中查看保存进度。')));
document.getElementById('aiSceneCancel')?.addEventListener('click',()=>sceneDialog.close());
sceneDownload.addEventListener('click',()=>{text('aiSceneDownloadStatus',tr('ai-download-started','已请求高清原图，请在浏览器下载列表中查看保存进度。'));sceneDialog.close();});
sceneDialog.addEventListener('close',()=>{document.body.style.overflow=scenePreviousOverflow;});
sceneDialog.addEventListener('click',event=>{if(event.target!==sceneDialog)return;const r=sceneDialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)sceneDialog.close();});

