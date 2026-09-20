# GETMON — demo strony

Statyczna wersja strony GETMON (Wrocław): klimatyzacja, wentylacja, pompy ciepła,
monitoring i systemy alarmowe. Zbudowana na bazie handoffu „GETMON design system”,
treść przeniesiona 1:1 z getmon.pl.

## Uruchomienie

```bash
python3 -m http.server 5174 --directory getmon
```

## Struktura

```
index.html                     strona główna (pisana ręcznie)
css/styles.css                 tokeny i komponenty z handoffu
js/main.js                     formularze, FAQ, drawer, dock, animacje linii
assets/img/                    logo + ikony GETMON
assets/img/bg/                 tła sekcji (+ _stock/ po podmianie zdjęć)
_build/build_pages.py          generator podstron + synchronizacja chrome
_build/content_services.py     treść 16 podstron usługowych
_build/content_blog.py         treść bloga (3 wpisy)
_build/fetch_images.py         podmiana teł na oryginalne zdjęcia GETMON
_build/WORDPRESS.md            instrukcja przeniesienia na WordPress
```

## Przebudowa podstron

```bash
python3 getmon/_build/build_pages.py
```

Treść edytujemy w `_build/content_*.py`, nie w wygenerowanym HTML.
Skrypt odświeża też nagłówek, stopkę, pasek CTA i sekcję kontaktu w `index.html`
(znaczniki `<!--#HEADER-->` … `<!--/#HEADER-->`).

## Strony

Slugi są identyczne jak na działającym getmon.pl — podmiana nie psuje żadnego
zaindeksowanego adresu.

- `/` — strona główna
- `/klimatyzacja-wroclaw/` + 6 podtypów + `/rodzaje-klimatyzacji/`
- `/wentylacja-wroclaw/`, `/pompy-ciepla-wroclaw/`
- `/montaz-monitoringu-wroclaw/` + IP + analogowy
- `/systemy-alarmowe-wroclaw/` + przewodowe + bezprzewodowe
- `/blog/` + 3 wpisy
- `/polityka-prywatnosci/`
