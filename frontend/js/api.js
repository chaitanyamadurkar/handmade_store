
/* ─────────────────────────────────────────────
   api.js — Shared API helper for Handmade Haven
   Change BASE_URL to your Django server address
───────────────────────────────────────────────── */

const BASE_URL = 'http://127.0.0.1:8000';

const API = {
  async get(endpoint) {
    const res = await fetch(`${BASE_URL}${endpoint}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  },

  async post(endpoint, data) {
    const res = await fetch(`${BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    const json = await res.json();
    if (!res.ok) throw { status: res.status, data: json };
    return json;
  },
};

/* ── Toast Notifications ── */
function showToast(message, type = 'success') {
  let toast = document.getElementById('global-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'global-toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.className = `toast ${type}`;
  toast.innerHTML = `<span>${type === 'success' ? '✓' : '✗'}</span> ${message}`;
  toast.classList.add('show');
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 3800);
}

/* ── URL Params helper ── */
function getParam(key) {
  return new URLSearchParams(window.location.search).get(key);
}

/* ── Format currency ── */
function formatPrice(price) {
  return `₹${parseFloat(price).toLocaleString('en-IN', { minimumFractionDigits: 2 })}`;
}

/* ── Product Card HTML ── */
function productCardHTML(p) {
  const imgHTML = p.image_url
    ? `<img src="${p.image_url}" alt="${p.name}" loading="lazy" />`
    : `<div class="placeholder">🧶</div>`;

  return `
    <div class="product-card fade-up" onclick="location.href='product.html?id=${p.id}'">
      <div class="product-card-img">
        ${imgHTML}
        ${p.is_featured ? '<span class="badge-featured">Featured</span>' : ''}
        ${!p.in_stock ? '<span class="badge-out">Out of Stock</span>' : ''}
      </div>
      <div class="product-card-body">
        <div class="product-cat">${p.category_name || 'Handmade'}</div>
        <div class="product-name">${p.name}</div>
        <div class="product-desc">${p.description}</div>
        <div class="product-footer">
          <div class="product-price">${formatPrice(p.price)}</div>
          <button class="btn btn-primary btn-card" onclick="event.stopPropagation(); location.href='product.html?id=${p.id}'">
            ${p.in_stock ? 'Order Now' : 'View Details'}
          </button>
        </div>
      </div>
    </div>
  `;
}
