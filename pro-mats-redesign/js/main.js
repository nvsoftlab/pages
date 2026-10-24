(() => {
  'use strict';

  const doc = document;
  const root = doc.documentElement;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const compactViewport = window.matchMedia('(max-width: 720px)');
  const navigationViewport = window.matchMedia('(max-width: 1020px)');
  const richMotion = window.matchMedia('(min-width: 721px) and (pointer: fine)');
  const header = doc.querySelector('.header');
  const nav = doc.querySelector('.nav');
  const menuButton = doc.querySelector('.menu-button');
  const progress = doc.querySelector('.page-progress span');
  const year = doc.querySelector('#year');
  const mobileCta = doc.querySelector('.mobile-cta');
  const orderSection = doc.querySelector('#order');
  const heroSection = doc.querySelector('.hero');
  const footer = doc.querySelector('.footer');

  if (year) year.textContent = String(new Date().getFullYear());

  const closeMenu = () => {
    if (!nav || !menuButton) return;
    nav.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'Відкрити меню');
    doc.body.classList.remove('menu-open');
    root.classList.remove('menu-open');
    if (navigationViewport.matches) {
      if (nav.contains(doc.activeElement)) menuButton.focus({ preventScroll: true });
      nav.setAttribute('inert', '');
    }
  };

  const syncMobileNavigation = () => {
    if (!nav) return;
    if (navigationViewport.matches && !nav.classList.contains('is-open')) nav.setAttribute('inert', '');
    else nav.removeAttribute('inert');
  };

  syncMobileNavigation();
  navigationViewport.addEventListener?.('change', syncMobileNavigation);

  menuButton?.addEventListener('click', () => {
    const shouldOpen = menuButton.getAttribute('aria-expanded') !== 'true';
    nav?.classList.toggle('is-open', shouldOpen);
    menuButton.setAttribute('aria-expanded', String(shouldOpen));
    menuButton.setAttribute('aria-label', shouldOpen ? 'Закрити меню' : 'Відкрити меню');
    doc.body.classList.toggle('menu-open', shouldOpen);
    root.classList.toggle('menu-open', shouldOpen);
    nav?.toggleAttribute('inert', !shouldOpen && navigationViewport.matches);
    if (shouldOpen) nav?.querySelector('a')?.focus({ preventScroll: true });
  });

  nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
  window.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') closeMenu();
  });

  navigationViewport.addEventListener?.('change', () => {
    closeMenu();
  });

  const revealItems = [...doc.querySelectorAll('.reveal')];
  revealItems.forEach((item) => {
    const delayIndex = Number(item.dataset.delay || 0);
    item.style.setProperty('--delay', `${Math.min(delayIndex * 0.12, 0.48)}s`);
  });

  if (compactViewport.matches || reduceMotion || !('IntersectionObserver' in window)) {
    revealItems.forEach((item) => item.classList.add('visible'));
  } else {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    revealItems.forEach((item) => revealObserver.observe(item));
  }

  const navLinks = [...doc.querySelectorAll('.nav > a[href^="#"]')];
  const sectionMap = navLinks
    .map((link) => ({ link, section: doc.querySelector(link.getAttribute('href')) }))
    .filter((item) => item.section);

  if ('IntersectionObserver' in window && sectionMap.length) {
    const activeObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        navLinks.forEach((link) => link.classList.remove('is-active'));
        sectionMap.find((item) => item.section === entry.target)?.link.classList.add('is-active');
      });
    }, { rootMargin: '-24% 0px -68% 0px', threshold: 0 });
    sectionMap.forEach((item) => activeObserver.observe(item.section));
  }

  const parallaxItems = [...doc.querySelectorAll('[data-parallax]')];
  let ticking = false;

  const updateScrollEffects = () => {
    const scrollTop = window.scrollY || root.scrollTop;
    const scrollRange = Math.max(1, root.scrollHeight - window.innerHeight);
    const scrollRatio = Math.min(1, Math.max(0, scrollTop / scrollRange));

    progress?.style.setProperty('transform', `scaleX(${scrollRatio})`);
    header?.classList.toggle('is-scrolled', scrollTop > 18);

    if (!reduceMotion && richMotion.matches) {
      const viewportCenter = window.innerHeight / 2;
      parallaxItems.forEach((item) => {
        const rect = item.getBoundingClientRect();
        if (rect.bottom < -200 || rect.top > window.innerHeight + 200) return;
        const speed = Number(item.dataset.parallax || 0);
        const itemCenter = rect.top + rect.height / 2;
        const shift = (itemCenter - viewportCenter) * speed;
        item.style.setProperty('--parallax', `${shift.toFixed(2)}px`);
      });
    }

    if (mobileCta) {
      const heroBottom = heroSection ? heroSection.getBoundingClientRect().bottom : 0;
      const pastHero = heroBottom < -24;
      const nearEnd = (orderSection && orderSection.getBoundingClientRect().top < window.innerHeight * 0.92)
        || (footer && footer.getBoundingClientRect().top < window.innerHeight * 0.98);
      mobileCta.classList.toggle('is-hidden', !compactViewport.matches || nearEnd || !pastHero);
    }
    ticking = false;
  };

  const requestScrollUpdate = () => {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(updateScrollEffects);
  };

  window.addEventListener('scroll', requestScrollUpdate, { passive: true });
  window.addEventListener('resize', requestScrollUpdate, { passive: true });
  updateScrollEffects();

  const countItems = [...doc.querySelectorAll('[data-count]')];
  const setFinalCount = (item) => {
    const value = Number(item.dataset.count || 0);
    item.textContent = `${value.toLocaleString('uk-UA')}${item.dataset.suffix || ''}`;
  };

  if (compactViewport.matches || reduceMotion || !('IntersectionObserver' in window)) {
    countItems.forEach(setFinalCount);
  } else {
    const countObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const item = entry.target;
        const target = Number(item.dataset.count || 0);
        const suffix = item.dataset.suffix || '';
        const duration = target > 100 ? 1500 : 1000;
        const startedAt = performance.now();

        const animateCount = (now) => {
          const progressValue = Math.min(1, (now - startedAt) / duration);
          const eased = 1 - Math.pow(1 - progressValue, 4);
          const current = Math.round(target * eased);
          item.textContent = `${current.toLocaleString('uk-UA')}${suffix}`;
          if (progressValue < 1) window.requestAnimationFrame(animateCount);
        };

        window.requestAnimationFrame(animateCount);
        observer.unobserve(item);
      });
    }, { threshold: 0.7 });
    countItems.forEach((item) => countObserver.observe(item));
  }

  if (!reduceMotion && window.matchMedia('(pointer:fine)').matches) {
    doc.querySelectorAll('[data-tilt]').forEach((card) => {
      card.addEventListener('pointermove', (event) => {
        const rect = card.getBoundingClientRect();
        const x = (event.clientX - rect.left) / rect.width;
        const y = (event.clientY - rect.top) / rect.height;
        const rotateY = (x - 0.5) * 7;
        const rotateX = (0.5 - y) * 7;
        card.style.setProperty('--rx', `${rotateX.toFixed(2)}deg`);
        card.style.setProperty('--ry', `${rotateY.toFixed(2)}deg`);
        card.style.setProperty('--mx', `${(x * 100).toFixed(1)}%`);
        card.style.setProperty('--my', `${(y * 100).toFixed(1)}%`);
      });

      card.addEventListener('pointerleave', () => {
        card.style.setProperty('--rx', '0deg');
        card.style.setProperty('--ry', '0deg');
        card.style.setProperty('--mx', '50%');
        card.style.setProperty('--my', '50%');
      });
    });
  }

  const previewMatrix = {
    black: {
      gray: 'design-double-black.webp',
      red: 'design-double-black-red.webp',
      blue: 'design-double-black-blue.webp',
      gold: 'design-double-black-gold.webp'
    },
    cognac: {
      gray: 'design-double-cognac.webp',
      red: 'design-double-cognac-red.webp',
      blue: 'design-double-cognac-blue.webp',
      gold: 'design-double-cognac-gold.webp'
    },
    burgundy: {
      gray: 'design-double-burgundy.webp',
      red: 'design-double-burgundy-red.webp',
      blue: 'design-double-burgundy-blue.webp',
      gold: 'design-double-burgundy-gold.webp'
    },
    beige: {
      gray: 'design-double-beige.webp',
      red: 'design-double-beige-red.webp',
      blue: 'design-double-beige-blue.webp',
      gold: 'design-double-beige-gold.webp'
    }
  };

  const preview = doc.querySelector('#custom-preview');
  const selection = doc.querySelector('#custom-selection');
  const baseLabel = doc.querySelector('#base-label');
  const threadLabel = doc.querySelector('#thread-label');
  const baseInput = doc.querySelector('#base-color-input');
  const threadInput = doc.querySelector('#thread-color-input');
  const colorState = { base: 'black', thread: 'gray', baseLabel: 'Чорний', threadLabel: 'Світло-сірий' };
  let previewRequest = 0;

  const setPreview = () => {
    if (!preview) return;
    const filename = previewMatrix[colorState.base]?.[colorState.thread];
    if (!filename) return;

    const nextSrc = `assets/img/${filename}`;
    const nextAlt = `${colorState.baseLabel} комплект килимків Pro Mats; колір нитки — ${colorState.threadLabel.toLowerCase()}`;
    const requestId = ++previewRequest;
    preview.classList.add('is-changing');

    const incoming = new Image();
    incoming.onload = () => {
      if (requestId !== previewRequest) return;
      window.setTimeout(() => {
        preview.src = nextSrc;
        preview.alt = nextAlt;
        preview.classList.remove('is-changing');
      }, (compactViewport.matches || reduceMotion) ? 0 : 110);
    };
    incoming.onerror = () => {
      if (requestId === previewRequest) preview.classList.remove('is-changing');
    };
    incoming.src = nextSrc;

    const selectionText = `${colorState.baseLabel} · нитка: ${colorState.threadLabel.toLowerCase()}`;
    if (selection) selection.textContent = selectionText;
    if (baseLabel) baseLabel.textContent = colorState.baseLabel;
    if (threadLabel) threadLabel.textContent = colorState.threadLabel;
    if (baseInput) baseInput.value = colorState.baseLabel;
    if (threadInput) threadInput.value = colorState.threadLabel;
  };

  doc.querySelectorAll('[data-choice]').forEach((group) => {
    const type = group.dataset.choice;
    group.querySelectorAll('.swatch').forEach((button) => {
      button.addEventListener('click', () => {
        group.querySelectorAll('.swatch').forEach((item) => {
          const active = item === button;
          item.classList.toggle('is-active', active);
          item.setAttribute('aria-pressed', String(active));
        });

        const key = button.dataset.color;
        const label = button.dataset.label;
        if (type === 'base') {
          colorState.base = key;
          colorState.baseLabel = label;
        } else {
          colorState.thread = key;
          colorState.threadLabel = label;
        }
        setPreview();
      });
    });
  });

  const designSelect = doc.querySelector('#design-select');
  doc.querySelectorAll('.collection-card[data-design] a[href="#order"]').forEach((link) => {
    link.addEventListener('click', () => {
      const design = link.closest('[data-design]')?.dataset.design;
      if (!designSelect || !design) return;
      const matchingOption = [...designSelect.options].find((option) => option.value === design);
      if (matchingOption) designSelect.value = design;
    });
  });

  doc.querySelectorAll('.accordion details').forEach((detail) => {
    detail.addEventListener('toggle', () => {
      if (!detail.open) return;
      doc.querySelectorAll('.accordion details').forEach((sibling) => {
        if (sibling !== detail) sibling.open = false;
      });
    });
  });

  const privacyDialog = doc.querySelector('#privacy-dialog');
  const privacyClose = privacyDialog?.querySelector('[data-privacy-close]');
  let privacyTrigger = null;

  const closePrivacy = () => {
    if (!privacyDialog?.open) return;
    privacyDialog.close();
  };

  doc.querySelectorAll('[data-privacy-open]').forEach((trigger) => {
    trigger.addEventListener('click', () => {
      if (!privacyDialog) return;
      privacyTrigger = trigger;
      doc.body.classList.add('dialog-open');
      root.classList.add('dialog-open');
      privacyDialog.showModal();
      privacyClose?.focus({ preventScroll: true });
    });
  });

  privacyClose?.addEventListener('click', closePrivacy);
  privacyDialog?.addEventListener('click', (event) => {
    if (event.target === privacyDialog) closePrivacy();
  });
  privacyDialog?.addEventListener('close', () => {
    doc.body.classList.remove('dialog-open');
    root.classList.remove('dialog-open');
    privacyTrigger?.focus({ preventScroll: true });
    privacyTrigger = null;
  });

  const form = doc.querySelector('#lead-form');
  const formStatus = form?.querySelector('.form-status');

  form?.querySelectorAll('input[required]').forEach((input) => {
    input.addEventListener('input', () => {
      input.classList.remove('is-invalid');
      input.removeAttribute('aria-invalid');
    });
  });

  form?.addEventListener('submit', (event) => {
    event.preventDefault();
    const required = [...form.querySelectorAll('input[required]')];
    const invalid = required.filter((input) => !input.value.trim());
    required.forEach((input) => {
      const isInvalid = invalid.includes(input);
      input.classList.toggle('is-invalid', isInvalid);
      input.setAttribute('aria-invalid', String(isInvalid));
    });

    if (invalid.length) {
      if (formStatus) formStatus.textContent = 'Заповніть, будь ласка, ім’я, телефон та дані авто.';
      invalid[0].focus();
      return;
    }

    const submitButton = form.querySelector('button[type="submit"]');
    if (submitButton) {
      submitButton.disabled = true;
      submitButton.firstChild.textContent = 'Дякуємо — заявку збережено ';
    }
    if (formStatus) {
      formStatus.textContent = 'Це демо: дані не надсилались. Після підключення CRM тут буде підтвердження заявки.';
    }
  });

  // Mobile carousels: manual swipe + dot indicators
  const carouselEls = [
    ...doc.querySelectorAll('.collection-grid, .works__grid')
  ];

  const initCarousel = (carousel) => {
    if (!carousel || carousel.dataset.carousel) return;
    const items = [...carousel.children].filter((child) => child.nodeType === 1);
    if (items.length < 2) return;
    carousel.dataset.carousel = '1';

    const dots = doc.createElement('div');
    dots.className = 'carousel-dots';
    dots.setAttribute('role', 'group');
    dots.setAttribute('aria-label', 'Навігація по слайдах');
    items.forEach((_, i) => {
      const dot = doc.createElement('button');
      dot.type = 'button';
      dot.className = i === 0 ? 'carousel-dot is-active' : 'carousel-dot';
      dot.setAttribute('aria-label', `Слайд ${i + 1} з ${items.length}`);
      dot.addEventListener('click', () => goTo(i));
      dots.appendChild(dot);
    });
    carousel.after(dots);

    let index = 0;
    let rafId = null;

    const goTo = (i) => {
      const item = items[i];
      if (!item) return;
      const cRect = carousel.getBoundingClientRect();
      const iRect = item.getBoundingClientRect();
      const target = carousel.scrollLeft + (iRect.left - cRect.left) - (carousel.clientWidth - item.clientWidth) / 2;
      carousel.scrollTo({ left: Math.max(0, target), behavior: 'smooth' });
    };

    const updateDots = () => {
      const cRect = carousel.getBoundingClientRect();
      const center = cRect.left + cRect.width / 2;
      let best = 0;
      let bestDist = Infinity;
      items.forEach((item, i) => {
        const r = item.getBoundingClientRect();
        const d = Math.abs(r.left + r.width / 2 - center);
        if (d < bestDist) {
          bestDist = d;
          best = i;
        }
      });
      if (best === index) return;
      index = best;
      dots.querySelectorAll('.carousel-dot').forEach((dot, i) => dot.classList.toggle('is-active', i === index));
    };

    carousel.addEventListener('scroll', () => {
      if (rafId) return;
      rafId = window.requestAnimationFrame(() => {
        updateDots();
        rafId = null;
      });
    }, { passive: true });

  };

  const setupCarousels = () => {
    if (compactViewport.matches) carouselEls.forEach(initCarousel);
  };

  setupCarousels();
  compactViewport.addEventListener?.('change', setupCarousels);
})();
