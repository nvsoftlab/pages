/* AIR-Serwis — landing page interactions */
(function () {
  'use strict';

  // Lead forms are POSTed as JSON to <body data-form-endpoint="...">
  // (e.g. a Formspree / Web3Forms URL). Without it, the visitor's mail
  // client opens with a pre-filled message to CONTACT_EMAIL.
  var CONTACT_EMAIL = 'patryk@air-serwis.net';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var mobileMq = window.matchMedia('(max-width: 760px)');
  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };

  /* ---------- Year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Hero intro ---------- */
  var hero = $('.hero');
  var startHero = function () { setTimeout(function () { hero.classList.add('is-loaded'); }, 30); };
  if (document.fonts && document.fonts.ready) {
    // wait for fonts (max 600ms) so the headline doesn't reflow mid-animation
    Promise.race([document.fonts.ready, new Promise(function (r) { setTimeout(r, 600); })]).then(startHero);
  } else {
    startHero();
  }

  /* ---------- Header shadow ---------- */
  var header = $('#header');
  var onScrollHeader = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };

  /* ---------- Scroll reveal ---------- */
  // stagger siblings that share a parent
  var revealEls = $$('[data-reveal]');
  var groups = new Map();
  revealEls.forEach(function (el) {
    var p = el.parentElement;
    var n = groups.get(p) || 0;
    el.style.setProperty('--d', (Math.min(n, 6) * 0.08) + 's');
    groups.set(p, n + 1);
  });

  var finishReveal = function (el) {
    // once revealed, drop the attribute so hover transitions aren't delayed
    var delay = parseFloat(getComputedStyle(el).getPropertyValue('--d')) || 0;
    setTimeout(function () { el.removeAttribute('data-reveal'); }, (delay + 0.9) * 1000);
  };

  /* ---------- Process steps ---------- */
  var steps = $('[data-steps]');
  $$('.step', steps).forEach(function (s, i) { s.style.setProperty('--i', i); });
  $$('.step__icon *').forEach(function (shape) { shape.setAttribute('pathLength', '1'); });

  /* ---------- Editor content (.entry-content from the CMS) ---------- */
  // Headings get ids (WordPress doesn't add them) and feed the table of contents.
  var slugify = function (t) {
    return t.toLowerCase().replace(/ł/g, 'l').normalize('NFD').replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'sekcja';
  };
  var entryEls = [];
  var headings = $$('.entry-content h2');
  headings.forEach(function (h) {
    if (!h.id) {
      var base = slugify(h.textContent), id = base, n = 2;
      while (document.getElementById(id)) id = base + '-' + n++;
      h.id = id;
    }
    entryEls.push(h);
  });
  $$('.entry-content > ul, .entry-content > ol').forEach(function (list) {
    $$(':scope > li', list).forEach(function (li, i) { li.style.setProperty('--i', i); });
    entryEls.push(list);
  });
  var tocNav = $('[data-toc]');
  if (tocNav) {
    headings.forEach(function (h, i) {
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.innerHTML = '<span>' + (i < 9 ? '0' : '') + (i + 1) + '</span>';
      a.appendChild(document.createTextNode(h.textContent));
      tocNav.appendChild(a);
    });
  }

  /* ---------- Infographic lines ---------- */
  var infographic = $('.infographic');
  if (infographic) {
    var svg = $('.infographic__lines', infographic);
    $$('.ig-line, .ig-pipe', svg).forEach(function (path, i) {
      path.setAttribute('pathLength', '1');
      path.style.setProperty('--i', i);
      // a light pulse that travels along each drawn line
      var flow = path.cloneNode();
      flow.setAttribute('class', 'ig-flow' + (path.classList.contains('ig-line') ? ' ig-flow--rev' : ''));
      flow.style.animationDelay = (1.9 + i * 0.35) + 's';
      svg.appendChild(flow);
    });
    $$('.ig-dot', infographic).forEach(function (d, i) { d.style.setProperty('--i', i); });
  }

  /* ---------- Counters ---------- */
  var runCounter = function (el) {
    var raw = el.getAttribute('data-count');
    var decimals = raw.indexOf(',') > -1 ? raw.split(',')[1].length : 0;
    var target = parseFloat(raw.replace(',', '.'));
    if (reduceMotion || isNaN(target)) return;
    var dur = 1400, t0 = null;
    var tick = function (t) {
      if (!t0) t0 = t;
      var k = Math.min(1, (t - t0) / dur);
      var eased = 1 - Math.pow(1 - k, 3);
      el.textContent = (target * eased).toFixed(decimals).replace('.', ',');
      if (k < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        io.unobserve(el);
        if (el.hasAttribute('data-count')) { runCounter(el); return; }
        el.classList.add('is-in');
        if (el.hasAttribute('data-reveal')) finishReveal(el);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });

    revealEls.forEach(function (el) { io.observe(el); });
    if (steps) io.observe(steps);
    entryEls.forEach(function (el) { io.observe(el); });
    io.observe($('.footer__bottom'));
    $$('[data-count]').forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); el.removeAttribute('data-reveal'); });
    if (steps) steps.classList.add('is-in');
    entryEls.forEach(function (el) { el.classList.add('is-in'); });
    $('.footer__bottom').classList.add('is-in');
  }

  /* ---------- Chips ---------- */
  $$('.chips').forEach(function (group) {
    group.addEventListener('click', function (e) {
      var chip = e.target.closest('.chip');
      if (!chip) return;
      $$('.chip', group).forEach(function (c) {
        var on = c === chip;
        c.classList.toggle('is-active', on);
        c.setAttribute('aria-checked', on ? 'true' : 'false');
      });
    });
  });

  /* ---------- Mobile placeholder swap (contact textarea) ---------- */
  var kMsg = $('#k-msg');
  var syncPlaceholder = function () {
    if (!kMsg) return;
    if (!kMsg.dataset.placeholderDesk) kMsg.dataset.placeholderDesk = kMsg.placeholder;
    kMsg.placeholder = mobileMq.matches ? kMsg.dataset.placeholderMob : kMsg.dataset.placeholderDesk;
  };
  syncPlaceholder();

  /* ---------- Forms ---------- */
  var validPhone = function (v) { return v.replace(/\D/g, '').length >= 9; };

  $$('.lead-form').forEach(function (form) {
    var name = form.querySelector('[name="imie"]');
    var phone = form.querySelector('[name="telefon"]');
    var msg = form.querySelector('[name="wiadomosc"]');

    var check = function (input, ok) {
      input.closest('.field').classList.toggle('is-invalid', !ok);
      input.setAttribute('aria-invalid', ok ? 'false' : 'true');
      return ok;
    };
    [name, phone].forEach(function (input) {
      input.addEventListener('input', function () {
        if (input.closest('.field').classList.contains('is-invalid')) {
          check(input, input === phone ? validPhone(input.value) : input.value.trim().length > 0);
        }
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var okName = check(name, name.value.trim().length > 0);
      var okPhone = check(phone, validPhone(phone.value));
      if (!okName || !okPhone) {
        (okName ? phone : name).focus();
        return;
      }

      var chip = form.querySelector('.chip.is-active');
      var kind = chip && chip.offsetParent !== null ? chip.textContent.trim() : '';
      var data = {
        imie: name.value.trim(),
        telefon: phone.value.trim(),
        rodzaj: kind,
        wiadomosc: msg.value.trim(),
        zrodlo: form.getAttribute('data-form'),
        usluga: form.getAttribute('data-service') || ''
      };

      var btn = form.querySelector('.btn--submit');
      btn.classList.add('is-loading');

      var done = function () {
        var success = form.parentElement.querySelector('.form-success');
        form.hidden = true;
        success.hidden = false;
        success.setAttribute('tabindex', '-1');
        success.focus({ preventScroll: true });
      };

      var endpoint = document.body.getAttribute('data-form-endpoint');
      if (endpoint) {
        fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(data)
        }).then(function (r) {
          if (!r.ok) throw new Error(r.status);
          done();
        }).catch(function () {
          btn.classList.remove('is-loading');
          sendByMail(data);
          done();
        });
      } else {
        sendByMail(data);
        done();
      }
    });
  });

  function sendByMail(d) {
    var body = [
      'Imię: ' + d.imie,
      'Telefon: ' + d.telefon,
      d.usluga ? 'Usługa: ' + d.usluga : '',
      d.rodzaj ? 'Czego dotyczy: ' + d.rodzaj : '',
      d.wiadomosc ? '\n' + d.wiadomosc : ''
    ].filter(Boolean).join('\n');
    var subject = 'Zapytanie o wycenę' + (d.usluga ? ' — ' + d.usluga : d.rodzaj ? ' — ' + d.rodzaj : '');
    window.location.href = 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  }

  /* ---------- FAQ accordion (one open at a time) ---------- */
  var accs = $$('.acc');
  accs.forEach(function (acc) {
    var btn = $('.acc__btn', acc);
    btn.addEventListener('click', function () {
      var open = !acc.classList.contains('is-open');
      accs.forEach(function (a) {
        a.classList.remove('is-open');
        $('.acc__btn', a).setAttribute('aria-expanded', 'false');
      });
      if (open) {
        acc.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ---------- Drawer ---------- */
  var drawer = $('#drawer');
  var burger = $('.burger');
  var lastFocus = null;
  var openDrawer = function () {
    lastFocus = document.activeElement;
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    burger.setAttribute('aria-expanded', 'true');
    document.body.classList.add('no-scroll');
    setTimeout(function () { $('.drawer__close', drawer).focus(); }, 50);
  };
  var closeDrawer = function () {
    if (!drawer.classList.contains('is-open')) return;
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('no-scroll');
    if (lastFocus) lastFocus.focus({ preventScroll: true });
  };
  burger.addEventListener('click', openDrawer);
  $$('[data-close]', drawer).forEach(function (el) { el.addEventListener('click', closeDrawer); });

  /* ---------- Lightbox ---------- */
  var lightbox = $('.lightbox');
  var lbImg = $('img', lightbox);
  var openLightbox = function (src, alt) {
    lbImg.src = src; lbImg.alt = alt || '';
    lightbox.hidden = false;
    document.body.classList.add('no-scroll');
    $('.lightbox__close', lightbox).focus();
  };
  var closeLightbox = function () {
    if (lightbox.hidden) return;
    lightbox.hidden = true;
    document.body.classList.remove('no-scroll');
  };
  $$('[data-full]').forEach(function (item) {
    item.addEventListener('click', function () {
      var img = $('img', item);
      openLightbox(item.getAttribute('data-full'), img.alt);
    });
  });
  lightbox.addEventListener('click', closeLightbox);

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeDrawer(); closeLightbox(); }
  });

  /* ---------- Dock (desktop) + scroll spy ---------- */
  var dock = $('.dock');
  var mbar = $('.mbar');
  var contact = $('#kontakt');
  // only in-page anchors take part in the scroll spy (sub-pages keep their static state)
  var navLinks = $('.nav__link.is-active') ? [] // sub-page: the header marks its own section
    : $$('.nav__link, .drawer__nav a').filter(function (a) { return a.getAttribute('href').charAt(0) === '#'; });
  var sections = ['uslugi', 'o-nas', 'proces', 'realizacje', 'faq', 'kontakt']
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);

  var updateDock = function () {
    var past = window.scrollY > 700;
    var nearContact = contact.getBoundingClientRect().top < window.innerHeight * 0.9;
    var show = past && !nearContact;
    dock.classList.toggle('is-visible', show);
    $$('a', dock).forEach(function (a) { a.tabIndex = show ? 0 : -1; });
    dock.setAttribute('aria-hidden', show ? 'false' : 'true');
  };

  var updateSpy = function () {
    var y = window.innerHeight * 0.35;
    var current = null;
    sections.forEach(function (s) { if (s.getBoundingClientRect().top <= y) current = s.id; });
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) current = 'kontakt';
    navLinks.forEach(function (a) { a.classList.toggle('is-active', a.getAttribute('href') === '#' + current); });
  };

  /* ---------- Article: table of contents spy ---------- */
  var tocLinks = $$('.toc a');
  var tocTargets = tocLinks.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
  var updateToc = function () {
    if (!tocLinks.length) return;
    var y = window.innerHeight * 0.3, current = -1;
    tocTargets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top <= y) current = i; });
    tocLinks.forEach(function (a, i) { a.classList.toggle('is-active', i === current); });
  };

  /* ---------- Article: copy link ---------- */
  $$('[data-share]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var url = window.location.href.split('#')[0];
      var ok = function () {
        btn.textContent = 'Skopiowano ✓';
        btn.classList.add('is-done');
        setTimeout(function () { btn.textContent = 'Kopiuj link'; btn.classList.remove('is-done'); }, 2200);
      };
      if (navigator.share && window.matchMedia('(pointer: coarse)').matches) {
        navigator.share({ title: document.title, url: url }).catch(function () {});
      } else if (navigator.clipboard) {
        navigator.clipboard.writeText(url).then(ok, function () { window.prompt('Skopiuj link:', url); });
      } else {
        window.prompt('Skopiuj link:', url);
      }
    });
  });

  var ticking = false;
  var onScroll = function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      onScrollHeader();
      updateDock();
      updateSpy();
      updateToc();
      ticking = false;
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();

  setTimeout(function () { mbar.classList.add('is-visible'); }, reduceMotion ? 0 : 900);

  var onMq = function () {
    syncPlaceholder();
  };
  if (mobileMq.addEventListener) mobileMq.addEventListener('change', onMq);
  else mobileMq.addListener(onMq);
  window.matchMedia('(max-width: 1100px)').addEventListener('change', function (e) { if (!e.matches) closeDrawer(); });
})();
