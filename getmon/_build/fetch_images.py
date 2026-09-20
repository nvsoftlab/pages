#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replaces the stock section backgrounds with GETMON's own photos.

The demo ships with free stock photos (Pexels) in assets/img/bg/, because
getmon.pl serves its photos from admin.getmon.pl, which sits behind an
adm.tools bot-protection that rate-limited us while the site was being built.

When you run this from a normal network (or once the block expires), it
downloads the originals into assets/img/bg/ under the SAME file names, so
every page picks them up with no HTML change. The stock files are kept in
assets/img/bg/_stock/ so you can roll back.

Run:  python3 getmon/_build/fetch_images.py
      python3 getmon/_build/fetch_images.py --restore     # back to stock
"""
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

BG = Path(__file__).resolve().parent.parent / 'assets' / 'img' / 'bg'
STOCK = BG / '_stock'
BASE = 'https://admin.getmon.pl/storage/'
UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/131.0 Safari/537.36')

# bg file name  ->  original on getmon.pl  (source page it appears on)
MAP = {
    'hero':                 'LBF4Hp9ssSBLstbQaKDO6XsS7i83wwahOVkMofvX.jpg',  # klimatyzacja-wroclaw
    'klimatyzacja':         'hm3De6x71uKdo5ev4iCGnKuMC8kyJ6sFle4qTvBO.jpg',  # klimatyzacja-wroclaw
    'klimatyzacja-2':       'jDb89LWXAnL0JBwKb059WeyQ7ZmL6JrTlF5czp5C.jpg',  # klimatyzacja-wroclaw
    'serwis':               'jg2RzIeReObXt3JAw6idRd5J1JeabqYDJ9e9EVaT.jpg',  # klimatyzacja-wroclaw
    'multisplit':           'l39LOtCJX1BZQm45cdI7oQi0FigXQtmymkBt91Pi.jpg',  # multi-split
    'kanalowa':             'aPjmhtiO93i3WIS7avU9aoQuataze92fxWUK5mhl.jpg',  # kanalowa
    'rodzaje':              'uAfKxnVxkEXxYLS3oNGMvwBWZ9fMKMS0aGUvac59.jpg',  # kanalowa
    'kasetonowa':           'sqtSJ0YBQzOv2g83boa4bb2x6zSPtspDfy79jjFX.jpg',  # kasetonowa
    'przypodlogowa':        'VQeJ32RML56qxR2FgB6b9hOnGqA7W8r3XklA2PXs.jpg',  # przypodlogowo-podsufitowa
    'przenosna':            'Znccq3D8GpWVp3ydwipcXCv8t41MHLRnXLedhs6A.jpg',  # przenosna
    'wentylacja':           'dNlROe4pHJgqI98k3e30bgggr3O2IVLVuNSehSPg.jpg',  # wentylacja
    'blog':                 'vsBo7MiZWBevuczAG8VoSWPSil9rOi2QnrYxZ7oF.jpg',  # wentylacja
    'opinie':               'a4E4UBwyEAtyeHV1zNDfkUIHvP0wp2fsLPkPGNM1.jpg',  # wentylacja
    'pompy':                'EuzEB9RWaJU9rDcQn2T6QUgjHPFanipa1anEeywO.jpg',  # pompy ciepla
    'band':                 'uff2g3hPkvGK8U1os7fA7MTyA4gRiUlsjQyVjZK7.jpg',  # pompy ciepla
    'monitoring':           '1bPC19eMXMEDpXYyMAtuGXzj1qlaB0lgxUO3PhCi.jpg',  # montaz monitoringu
    'proces':               'BDqk4B1ehIWIK8kr5Estm8SJLFOCAZxLq56ETHEj.jpg',  # scienna split
    'kontakt':              'lnOmrg61Tw6vyImQH4tN1prDWDxDa1aFFLN8G5Cg.jpg',  # scienna split
    # blog post images
    'ip':                   'XUbMN3HikWtdPRU8OQ4ReTCBOAZM4WacFnnfraBi.JPG',  # kanalowa
    'analogowy':            '2hyMXPA4FZwY7mcQSq3sY2Su1ZGEwyWiYdq4qOg8.jpg',  # blog: kanalowa
    'alarmy':               'k8jnrMRR7QkY3JTiJETsG61HVN7zcjHFGBqkbHQJ.jpg',  # blog: kanalowa
    'alarm-przewodowy':     'NNAbOEZnH6MFl3cEFovBvO6wHsfLrjHPpNSAQ7AK.jpg',  # blog: rekuperacja
    'alarm-bezprzewodowy':  'blog-images/01KPNK662M1TT57PX259F769FP.JPG',    # blog cover
}


def restore():
    if not STOCK.exists():
        print('nothing to restore — _stock/ is empty'); return
    n = 0
    for f in STOCK.glob('*.jpg'):
        shutil.copy2(f, BG / f.name); n += 1
    print(f'restored {n} stock images')


def fetch():
    STOCK.mkdir(exist_ok=True)
    ok = fail = 0
    for name, path in MAP.items():
        dst = BG / f'{name}.jpg'
        backup = STOCK / f'{name}.jpg'
        if dst.exists() and not backup.exists():
            shutil.copy2(dst, backup)          # keep the stock version once
        req = urllib.request.Request(BASE + path, headers={
            'User-Agent': UA, 'Referer': 'https://getmon.pl/',
            'Accept': 'image/avif,image/webp,image/*,*/*;q=0.8'})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
        except (urllib.error.URLError, urllib.error.HTTPError) as exc:
            print(f'  FAIL {name}: {exc}'); fail += 1; continue
        # the bot-protection answers 429 with a ~5 KB HTML page
        if len(data) < 20000 or data[:2] not in (b'\xff\xd8', b'\x89P'):
            print(f'  BLOCKED {name} ({len(data)} B — bot protection, try again later)')
            fail += 1
            continue
        dst.write_bytes(data)
        print(f'  ok {name}.jpg  {len(data)//1024} KB')
        ok += 1
    print(f'\n{ok} downloaded, {fail} failed. Stock backups in {STOCK}')
    if fail:
        print('Re-run later, or download the files by hand from getmon.pl and drop '
              'them into assets/img/bg/ under the names above.')


if __name__ == '__main__':
    restore() if '--restore' in sys.argv else fetch()
