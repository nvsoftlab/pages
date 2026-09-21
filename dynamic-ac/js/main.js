/* Dynamic AC — site interactions
   One file for every page. Everything degrades gracefully without JS:
   the markup is complete, this only adds motion and the form handling. */
(function () {
  'use strict';

  // Lead forms are POSTed as JSON to <body data-form-endpoint="...">
  // (e.g. a Formspree / Web3Forms URL). Without it the visitor's mail client
  // opens with a pre-filled message to CONTACT_EMAIL.
  var CONTACT_EMAIL = 'kontakt@wroclawklima.pl';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (sel, ctx) { return (ctx || document).querySelector(sel); };
  var $$ = function (sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); };
  var on = function (el, ev, fn, opt) { if (el) el.addEventListener(ev, fn, opt); };

  /* ---------- Year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Header shadow ---------- */
  var header = $('.header');
  var onScrollHeader = function () {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
  };

  /* ---------- Services dropdown ---------- */
  // Keep "Usługi" itself as a normal link to the landing-page section. The
  // adjacent toggle exposes direct links to the individual service pages.
  var servicesLink = $('.nav > .nav__link[href$="#uslugi"]');
  if (servicesLink) {
    var servicesRoot = servicesLink.getAttribute('href').slice(0, -'#uslugi'.length);
    var services = [
      ['diagnostyka-i-konserwacja/', 'Diagnostyka i konserwacja'],
      ['serwis-gwarancyjny/', 'Serwis gwarancyjny'],
      ['naprawy-biezace/', 'Naprawy bieżące'],
      ['modernizacja/', 'Modernizacja i retrofitting']
    ];
    var servicesItem = document.createElement('div');
    servicesItem.className = 'nav__item';
    servicesLink.parentNode.insertBefore(servicesItem, servicesLink);
    servicesItem.appendChild(servicesLink);

    var servicesToggle = document.createElement('button');
    servicesToggle.className = 'nav__toggle';
    servicesToggle.type = 'button';
    servicesToggle.setAttribute('aria-label', 'Pokaż strony usług');
    servicesToggle.setAttribute('aria-expanded', 'false');
    servicesToggle.innerHTML = '<svg width="12" height="8" viewBox="0 0 12 8" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="m1 1.5 5 5 5-5"/></svg>';
    servicesItem.appendChild(servicesToggle);

    var servicesMenu = document.createElement('div');
    servicesMenu.className = 'nav__dropdown';
    services.forEach(function (service) {
      var link = document.createElement('a');
      link.href = servicesRoot + service[0];
      link.textContent = service[1];
      if (window.location.pathname.indexOf('/' + service[0]) !== -1) link.classList.add('is-active');
      servicesMenu.appendChild(link);
    });
    servicesItem.appendChild(servicesMenu);

    var closeServices = function () {
      servicesItem.classList.remove('is-open');
      servicesToggle.setAttribute('aria-expanded', 'false');
    };
    on(servicesToggle, 'click', function (event) {
      event.stopPropagation();
      var open = servicesItem.classList.toggle('is-open');
      servicesToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    on(document, 'click', closeServices);
    on(document, 'keydown', function (event) { if (event.key === 'Escape') closeServices(); });
  }

  /* ---------- Circuit infographic ---------- */
  var circuit = $('.circuit');
  if (circuit) {
    var svg = $('.circuit__lines', circuit);
    // Halos sit under the coloured strokes so the lines stay readable over the
    // photo; they are drawn first and share the same dash animation.
    $$('.cir-halo, .cir-hi, .cir-lo', svg).forEach(function (path, i) {
      path.setAttribute('pathLength', '1');
      path.style.setProperty('--i', i);
    });
    // a travelling highlight cloned from each coloured pipe
    $$('.cir-hi, .cir-lo', svg).forEach(function (path, i) {
      var hot = path.classList.contains('cir-hi');
      var flow = path.cloneNode();
      flow.setAttribute('class', 'cir-flow ' + (hot ? 'cir-flow--hi' : 'cir-flow--lo cir-flow--rev'));
      flow.style.animationDelay = (1.8 + i * 0.3) + 's';
      svg.appendChild(flow);
    });
    $$('.cir-pin', circuit).forEach(function (p, i) { p.style.setProperty('--i', i); });
  }

  /* ---------- Scroll reveal ---------- */
  var revealEls = $$('[data-reveal]');
  var groups = new Map();
  revealEls.forEach(function (el) {
    var p = el.parentElement;
    var n = groups.get(p) || 0;
    el.style.setProperty('--d', (Math.min(n, 6) * 0.08) + 's');
    groups.set(p, n + 1);
  });

  /* ---------- Step / symptom cycling ---------- */
  // The design highlights one card at a time. Drive it from JS so the
  // rotation only runs while the section is actually on screen.
  var makeCycle = function (items, period) {
    var timer = null, at = 0;
    var show = function () {
      items.forEach(function (el, i) { el.classList.toggle('is-live', i === at); });
      at = (at + 1) % items.length;
    };
    return {
      start: function () { if (timer || !items.length || reduceMotion) return; show(); timer = setInterval(show, period); },
      stop: function () {
        if (!timer) return;
        clearInterval(timer); timer = null;
        items.forEach(function (el) { el.classList.remove('is-live'); });
      }
    };
  };
  var stepsBox = $('.steps');
  var stepCycle = stepsBox ? makeCycle($$('.step', stepsBox), 2250) : null;
  var symCycle = $('.sym-grid') ? makeCycle($$('.sym'), 2200) : null;
  $$('.step__icon svg *').forEach(function (shape) { shape.setAttribute('pathLength', '1'); });
  $$('.step', stepsBox || document).forEach(function (s, i) { s.style.setProperty('--i', i); });

  /* ---------- Editor content: heading ids + table of contents ---------- */
  var slugify = function (t) {
    return t.toLowerCase()
      .replace(/ł/g, 'l').replace(/ą/g, 'a').replace(/ę/g, 'e').replace(/ś/g, 's')
      .replace(/ć/g, 'c').replace(/ź/g, 'z').replace(/ż/g, 'z').replace(/ń/g, 'n').replace(/ó/g, 'o')
      .normalize('NFD').replace(/[̀-ͯ]/g, '')
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
  var tocNav = $('[data-toc]');
  if (tocNav) {
    if (!headings.length) {
      var tocBox = tocNav.closest('.toc');
      if (tocBox) tocBox.hidden = true;
    }
    headings.forEach(function (h, i) {
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.innerHTML = '<span>' + (i < 9 ? '0' : '') + (i + 1) + '</span>';
      a.appendChild(document.createTextNode(h.textContent));
      tocNav.appendChild(a);
    });
  }

  /* ---------- IntersectionObserver wiring ---------- */
  var liveOn = function (cycle) {
    return function (entries) {
      entries.forEach(function (e) { e.isIntersecting ? cycle.start() : cycle.stop(); });
    };
  };

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        io.unobserve(e.target);
        e.target.classList.add('is-in');
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.01 });

    revealEls.forEach(function (el) { io.observe(el); });
    entryEls.forEach(function (el) { io.observe(el); });
    if (circuit) io.observe(circuit);
    if (stepsBox) io.observe(stepsBox);
    var track = $('.track');
    if (track) io.observe(track);

    if (stepCycle) new IntersectionObserver(liveOn(stepCycle), { threshold: 0.2 }).observe(stepsBox);
    if (symCycle) new IntersectionObserver(liveOn(symCycle), { threshold: 0.15 }).observe($('.sym-grid'));
  } else {
    revealEls.concat(entryEls).forEach(function (el) { el.classList.add('is-in'); });
    ['.circuit', '.steps', '.track'].forEach(function (s) { var el = $(s); if (el) el.classList.add('is-in'); });
  }

  /* ---------- FAQ accordion ---------- */
  var accs = $$('.acc');
  accs.forEach(function (acc) {
    var btn = $('.acc__btn', acc);
    var panel = $('.acc__panel', acc);
    if (!btn || !panel) return;
    // start from whatever the markup declared (first item open)
    panel.style.height = acc.classList.contains('is-open') ? 'auto' : '0px';

    var setOpen = function (open) {
      acc.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      panel.style.height = panel.scrollHeight + 'px';
      if (!open) {
        requestAnimationFrame(function () { panel.style.height = '0px'; });
      } else {
        var done = function () { panel.style.height = 'auto'; panel.removeEventListener('transitionend', done); };
        panel.addEventListener('transitionend', done);
      }
    };

    on(btn, 'click', function () {
      var willOpen = !acc.classList.contains('is-open');
      accs.forEach(function (other) {
        if (other === acc || !other.classList.contains('is-open')) return;
        var op = $('.acc__panel', other);
        op.style.height = op.scrollHeight + 'px';
        other.classList.remove('is-open');
        $('.acc__btn', other).setAttribute('aria-expanded', 'false');
        requestAnimationFrame(function () { op.style.height = '0px'; });
      });
      setOpen(willOpen);
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
    setTimeout(function () { $('.drawer__close', drawer).focus(); }, 60);
  };
  var closeDrawer = function () {
    if (!drawer || !drawer.classList.contains('is-open')) return;
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    burger.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('no-scroll');
    if (lastFocus) lastFocus.focus({ preventScroll: true });
  };
  if (drawer && burger) {
    on(burger, 'click', openDrawer);
    $$('[data-close]', drawer).forEach(function (el) { on(el, 'click', closeDrawer); });
  }

  /* ---------- Lightbox ---------- */
  var lightbox = $('.lightbox');
  var closeLightbox = function () {
    if (!lightbox || lightbox.hidden) return;
    lightbox.hidden = true;
    document.body.classList.remove('no-scroll');
  };
  if (lightbox) {
    var lbImg = $('img', lightbox);
    $$('.gallery__item').forEach(function (item) {
      on(item, 'click', function () {
        lbImg.src = item.getAttribute('data-full') || $('img', item).src;
        lbImg.alt = $('img', item).alt || '';
        lightbox.hidden = false;
        document.body.classList.add('no-scroll');
        $('.lightbox__close', lightbox).focus();
      });
    });
    on(lightbox, 'click', closeLightbox);
  }

  on(document, 'keydown', function (e) {
    if (e.key === 'Escape') { closeDrawer(); closeLightbox(); }
  });

  /* ---------- Forms ---------- */
  var validPhone = function (v) { return v.replace(/\D/g, '').length >= 9; };

  $$('.lead-form').forEach(function (form) {
    var name = form.querySelector('[name="imie"]');
    var phone = form.querySelector('[name="telefon"]');
    var car = form.querySelector('[name="auto"]');
    var msg = form.querySelector('[name="wiadomosc"]');

    var check = function (input, ok) {
      input.closest('.field').classList.toggle('is-invalid', !ok);
      input.setAttribute('aria-invalid', ok ? 'false' : 'true');
      return ok;
    };
    [name, phone].forEach(function (input) {
      on(input, 'input', function () {
        if (input.closest('.field').classList.contains('is-invalid')) {
          check(input, input === phone ? validPhone(input.value) : input.value.trim().length > 0);
        }
      });
    });

    on(form, 'submit', function (e) {
      e.preventDefault();
      var okName = check(name, name.value.trim().length > 0);
      var okPhone = check(phone, validPhone(phone.value));
      if (!okName || !okPhone) { (okName ? phone : name).focus(); return; }

      var data = {
        imie: name.value.trim(),
        telefon: phone.value.trim(),
        auto: car ? car.value.trim() : '',
        wiadomosc: msg ? msg.value.trim() : '',
        zrodlo: form.getAttribute('data-form') || '',
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
      d.auto ? 'Model auta: ' + d.auto : '',
      d.usluga ? 'Usługa: ' + d.usluga : '',
      d.wiadomosc ? '\n' + d.wiadomosc : ''
    ].filter(Boolean).join('\n');
    var subject = 'Zapytanie o serwis klimatyzacji' + (d.usluga ? ' — ' + d.usluga : '');
    window.location.href = 'mailto:' + CONTACT_EMAIL
      + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
  }

  /* ---------- Copy link (articles) ---------- */
  $$('[data-share]').forEach(function (btn) {
    on(btn, 'click', function () {
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

  /* ---------- Dock, mobile bar, scroll spy, TOC spy ---------- */
  var dock = $('.dock');
  var mbar = $('.mbar');
  var contact = $('#kontakt');
  // Sub-pages mark their own nav item; only in-page anchors take part in the spy.
  var navLinks = $('.nav__link.is-active')
    ? []
    : $$('.nav__link, .drawer__nav a').filter(function (a) { return a.getAttribute('href').charAt(0) === '#'; });
  // Only sections the menu actually links to take part: a section without a nav
  // item (#diagnostyka, #objawy, #o-nas) would otherwise clear every highlight
  // as soon as it scrolled past.
  var sections = [];
  var seen = {};
  navLinks.forEach(function (a) {
    var id = a.getAttribute('href').slice(1);
    var el = id && !seen[id] && document.getElementById(id);
    if (el) { seen[id] = true; sections.push(el); }
  });

  var updateDock = function () {
    if (!dock) return;
    var past = window.scrollY > 700;
    var nearContact = contact ? contact.getBoundingClientRect().top < window.innerHeight * 0.9 : false;
    var show = past && !nearContact;
    dock.classList.toggle('is-visible', show);
    $$('a', dock).forEach(function (a) { a.tabIndex = show ? 0 : -1; });
    dock.setAttribute('aria-hidden', show ? 'false' : 'true');
  };

  var updateSpy = function () {
    if (!navLinks.length) return;
    var y = window.innerHeight * 0.35;
    var current = null;
    sections.forEach(function (s) { if (s.getBoundingClientRect().top <= y) current = s.id; });
    if (window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) current = 'kontakt';
    navLinks.forEach(function (a) { a.classList.toggle('is-active', a.getAttribute('href') === '#' + current); });
  };

  var tocLinks = $$('.toc a');
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
  on(window, 'scroll', onScroll, { passive: true });
  on(window, 'resize', onScroll, { passive: true });
  onScroll();

  if (mbar) setTimeout(function () { mbar.classList.add('is-visible'); }, reduceMotion ? 0 : 900);

  var wide = window.matchMedia('(min-width: 1101px)');
  var onWide = function (e) { if (e.matches) closeDrawer(); };
  if (wide.addEventListener) wide.addEventListener('change', onWide);
  else wide.addListener(onWide);
})();
