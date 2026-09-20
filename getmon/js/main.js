/* GETMON — site interactions */
(function () {
  'use strict';

  // Lead forms are POSTed as JSON to <body data-form-endpoint="...">
  // (e.g. a Formspree / Web3Forms URL, or a WordPress admin-ajax handler).
  // Without it, the visitor's mail client opens with a pre-filled message.
  var CONTACT_EMAIL = 'biuro@getmon.pl';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------- Year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Hero intro ---------- */
  var hero = $('.hero');
  var startHero = function () {
    if (!hero) return;
    setTimeout(function () { hero.classList.add('is-loaded'); }, 30);
  };
  if (document.fonts && document.fonts.ready) {
    // wait for fonts (max 600ms) so the headline doesn't reflow mid-animation
    Promise.race([document.fonts.ready, new Promise(function (r) { setTimeout(r, 600); })]).then(startHero);
  } else {
    startHero();
  }

  /* ---------- Header shadow ---------- */
  var header = $('#header');
  var onScrollHeader = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };

  /* ---------- Scroll reveal (siblings stagger) ---------- */
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
    var d = parseFloat(getComputedStyle(el).getPropertyValue('--d')) || 0;
    setTimeout(function () { el.removeAttribute('data-reveal'); }, (d + 0.9) * 1000);
  };

  /* ---------- Process steps ---------- */
  var steps = $('[data-steps]');
  if (steps) {
    $$('.step', steps).forEach(function (s, i) { s.style.setProperty('--i', i); });
    // normalise every icon path to length 1 so one CSS rule draws them all
    $$('.step__icon *', steps).forEach(function (shape) { shape.setAttribute('pathLength', '1'); });
  }

  /* ---------- Schematic diagram: draw the lines, then flow the pulses ---------- */
  var diagram = $('[data-diagram]');
  if (diagram) {
    var svg = $('svg', diagram);
    // stagger the draw-in, and give every stroke a unit length
    $$('.dg-draw, .dg-pipe, .dg-signal', svg).forEach(function (path, i) {
      path.setAttribute('pathLength', '1');
      path.style.setProperty('--i', i);
    });
    $$('.dg-box, .dg-fill, .dg-node', svg).forEach(function (el, i) { el.style.setProperty('--i', i); });
    $$('.dg-label, .dg-cap', svg).forEach(function (el, i) { el.style.setProperty('--i', i); });
    $$('.dg-ring', svg).forEach(function (el, i) { el.style.setProperty('--i', i); });
    // a light pulse that travels along each refrigerant pipe
    $$('.dg-pipe', svg).forEach(function (pipe, i) {
      var flow = pipe.cloneNode();
      flow.setAttribute('class', 'dg-flow');
      flow.setAttribute('pathLength', '1');
      flow.style.animationDelay = (2 + i * 0.3) + 's';
      svg.appendChild(flow);
    });
  }

  /* ---------- Table of contents (built from the article's H2s) ---------- */
  var slugify = function (t) {
    return t.toLowerCase().replace(/ł/g, 'l').normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '') || 'sekcja';
  };
  var tocNav = $('[data-toc]');
  var headings = $$('.prose h2');
  if (tocNav) {
    if (!headings.length) {
      tocNav.hidden = true;
    } else {
      headings.forEach(function (h, i) {
        if (!h.id) {
          var base = slugify(h.textContent), id = base, n = 2;
          while (document.getElementById(id)) id = base + '-' + n++;
          h.id = id;
        }
        var a = document.createElement('a');
        a.href = '#' + h.id;
        a.innerHTML = '<span>' + (i < 9 ? '0' : '') + (i + 1) + '</span>';
        a.appendChild(document.createTextNode(h.textContent));
        tocNav.appendChild(a);
      });
    }
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
      el.textContent = (target * (1 - Math.pow(1 - k, 3))).toFixed(decimals).replace('.', ',');
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
    if (diagram) io.observe(diagram);
    $$('[data-count]').forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); el.removeAttribute('data-reveal'); });
    if (steps) steps.classList.add('is-in');
    if (diagram) diagram.classList.add('is-in');
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

  /* ---------- Forms ---------- */
  var validPhone = function (v) { return v.replace(/\D/g, '').length >= 9; };

  $$('.lead-form').forEach(function (form) {
    var name = form.querySelector('[name="imie"]');
    var phone = form.querySelector('[name="telefon"]');
    var mail = form.querySelector('[name="email"]');
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
      if (!okName || !okPhone) { (okName ? phone : name).focus(); return; }

      var chip = form.querySelector('.chip.is-active');
      var data = {
        imie: name.value.trim(),
        telefon: phone.value.trim(),
        email: mail ? mail.value.trim() : '',
        rodzaj: chip ? chip.textContent.trim() : '',
        wiadomosc: msg ? msg.value.trim() : '',
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
      'Nazwa / imię: ' + d.imie,
      'Telefon: ' + d.telefon,
      d.email ? 'E-mail: ' + d.email : '',
      d.usluga ? 'Usługa: ' + d.usluga : '',
      d.rodzaj ? 'Czego dotyczy: ' + d.rodzaj : '',
      d.wiadomosc ? '\n' + d.wiadomosc : ''
    ].filter(Boolean).join('\n');
    var subject = 'Zapytanie o wycenę' + (d.usluga ? ' — ' + d.usluga : d.rodzaj ? ' — ' + d.rodzaj : '');
    window.location.href = 'mailto:' + CONTACT_EMAIL
      + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
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
      if (open) { acc.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); }
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
  var lbImg = lightbox ? $('img', lightbox) : null;
  var closeLightbox = function () {
    if (!lightbox || lightbox.hidden) return;
    lightbox.hidden = true;
    document.body.classList.remove('no-scroll');
  };
  $$('.gallery__item').forEach(function (item) {
    item.addEventListener('click', function () {
      lbImg.src = item.getAttribute('data-full');
      lbImg.alt = $('img', item).alt;
      lightbox.hidden = false;
      document.body.classList.add('no-scroll');
      $('.lightbox__close', lightbox).focus();
    });
  });
  if (lightbox) lightbox.addEventListener('click', closeLightbox);

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { closeDrawer(); closeLightbox(); }
  });

  /* ---------- Dock + scroll spy + TOC spy ---------- */
  var dock = $('.dock');
  var mbar = $('.mbar');
  var contact = $('#kontakt');
  // in-page anchors only; sub-pages keep the static nav state from the builder
  var navLinks = $('.nav__link.is-active') ? []
    : $$('.nav__link').filter(function (a) { return a.getAttribute('href').charAt(0) === '#'; });
  var sections = ['oferta', 'klimatyzacja', 'proces', 'realizacje', 'opinie', 'faq', 'kontakt']
    .map(function (id) { return document.getElementById(id); }).filter(Boolean);

  // desktop: the floating card appears once you are past the hero and hides at #kontakt
  var updateDock = function () {
    var show = window.scrollY > 600
      && !(contact && contact.getBoundingClientRect().top < window.innerHeight * 0.9);
    dock.classList.toggle('is-visible', show);
    $$('a', dock).forEach(function (a) { a.tabIndex = show ? 0 : -1; });
    dock.setAttribute('aria-hidden', show ? 'false' : 'true');
  };

  var updateSpy = function () {
    if (!navLinks.length) return;
    var y = window.innerHeight * 0.35, current = null;
    sections.forEach(function (s) { if (s.getBoundingClientRect().top <= y) current = s.id; });
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) current = 'kontakt';
    navLinks.forEach(function (a) { a.classList.toggle('is-active', a.getAttribute('href') === '#' + current); });
  };

  var tocLinks = tocNav ? $$('a', tocNav) : [];
  var tocTargets = tocLinks.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
  var updateToc = function () {
    if (!tocLinks.length) return;
    var y = window.innerHeight * 0.3, current = -1;
    tocTargets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top <= y) current = i; });
    tocLinks.forEach(function (a, i) { a.classList.toggle('is-active', i === current); });
  };

  var ticking = false;
  var onScroll = function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      onScrollHeader(); updateDock(); updateSpy(); updateToc();
      ticking = false;
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();

  setTimeout(function () { mbar.classList.add('is-visible'); }, reduceMotion ? 0 : 900);

  window.matchMedia('(max-width: 1100px)').addEventListener('change', function (e) {
    if (!e.matches) closeDrawer();
  });
})();
