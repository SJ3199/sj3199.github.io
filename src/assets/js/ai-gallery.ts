const grid = document.getElementById('aiGalleryGrid')!;
const tabs = [...document.querySelectorAll<HTMLButtonElement>('.ai-tab')];
const cards = [...grid.querySelectorAll<HTMLElement>('[data-category]')];
const wallpaperHint = document.getElementById('wallpaperHint')!;
const wallpaperStatus = document.getElementById('wallpaperDownloadStatus')!;
const emptyState = document.getElementById('aiEmpty')!;

function selectCategory(button: HTMLButtonElement) {
  const category = button.dataset.filter!;
  let hasCards = false;
  for (const tab of tabs) {
    tab.classList.toggle('active', tab === button);
    tab.setAttribute('aria-pressed', String(tab === button));
  }
  for (const card of cards) {
    card.hidden = card.dataset.category !== category;
    if (!card.hidden) hasCards = true;
  }
  grid.dataset.activeCategory = category;
  wallpaperHint.hidden = category !== 'texture-wallpapers' || !hasCards;
  emptyState.hidden = hasCards;
  wallpaperStatus.textContent = '';
}

function selectFromHash() {
  const selected = tabs.find(tab => `#${tab.dataset.filter}` === location.hash);
  selectCategory(selected ?? tabs[0]);
}

for (const tab of tabs) {
  tab.addEventListener('click', () => {
    selectCategory(tab);
    const url = new URL(location.href);
    url.hash = tab === tabs[0] ? '' : tab.dataset.filter!;
    history.replaceState(history.state, '', url);
  });
}
selectFromHash();
window.addEventListener('hashchange', selectFromHash);

const downloadStarted = () => (window as Window & { t?: (key: string) => string })
  .t?.('ai-download-started') || '已请求高清原图，请在浏览器下载列表中查看保存进度。';

grid.querySelectorAll<HTMLAnchorElement>('a.wallpaper-preview').forEach(link => {
  link.addEventListener('click', () => { wallpaperStatus.textContent = downloadStarted(); });
});

const sceneDialog = document.getElementById('aiSceneConfirm') as HTMLDialogElement;
const sceneDownload = document.getElementById('aiSceneDownload') as HTMLAnchorElement;
const sceneUnavailable = document.getElementById('aiSceneUnavailable')!;
let previousOverflow = '';

grid.querySelectorAll<HTMLButtonElement>('.ai-card-open').forEach(button => {
  button.addEventListener('click', () => {
    const { originalUrl, originalFilename } = button.dataset;
    sceneDownload.hidden = !originalUrl;
    sceneUnavailable.hidden = Boolean(originalUrl);
    if (originalUrl) {
      sceneDownload.href = originalUrl;
      sceneDownload.download = originalFilename ?? '';
    } else {
      sceneDownload.removeAttribute('href');
    }
    previousOverflow = document.body.style.overflow;
    sceneDialog.showModal();
    document.body.style.overflow = 'hidden';
  });
});

document.getElementById('aiSceneCancel')?.addEventListener('click', () => sceneDialog.close());
sceneDownload.addEventListener('click', () => sceneDialog.close());
sceneDialog.addEventListener('close', () => { document.body.style.overflow = previousOverflow; });
sceneDialog.addEventListener('click', event => {
  if (event.target !== sceneDialog) return;
  const bounds = sceneDialog.getBoundingClientRect();
  if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) {
    sceneDialog.close();
  }
});
