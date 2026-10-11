'use strict';
const search = document.querySelector('#gallery-search');
if (search) {
  const input = document.querySelector('#search');
  const project = document.querySelector('#project');
  const cards = [...document.querySelectorAll('.concept')];
  const groups = [...document.querySelectorAll('.concept-group')];
  const count = document.querySelector('#result-count');
  function filter() {
    const words = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const card of cards) {
      const matches = (project.value === 'all' || card.dataset.project === project.value)
        && words.every(word => card.dataset.search.includes(word));
      card.hidden = !matches;
      if (matches) visible++;
    }
    for (const group of groups) group.hidden = !group.querySelector('.concept:not([hidden])');
    count.textContent = `Showing ${visible} of ${cards.length} concepts`;
    document.querySelector('#no-results').hidden = visible > 0;
  }
  search.addEventListener('submit', event => event.preventDefault());
  input.addEventListener('input', filter);
  project.addEventListener('change', filter);
  search.addEventListener('reset', () => requestAnimationFrame(filter));
  const dialog = document.querySelector('#image-dialog');
  let opener;
  document.querySelectorAll('.zoom').forEach(anchor => anchor.addEventListener('click', event => {
    if (!dialog || !dialog.showModal || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
    event.preventDefault();
    opener = anchor;
    document.querySelector('#image-title').textContent = anchor.dataset.title;
    const image = document.querySelector('#dialog-image');
    image.src = anchor.dataset.image;
    image.alt = anchor.dataset.title;
    document.querySelector('#dialog-source').href = anchor.href;
    dialog.showModal();
  }));
  document.querySelector('#close-dialog').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    const rect = dialog.getBoundingClientRect();
    if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
  });
  dialog.addEventListener('close', () => { if (opener) opener.focus(); });
}
