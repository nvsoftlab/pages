# Перенос на WordPress

Демо — статичний HTML. `css/styles.css` і `js/main.js` переносяться в тему без змін
(`wp_enqueue_style` / `wp_enqueue_script`), шляхи до картинок → `get_template_directory_uri()`.

## Шаблони

| Демо | Тема WordPress |
|---|---|
| `.topbar`, `.header`, меню | `header.php`, меню через `wp_nav_menu()` (пункти з класом `nav__link`) |
| `.footer`, `.dock`, `.mbar`, `.drawer`, `.lightbox`, `#kontakt` | `footer.php` |
| `index.html` | `front-page.php` |
| `<послуга>/index.html` | `page-usluga.php` (шаблон сторінки) + ACF |
| `kontakt/index.html` | `page-kontakt.php` |
| `blog/index.html` | `home.php` — цикл постів, перший → `.post-feature`, решта → `.post-card` |
| `blog/<пост>/index.html` | `single.php` |

## ACF для сторінки послуги

| Поле | Куди йде |
|---|---|
| `pill` (text) | ейбров над H1 |
| `lead` (textarea) | `.phero__lead` |
| `hero_img` (image) | `.phero__bg` |
| `highlights` (repeater ×4: icon, title, text) | `.hl-grid` |
| `steps_title`, `steps_lead`, `steps` (repeater ×5) | блок `.steps` |
| `gallery` (gallery ×3) | `.gallery` + `data-full` на повний розмір |
| `cta` (text) | напис «Umów …» у сайдбарі (знахідний відмінок) |

Іконки — inline SVG зі словника `ICONS` в `_build/content_services.py`; у темі
зручно тримати їх як `get_template_part('icon', $name)`.

## Контент з редактора

Текст послуги й статті виводиться як є:

```php
<div class="entry-content"><?php the_content(); ?></div>
```

Стилі `.entry-content` розраховані на звичайні блоки Gutenberg, класи не потрібні:

- **Paragraph / Heading (H2, H3) / List / Quote / Image** — нумерацію «01, 02»,
  помаранчеву риску над H2 і галочки в списках малює CSS.
- **Group** з додатковим CSS-класом `callout` — темний блок «W skrócie»,
  перший абзац стає підписом.
- **Details** (core/details) — пункт FAQ-акордеону, працює без JS.
- Зміст (`<nav class="toc" data-toc>`) і `id` заголовків генерує `main.js` з H2 —
  руками нічого не треба. Якщо H2 немає, блок `.toc` ховається сам.

## Головна сторінка

Секції головної, які варто винести в ACF (flexible content), — у порядку верстки:

`hero` → `strip` → `marquee` → `benefits` → `uslugi` → `mobilny` →
`diagnostyka` (інфографіка) → `proces` → `objawy` → `opinie` → `o-nas` → `faq` → `kontakt`

Анімована схема обігу (`.circuit`) — це `<img>` + накладений inline SVG із
чотирма підписаними точками. Координати точок задані у відсотках, `viewBox`
збігається з розміром фото (1672×941). Якщо зміниться фото — перерахувати
`viewBox` і відсотки. Нижче 700 px накладка ховається (в CSS), лишається саме фото.

## Форми

Розмітка `.lead-form` уже містить валідацію (ім'я + телефон) і екран подяки.
Варіанти підключення:

1. **Contact Form 7 / WPForms** — замінити `<form class="lead-form">` шорткодом
   і лишити класи полів.
2. **Свій обробник** — передати URL у `<body data-form-endpoint="...">`;
   `main.js` відправить JSON `{imie, telefon, auto, wiadomosc, zrodlo, usluga}`.
3. Без `data-form-endpoint` відкривається поштовий клієнт на адресу
   `CONTACT_EMAIL` з `main.js` — **замінити на реальну пошту перед запуском**
   (зараз стоїть заглушка `kontakt@wroclawklima.pl`).

Поле `data-service` на формі підставляє назву послуги в тему листа.

## Ще треба зробити перед запуском

- [ ] Реальний e-mail у `CONTACT_EMAIL` (`js/main.js`) або `data-form-endpoint`.
- [ ] Сторінка політики приватності + посилання під формою.
- [ ] Google Analytics / Pixel, якщо потрібні.
- [ ] Перевірити NIP/REGON і адресу реєстрації на сторінці `kontakt/`.
- [ ] Картки «Wkrótce» на сторінці блогу — демо-заглушка, в темі їх не буде.

## Структурована розмітка

JSON-LD генерується в `_build/build_pages.py`:

- `AutoRepair` (головна + контакти) з годинами роботи й `areaServed`
- `Service` + `FAQPage` + `BreadcrumbList` на сторінках послуг
- `BlogPosting` + `BreadcrumbList` на статтях
- `FAQPage` на головній

У темі це перенести в `functions.php` або в шаблони — дані ті самі.

## Перегенерація демо

```bash
python3 dynamic-ac/_build/build_pages.py
```

Головна (`index.html`) написана руками — білдер її не чіпає. Спільна «обв'язка»
(топбар, хедер, футер, дровер, плаваючі CTA) живе в `build_pages.py`: якщо
міняєш її там, продублюй зміну в `index.html`.
