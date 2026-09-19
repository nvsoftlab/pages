# Перенос на WordPress

Демо — статичний HTML. `css/styles.css` і `js/main.js` переносяться в тему без змін
(`wp_enqueue_style` / `wp_enqueue_script`), шляхи до картинок → `get_template_directory_uri()`.

## Шаблони

| Демо | Тема WordPress |
|---|---|
| топбар, `.header`, меню | `header.php`, меню через `wp_nav_menu()` (пункти з класом `nav__link`) |
| `.footer`, `.dock`, `.mbar`, `.drawer`, `.lightbox`, `#kontakt` | `footer.php` |
| `index.html` | `front-page.php` |
| `<послуга>/index.html` | `page-usluga.php` (шаблон сторінки) + ACF: hero, 4 переваги, 5 кроків, 3 фото |
| `blog/index.html` | `home.php` — цикл постів, перший пост → `.post-feature`, решта → `.post-card` |
| `blog/<пост>/index.html` | `single.php` |

## Контент з редактора

Текст статті й опис послуги виводяться як є:

```php
<div class="entry-content"><?php the_content(); ?></div>
```

Стилі `.entry-content` розраховані на звичайні блоки Gutenberg, класи не потрібні:

- **Paragraph / Heading (H2) / List / Quote / Image**: нумерація «01, 02», лінії під H2 і галочки в списках малює CSS.
- **Group** з додатковим CSS-класом `callout`: синій блок «W skrócie», перший абзац стає підписом.
- **Details** (core/details): пункт FAQ-акордеону, працює без JS.
- Зміст (`<nav class="toc" data-toc>`) і `id` заголовків генерує `main.js` з H2, руками нічого не треба.

## Інше

- Мета статті (`.post-meta`): категорія, `get_the_date()`, час читання (можна з кількості слів).
- «Powiązana usługa»: ACF-поле «Relationship» на сторінку послуги.
- Форми: Contact Form 7 / WPForms, або лишити нашу розмітку й передати URL обробника в `<body data-form-endpoint="...">`.
- Картки «Wkrótce» на сторінці блогу — демо-заглушка, в темі їх не буде.
