(function () {
  var root = document.documentElement;
  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function set(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  /* language */
  var langBtn = document.getElementById('langBtn');
  function setLang(l) { root.dataset.lang = l; root.lang = l; langBtn.textContent = l === 'ko' ? 'EN' : '한'; set('lang', l); }
  setLang(root.dataset.lang === 'en' ? 'en' : 'ko');
  langBtn.addEventListener('click', function () { setLang(root.dataset.lang === 'ko' ? 'en' : 'ko'); });

  /* theme */
  document.getElementById('themeBtn').addEventListener('click', function () {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    set('theme', root.dataset.theme);
  });

  /* mobile menu */
  var menu = document.getElementById('menu'), menuBtn = document.getElementById('menuBtn');
  menuBtn.addEventListener('click', function () {
    var open = menu.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    menuBtn.textContent = open ? 'Close' : 'Menu';
  });

  var yr = document.getElementById('yr');
  if (yr) yr.textContent = new Date().getFullYear();

  /* home slideshow */
  var show = document.getElementById('show');
  if (show) {
    var slides = show.querySelectorAll('.slide'), caps = document.querySelectorAll('.caps .sc'),
        num = document.getElementById('showNum'), cur = 0, sec = +show.dataset.sec || 5, timer;
    function go(i) {
      cur = (i + slides.length) % slides.length;
      slides.forEach(function (s, k) { s.classList.toggle('on', k === cur); });
      caps.forEach(function (s, k) { s.classList.toggle('on', k === cur); });
      if (num) num.textContent = (cur + 1 < 10 ? '0' : '') + (cur + 1);
      var nx = slides[(cur + 1) % slides.length]; if (nx) nx.loading = 'eager';
    }
    function start() { stop(); timer = setInterval(function () { go(cur + 1); }, sec * 1000); }
    function stop() { if (timer) clearInterval(timer); }
    if (slides.length > 1 && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) start();
    show.addEventListener('click', function () { go(cur + 1); start(); });
    show.style.cursor = 'pointer';
  }

  /* research gallery + lightbox */
  var gals = document.querySelectorAll('.gal');
  if (gals.length) {
    var lb = document.createElement('div');
    lb.className = 'lb';
    lb.innerHTML = '<button class="lb-x" type="button" aria-label="Close">&times;</button><button class="lb-p" type="button" aria-label="Previous">&#8249;</button><img alt=""><div class="lb-cap"></div><button class="lb-n" type="button" aria-label="Next">&#8250;</button>';
    document.body.appendChild(lb);
    var lbImg = lb.querySelector('img'), lbCap = lb.querySelector('.lb-cap'), g0 = null, gi = 0;
    function showG(g, i) {
      var items = g.querySelectorAll('.gal-item'), ths = g.querySelectorAll('.gal-th');
      i = (i + items.length) % items.length;
      items.forEach(function (el, k) { el.classList.toggle('on', k === i); });
      ths.forEach(function (el, k) { el.classList.toggle('on', k === i); });
      return i;
    }
    function lbShow(g, i) {
      var items = g.querySelectorAll('.gal-item');
      gi = showG(g, i); g0 = g;
      lbImg.src = items[gi].querySelector('img').src;
      lbCap.innerHTML = items[gi].querySelector('figcaption').innerHTML;
      var multi = items.length > 1;
      lb.querySelector('.lb-p').style.display = multi ? '' : 'none';
      lb.querySelector('.lb-n').style.display = multi ? '' : 'none';
    }
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; }
    gals.forEach(function (g) {
      g.querySelectorAll('.gal-th').forEach(function (t, k) { t.addEventListener('click', function () { showG(g, k); }); });
      g.querySelectorAll('.gal-zoom').forEach(function (z, k) {
        z.addEventListener('click', function () { lbShow(g, k); lb.classList.add('open'); document.body.style.overflow = 'hidden'; });
      });
    });
    lb.querySelector('.lb-x').addEventListener('click', close);
    lb.querySelector('.lb-p').addEventListener('click', function (e) { e.stopPropagation(); lbShow(g0, gi - 1); });
    lb.querySelector('.lb-n').addEventListener('click', function (e) { e.stopPropagation(); lbShow(g0, gi + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      else if (e.key === 'ArrowLeft') lbShow(g0, gi - 1);
      else if (e.key === 'ArrowRight') lbShow(g0, gi + 1);
    });
  }
})();
