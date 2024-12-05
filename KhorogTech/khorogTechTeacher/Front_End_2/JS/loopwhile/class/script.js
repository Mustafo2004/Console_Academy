 // Array of objects with different textContents and image sources
 const items = [
    { text: 'Item 1', imgSrc: '/images/place.png' },
    { text: 'Item 2', imgSrc: '/images/tour-guide 1.png' },
    { text: 'Item 3', imgSrc: '/images/logo.png' },
    { text: 'Item 4', imgSrc: '/images/image1.png' },
    { text: 'Item 5', imgSrc: '/images/chorkunja.png' }
  ];

  const container = document.getElementById('content');
  let i = 0;
  while (i < items.length) {
    const item = items[i];
    const div = document.createElement('div');
    div.classList.add('item');

    const img = document.createElement('img');
    img.src = item.imgSrc;

    const p = document.createElement('p');
    p.textContent = item.text;

    div.appendChild(img);
    div.appendChild(p);
    container.appendChild(div);
    i++;
  }