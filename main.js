(function () {
  var root = document.documentElement;
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  /* language */
  var langBtn = document.getElementById('langBtn');
  function setLang(l) {
    root.dataset.lang = l; root.lang = l;
    langBtn.textContent = l === 'ko' ? 'EN' : '한';
    set('lang', l);
    if (window.__hystRedraw) window.__hystRedraw();
  }
  setLang(root.dataset.lang === 'en' ? 'en' : 'ko');
  langBtn.addEventListener('click', function () { setLang(root.dataset.lang === 'ko' ? 'en' : 'ko'); });

  /* theme */
  document.getElementById('themeBtn').addEventListener('click', function () {
    var dark = root.dataset.theme === 'dark';
    root.dataset.theme = dark ? 'light' : 'dark';
    set('theme', root.dataset.theme);
    if (window.__hystRedraw) window.__hystRedraw();
  });

  /* mobile menu */
  var menu = document.getElementById('menu'), menuBtn = document.getElementById('menuBtn');
  menuBtn.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();


  /* ---------- research gallery + lightbox ---------- */
  var gals = document.querySelectorAll('.gal');
  if (gals.length) {
    var lb = document.createElement('div');
    lb.className = 'lb';
    lb.innerHTML = '<button class="lb-x" type="button" aria-label="Close">&times;</button><button class="lb-p" type="button" aria-label="Previous">&#8249;</button><img alt=""><div class="lb-cap"></div><button class="lb-n" type="button" aria-label="Next">&#8250;</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.lb-cap'), cur = null, curI = 0;
    function show(g, i) {
      var items = g.querySelectorAll('.gal-item'), ths = g.querySelectorAll('.gal-th');
      i = (i + items.length) % items.length;
      items.forEach(function (el, k) { el.classList.toggle('on', k === i); });
      ths.forEach(function (el, k) { el.classList.toggle('on', k === i); });
      return i;
    }
    function lbShow(g, i) {
      var items = g.querySelectorAll('.gal-item');
      curI = show(g, i); cur = g;
      lbImg.src = items[curI].querySelector('img').src;
      lbCap.innerHTML = items[curI].querySelector('figcaption').innerHTML;
      var multi = items.length > 1;
      lb.querySelector('.lb-p').style.display = multi ? '' : 'none';
      lb.querySelector('.lb-n').style.display = multi ? '' : 'none';
    }
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; }
    gals.forEach(function (g) {
      g.querySelectorAll('.gal-th').forEach(function (t, k) { t.addEventListener('click', function () { show(g, k); }); });
      g.querySelectorAll('.gal-zoom').forEach(function (z, k) {
        z.addEventListener('click', function () { lbShow(g, k); lb.classList.add('open'); document.body.style.overflow = 'hidden'; });
      });
    });
    lb.querySelector('.lb-x').addEventListener('click', close);
    lb.querySelector('.lb-p').addEventListener('click', function (e) { e.stopPropagation(); lbShow(cur, curI - 1); });
    lb.querySelector('.lb-n').addEventListener('click', function (e) { e.stopPropagation(); lbShow(cur, curI + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') lbShow(cur, curI - 1);
      else if (e.key === 'ArrowRight') lbShow(cur, curI + 1);
    });
  }

  /* ---------- hysteresis figure (home) ---------- */
  var cv = document.getElementById('hyst');
  if (!cv) return;
  var ctx = cv.getContext('2d');

  // AISC 341 beam-to-column qualification protocol: [story drift %, cycles]
  var PROTOCOL = [[0.375, 6], [0.5, 6], [0.75, 6], [1, 4], [1.5, 2], [2, 2], [3, 2], [4, 2]];
  var CYCLES = PROTOCOL.reduce(function (s, p) { return s + p[1]; }, 0);

  // Bouc–Wen hysteresis with mild strength degradation (illustrative)
  var pts = [], x = 0, z = 0, E = 0, cyc = 0;
  var A = 1, b = 0.55, g = 0.45, n = 1.6, a = 0.05, dx = 0.01;
  function step(xt) {
    while (Math.abs(xt - x) > 1e-9) {
      var d = Math.max(-dx, Math.min(dx, xt - x));
      z += (A - Math.pow(Math.abs(z), n) * (b * Math.sign(d * z) + g)) * d;
      x += d;
      var deg = Math.max(0.78, 1 - 0.0018 * E);
      E += Math.abs((1 - a) * z * d) * (Math.abs(x) > 1.5 ? 1 : 0.15);
      pts.push([x, (a * x + (1 - a) * z) * deg, cyc]);
    }
  }
  PROTOCOL.forEach(function (p) {
    for (var i = 0; i < p[1]; i++) { cyc++; step(p[0]); step(-p[0]); step(0); }
  });
  var Fmax = pts.reduce(function (m, p) { return Math.max(m, Math.abs(p[1])); }, 0);
  pts.forEach(function (p) { p[1] = p[1] / Fmax * 1.05; });

  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W, H, box, colors, XMAX = 5, YMAX = 1.3;
  function css(v) { return getComputedStyle(root).getPropertyValue(v).trim(); }
  function readColors() {
    colors = { line: css('--line'), line2: css('--line-2'), muted: css('--muted'), ink: css('--ink'),
      accent: css('--accent'), faint: css('--plot-faint'), bg: css('--plot-bg') };
  }
  function size() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2), r = cv.getBoundingClientRect();
    W = r.width; H = r.height;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var narrow = W < 480;
    box = { l: narrow ? 40 : 52, r: narrow ? 14 : 22, t: 52, b: 40 };
  }
  function X(v) { return box.l + (v + XMAX) / (2 * XMAX) * (W - box.l - box.r); }
  function Y(v) { return box.t + (YMAX - v) / (2 * YMAX) * (H - box.t - box.b); }
  var FONT = '"Pretendard Variable", Pretendard, system-ui, sans-serif';

  function axes(c) {
    ctx.lineWidth = 1; ctx.font = '500 11px ' + FONT; ctx.fillStyle = c.muted;
    ctx.textAlign = 'center'; ctx.textBaseline = 'top';
    [-4, -2, 0, 2, 4].forEach(function (t) {
      ctx.strokeStyle = t === 0 ? c.line2 : c.line;
      ctx.beginPath(); ctx.moveTo(X(t), Y(YMAX)); ctx.lineTo(X(t), Y(-YMAX)); ctx.stroke();
      ctx.fillText((t > 0 ? '+' : t < 0 ? '−' : '') + Math.abs(t), X(t), Y(-YMAX) + 10);
    });
    ctx.textAlign = 'right'; ctx.textBaseline = 'middle';
    [-1, 0, 1].forEach(function (t) {
      ctx.strokeStyle = t === 0 ? c.line2 : c.line;
      ctx.beginPath(); ctx.moveTo(X(-XMAX), Y(t)); ctx.lineTo(X(XMAX), Y(t)); ctx.stroke();
      ctx.fillText((t < 0 ? '−' : '') + Math.abs(t).toFixed(1), X(-XMAX) - 10, Y(t));
    });
    ctx.textAlign = 'right'; ctx.textBaseline = 'bottom';
    ctx.fillText(root.dataset.lang === 'en' ? 'Story drift ratio (%)' : '층간변위비 (%)', X(XMAX), Y(0) - 8);
    ctx.textAlign = 'left'; ctx.textBaseline = 'top';
    ctx.fillText('M / Mp', X(0) + 8, Y(YMAX) + 2);
  }
  function path(from, to) {
    ctx.beginPath(); ctx.moveTo(X(pts[from][0]), Y(pts[from][1]));
    for (var i = from + 1; i <= to; i += 2) ctx.lineTo(X(pts[i][0]), Y(pts[i][1]));
    ctx.lineTo(X(pts[to][0]), Y(pts[to][1])); ctx.stroke();
  }
  function sgn(v) { return v >= 0 ? '+' : '−'; }

  var idx = 0, holdUntil = 0, last = 0;
  function draw() {
    var c = colors;
    ctx.fillStyle = c.bg; ctx.fillRect(0, 0, W, H);
    axes(c);
    ctx.lineJoin = 'round'; ctx.lineCap = 'round';
    ctx.strokeStyle = c.faint; ctx.lineWidth = 1; path(0, pts.length - 1);
    var end = Math.max(1, Math.floor(idx)), p = pts[end];
    ctx.strokeStyle = c.accent; ctx.lineWidth = 1.8; path(0, end);
    ctx.fillStyle = c.bg; ctx.beginPath(); ctx.arc(X(p[0]), Y(p[1]), 6, 0, 7); ctx.fill();
    ctx.fillStyle = c.accent; ctx.beginPath(); ctx.arc(X(p[0]), Y(p[1]), 4, 0, 7); ctx.fill();
    // readout
    ctx.font = '600 12px ' + FONT; ctx.textBaseline = 'middle'; ctx.textAlign = 'left';
    var items = [['θ', sgn(p[0]) + Math.abs(p[0]).toFixed(2) + '%'], ['M/Mp', sgn(p[1]) + Math.abs(p[1]).toFixed(2)], ['Cycle', p[2] + ' / ' + CYCLES]];
    var xx = 18;
    items.forEach(function (it) {
      ctx.fillStyle = c.muted; ctx.font = '500 11px ' + FONT; ctx.fillText(it[0], xx, 24);
      xx += ctx.measureText(it[0]).width + 6;
      ctx.fillStyle = c.ink; ctx.font = '600 12px ' + FONT; ctx.fillText(it[1], xx, 24);
      xx += ctx.measureText(it[1] + '  ').width + 14;
    });
  }
  function frame(t) {
    if (!last) last = t;
    var dt = Math.min(64, t - last); last = t;
    if (idx < pts.length - 1) {
      idx = Math.min(pts.length - 1, idx + dt * pts.length / 16000);
      if (idx >= pts.length - 1) holdUntil = t + 2500;
    } else if (t > holdUntil) { idx = 0; }
    draw();
    requestAnimationFrame(frame);
  }
  function init() {
    size(); readColors();
    if (reduce) { idx = pts.length - 1; draw(); }
    else { idx = pts.length * 0.55; draw(); requestAnimationFrame(frame); }
  }
  window.__hystRedraw = function () { if (!W) return; readColors(); draw(); };
  window.addEventListener('resize', function () { size(); draw(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(init); else init();
})();
