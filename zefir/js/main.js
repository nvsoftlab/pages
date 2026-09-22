/* ZEFIR Klimatyzacja — landing page interactions
   Shares the Klimat OK interaction model: hero intro, scroll reveal, stepped
   process timeline, chips, validated lead form, drawer, dock + mobile bar. */
(function () {
  'use strict';

  // Lead forms are POSTed as JSON to <body data-form-endpoint="...">
  // (e.g. a Formspree / Web3Forms URL). Without it, the visitor's mail
  // client opens with a pre-filled message to CONTACT_EMAIL.
  var CONTACT_EMAIL = 'biuro@zefir-klimatyzacja.pl';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
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
  if (steps) $$('.step', steps).forEach(function (s, i) { s.style.setProperty('--i', i); });
  $$('.step__icon *').forEach(function (shape) { shape.setAttribute('pathLength', '1'); });

  /* ---------- Service checklist ---------- */
  var checklist = $('.checklist');
  if (checklist) $$('li', checklist).forEach(function (li, i) { li.style.setProperty('--i', i); });

  if ('IntersectionObserver' in window && !reduceMotion) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        io.unobserve(el);
        el.classList.add('is-in');
        if (el.hasAttribute('data-reveal')) finishReveal(el);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });

    revealEls.forEach(function (el) { io.observe(el); });
    if (steps) io.observe(steps);
    if (checklist) io.observe(checklist);
    io.observe($('.footer__bottom'));
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); el.removeAttribute('data-reveal'); });
    if (steps) steps.classList.add('is-in');
    if (checklist) checklist.classList.add('is-in');
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

  /* ---------- Forms ---------- */
  var validPhone = function (v) { return v.replace(/\D/g, '').length >= 9; };
  var validMail = function (v) { return !v.trim() || /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); };

  $$('.lead-form').forEach(function (form) {
    var name = form.querySelector('[name="imie"]');
    var phone = form.querySelector('[name="telefon"]');
    var mail = form.querySelector('[name="email"]');
    var obiekt = form.querySelector('[name="obiekt"]');
    var msg = form.querySelector('[name="wiadomosc"]');

    var check = function (input, ok) {
      input.closest('.field').classList.toggle('is-invalid', !ok);
      input.setAttribute('aria-invalid', ok ? 'false' : 'true');
      return ok;
    };
    var testOf = function (input) {
      if (input === phone) return validPhone(input.value);
      if (input === mail) return validMail(input.value);
      return input.value.trim().length > 0;
    };
    [name, phone, mail].filter(Boolean).forEach(function (input) {
      input.addEventListener('input', function () {
        if (input.closest('.field').classList.contains('is-invalid')) check(input, testOf(input));
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var checks = [name, phone, mail].filter(Boolean).map(function (input) { return check(input, testOf(input)); });
      var firstBad = [name, phone, mail].filter(Boolean)[checks.indexOf(false)];
      if (firstBad) { firstBad.focus(); return; }

      var chip = form.querySelector('.chip.is-active');
      var kind = chip && chip.offsetParent !== null ? chip.textContent.trim() : (obiekt ? obiekt.value : '');
      var data = {
        imie: name.value.trim(),
        telefon: phone.value.trim(),
        email: mail ? mail.value.trim() : '',
        obiekt: kind,
        wiadomosc: msg ? msg.value.trim() : '',
        zrodlo: form.getAttribute('data-form')
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
      d.email ? 'E-mail: ' + d.email : '',
      d.obiekt ? 'Typ obiektu: ' + d.obiekt : '',
      d.wiadomosc ? '\n' + d.wiadomosc : ''
    ].filter(Boolean).join('\n');
    var subject = 'Zapytanie o wycenę' + (d.obiekt ? ' — ' + d.obiekt : '');
    window.location.href = 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  }

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
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeDrawer(); });

  /* ---------- Dock (desktop) + scroll spy ---------- */
  var dock = $('.dock');
  var mbar = $('.mbar');
  var contact = $('#kontakt');
  var navLinks = $$('.nav__link, .drawer__nav a').filter(function (a) { return a.getAttribute('href').charAt(0) === '#'; });
  var sections = ['oferta', 'miejsce', 'montaz', 'wycena', 'serwis', 'o-nas', 'kontakt']
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

  var ticking = false;
  var onScroll = function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      onScrollHeader();
      updateDock();
      updateSpy();
      ticking = false;
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();

  setTimeout(function () { mbar.classList.add('is-visible'); }, reduceMotion ? 0 : 900);

  window.matchMedia('(max-width: 1100px)').addEventListener('change', function (e) { if (!e.matches) closeDrawer(); });
})();
