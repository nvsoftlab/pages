# Перенос GETMON на WordPress

Демо — статичний HTML. `css/styles.css` і `js/main.js` переносяться в тему без змін
(`wp_enqueue_style` / `wp_enqueue_script`), шляхи до картинок → `get_template_directory_uri()`.

## Шаблони

| Демо | Тема WordPress |
|---|---|
| топбар, `.header` з випадайками | `header.php`, меню через `wp_nav_menu()` (пункти з класом `nav__link`, підменю → `.nav__menu`) |
| `.footer`, `.dock`, `.drawer`, `.lightbox`, `.band`, `#kontakt` | `footer.php` |
| `index.html` | `front-page.php` |
| `<slug>/index.html` (16 сторінок послуг) | `page-usluga.php` + ACF: hero (заголовок, лід, 3 «тіки», фон), блоки тексту, «Powiązane usługi» |
| `blog/index.html` | `home.php` — цикл постів, перший → `.post-feature`, решта → `.post-card` |
| `blog/<slug>/index.html` | `single.php` |
| `polityka-prywatnosci/index.html` | звичайна сторінка + `page.php` |

## Контент з редактора

Текст статті й опис послуги виводяться як є:

```php
<div class="prose entry-content"><?php the_content(); ?></div>
```

Стилі `.prose` розраховані на звичайні блоки Gutenberg, класи не потрібні:

- **Paragraph / Heading (H2, H3) / List / Image**: лінію під H2 і галочки в списках малює CSS.
- **Group** з додатковим CSS-класом `callout`: блок з бірюзовою лінією; перший абзац стає підписом.
- Зміст (`<nav class="toc" data-toc>`) і `id` заголовків генерує `main.js` з H2 — руками нічого не треба.

## Форми

Одна розмітка на всі форми — та сама `.lead-form` у герої та в `#kontakt`
(різниця лише в полях e-mail/повідомлення). Варіанти:

1. **Contact Form 7 / WPForms** — замінити `<form class="lead-form">` шорткодом,
   лишивши класи `.field`, `.chips`, `.btn--submit` на полях.
2. **Лишити нашу розмітку** — передати URL обробника в `<body data-form-endpoint="...">`
   (напр. `admin-ajax.php?action=getmon_lead`). `main.js` шле JSON:
   `{imie, telefon, email, rodzaj, wiadomosc, zrodlo, usluga}`.
   Без `data-form-endpoint` відкривається поштовий клієнт на `biuro@getmon.pl`.

`zrodlo` = `hero` / `kontakt`, `usluga` = назва послуги зі сторінки — зручно для аналітики.

## Картинки

`assets/img/bg/*.jpg` — фони секцій. У демо це безкоштовні стокові фото (Pexels),
бо CDN `admin.getmon.pl` під час збірки блокував завантаження (adm.tools, HTTP 429).

Щоб підставити **справжні фото GETMON**:

```bash
python3 getmon/_build/fetch_images.py            # завантажити оригінали
python3 getmon/_build/fetch_images.py --restore  # повернути сток
```

Скрипт кладе файли під тими самими іменами, тож HTML міняти не треба.
Мапінг «ім'я фону → оригінал на getmon.pl» — у `MAP` всередині скрипта.

## URL-и

Слаги **збігаються з чинним getmon.pl**, тож жодне проіндексоване посилання не
зламається. 301-редіректи не потрібні. Сторінки, яких на getmon.pl зараз немає
(є тільки биті посилання в меню — анкети, RTV/SAT, smart home), у демо теж немає.

## Анімації

- `.step__icon` і схема `[data-diagram]` — SVG-лінії малюються через
  `pathLength="1"` + `stroke-dashoffset` (значення ставить `main.js`).
- Імпульси на трасі (`.dg-flow`) — клони ліній з `stroke-dasharray`.
- Усе вимикається через `prefers-reduced-motion`.

## Інше

- `_build/build_pages.py` генерує всі підсторінки й **синхронізує шапку/підвал
  в `index.html`** через маркери `<!--#HEADER-->…<!--/#HEADER-->`.
  Після переносу в тему скрипт більше не потрібен — але поки демо живе, правити
  контент треба в `_build/content_*.py`, а не в згенерованому HTML.
- Schema.org (`HVACBusiness`, `Service`, `BlogPosting`) вже в `<head>` кожної сторінки.
