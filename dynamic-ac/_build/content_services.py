"""Content of the service pages.

Source material: the service descriptions from wroclawklima.pl, rewritten to be
specific and sales-oriented (what the customer gets, what it costs them to wait)
without inventing facts about the business.
"""

ICONS = {
    'phone': '<path d="M4 5c0 8.3 6.7 15 15 15l1.5-3.4-4.3-2-2 2a12.6 12.6 0 0 1-6.8-6.8l2-2-2-4.3L4 5z"/>',
    'pin': '<path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
    'pulse': '<path d="M3 12h3.5l2-5 3 10 2.5-7 1.7 4H21"/>',
    'wrench': '<path d="M14.5 3.5a5 5 0 0 0-6.2 6.2L3 15v5h5l5.3-5.3a5 5 0 0 0 6.2-6.2l-3 3-2.8-2.8 3-3z"/>',
    'van': '<path d="M2 16h3l1.6-4.5h8.4L17 16h5"/><path d="M4 16v3h3v-3M17 16v3h3v-3"/>',
    'refresh': '<path d="M20 12a8 8 0 1 1-2.6-5.9"/><path d="M20 3.5V8h-4.5"/>',
    'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6l8-3z"/><path d="M8.5 12l2.5 2.5 4.5-4.5"/>',
    'gauge': '<path d="M12 20a8 8 0 1 1 8-8"/><path d="M12 12l4.5-3.5"/><circle cx="12" cy="12" r="1.4"/>',
    'drop': '<path d="M12 3.5c3.5 4.2 6 7.4 6 10.5a6 6 0 0 1-12 0c0-3.1 2.5-6.3 6-10.5z"/>',
    'snow': '<path d="M12 2v20M3.5 7l17 10M20.5 7l-17 10"/><path d="M12 6l-2.6-2.4M12 6l2.6-2.4M12 18l-2.6 2.4M12 18l2.6 2.4"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5.2l3.4 2"/>',
    'doc': '<rect x="4.5" y="3" width="15" height="18"/><path d="M8 8.5h8M8 12.5h8M8 16.5h4.5"/>',
    'search': '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/>',
    'gear': '<circle cx="12" cy="12" r="2.6"/><path d="M11 3h2l.4 2.3 2 .9 2-1.3 1.4 1.4-1.3 2 .9 2L21 11v2l-2.3.4-.9 2 1.3 2-1.4 1.4-2-1.3-2 .9L13 21h-2l-.4-2.3-2-.9-2 1.3-1.4-1.4 1.3-2-.9-2L3 13v-2l2.3-.4.9-2-1.3-2 1.4-1.4 2 1.3 2-.9z"/>',
    'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/>',
    'cash': '<rect x="2.5" y="6" width="19" height="12"/><circle cx="12" cy="12" r="2.6"/><path d="M6 9.5v5M18 9.5v5"/>',
}

SERVICES = [
    # ------------------------------------------------------------------ 01 --
    {
        'slug': 'diagnostyka-i-konserwacja',
        'cta': 'diagnostykę i konserwację',
        'num': '01',
        'name': 'Diagnostyka i konserwacja',
        'nav': 'Diagnostyka i konserwacja',
        'short': 'Kontrola szczelności, pomiar wydajności, wymiana czynnika i dezynfekcja układu.',
        'title': 'Przegląd klimatyzacji samochodowej Wrocław | Dynamic AC',
        'desc': 'Mobilna diagnostyka i konserwacja klimatyzacji samochodowej we Wrocławiu. '
                'Kontrola szczelności, pomiar wydajności, wymiana czynnika i dezynfekcja układu u klienta. Zadzwoń: 575 749 772.',
        'pill': 'Przegląd • szczelność • dezynfekcja',
        'h1': 'Diagnostyka i konserwacja<br class="br-desk"> klimatyzacji samochodowej',
        'lead': 'Roczny przegląd kosztuje ułamek tego, co wymiana sprężarki. Sprawdzamy cały układ, '
                'pokazujemy pomiary i mówimy wprost, co wymaga uwagi teraz, a co może poczekać.',
        'hero_img': 'diagnostyka.jpg',
        'highlights': [
            ('gauge', 'Pomiar ciśnień', 'Strona wysoka i niska pod obciążeniem'),
            ('search', 'Kontrola szczelności', 'Detektor elektroniczny i kontrast UV'),
            ('snow', 'Wymiana czynnika', 'Odzysk, osuszenie i napełnienie z wagą'),
            ('drop', 'Dezynfekcja układu', 'Ozonowanie i wymiana filtra kabinowego'),
        ],
        'intro': 'Klimatyzacja samochodowa traci rocznie kilkanaście procent czynnika — to normalne zjawisko, '
                 'wynikające z przenikania przez elastyczne przewody i uszczelnienia. Problem w tym, że razem z czynnikiem '
                 'ucieka olej smarujący sprężarkę. Auto, które „jeszcze trochę chłodzi”, potrafi w ciągu jednego sezonu '
                 'zajechać sprężarkę — a to już koszt liczony w tysiącach złotych zamiast w kilkuset. Dlatego regularna '
                 'diagnostyka i konserwacja to najtańsza rzecz, jaką możesz zrobić dla układu klimatyzacji.',
        'sections': [
            ('Co dokładnie sprawdzamy podczas przeglądu', [
                'Przegląd zaczynamy od pomiaru ciśnień roboczych po stronie wysokiej i niskiej przy pracującym silniku. '
                'Same ciśnienia mówią bardzo dużo: inaczej zachowuje się układ z niedoborem czynnika, inaczej z niedrożnym '
                'skraplaczem, a jeszcze inaczej z zatartym zaworem rozprężnym. Do tego dokładamy pomiar temperatury '
                'powietrza na wylocie z nawiewów i porównujemy go z temperaturą otoczenia.',
                'Następnie przechodzimy do kontroli szczelności. Używamy detektora elektronicznego, a przy trudniejszych '
                'przypadkach kontrastu UV, który pokazuje miejsce ucieczki czynnika nawet wtedy, gdy nieszczelność jest '
                'minimalna. Sprawdzamy stan sprzęgła sprężarki, napięcie i stan paska, drożność skraplacza oraz odpływ '
                'skroplin — zapchany odpływ to najczęstsza przyczyna mokrej wykładziny po stronie pasażera.',
            ]),
            ('Wymiana czynnika — dlaczego „dolewka” to za mało', [
                'Sam dolew czynnika bez odzysku to strzał w ciemno: nie wiesz, ile środka faktycznie zostało w układzie, '
                'a przepełniony układ chłodzi gorzej niż niedopełniony i pracuje przy zawyżonym ciśnieniu. My pracujemy '
                'stacją obsługi klimatyzacji: najpierw odzyskujemy pozostały czynnik, ważymy go, osuszamy i odpowietrzamy '
                'układ próżnią, a dopiero potem napełniamy odważoną ilością zgodną z tabliczką producenta.',
                'Próżnia to etap, który bywa pomijany, a jest kluczowy. Wilgoć w układzie tworzy z olejem związki '
                'kwaśne, które zżerają uszczelnienia od środka. Kilkanaście minut na pompie próżniowej to różnica między '
                'naprawą na lata a powrotem problemu za pół roku.',
            ]),
            ('Dezynfekcja: skąd bierze się zapach z nawiewów', [
                'Parownik klimatyzacji pracuje w temperaturze bliskiej zera i jest stale wilgotny. To idealne środowisko '
                'dla grzybów i bakterii, które osadzają się na jego lamelach i przy każdym uruchomieniu nawiewu trafiają '
                'prosto do kabiny. Charakterystyczny „piwniczny” zapach po włączeniu klimatyzacji to właśnie one.',
                'W ramach konserwacji wykonujemy ozonowanie wnętrza i układu wentylacji oraz wymieniamy filtr kabinowy. '
                'Ozon dociera tam, gdzie nie sięga żaden aerozol — do kanałów wentylacyjnych i na powierzchnię parownika. '
                'Efekt jest odczuwalny od razu, a przy regularnym powtarzaniu problem po prostu nie wraca.',
            ]),
            ('Jak często robić przegląd klimatyzacji?', [
                'Przyjmuje się, że obsługę klimatyzacji warto wykonywać raz na rok, najlepiej wiosną — zanim zacznie się '
                'sezon i zanim okaże się, że w pierwszy upalny dzień układ nie chłodzi. Wymiana filtra kabinowego przy tej '
                'okazji to naturalny moment, bo i tak jest zdejmowana obudowa.',
                'Jeżeli auto ma więcej niż dziesięć lat albo było już naprawiane w obrębie układu klimatyzacji, warto '
                'skrócić ten okres. Starsze uszczelnienia tracą elastyczność i ubytek czynnika rośnie. Regularna kontrola '
                'pozwala wychwycić moment, w którym warto wymienić o-ringi za kilkadziesiąt złotych zamiast czekać na '
                'awarię sprężarki. Jeśli objawy już występują, zobacz <a href="../naprawy-biezace/">naprawy bieżące</a>.',
            ]),
        ],
        'steps_title': 'Przegląd krok po kroku',
        'steps_lead': 'Od podłączenia stacji do raportu z pomiarami — zwykle 60–90 minut na miejscu u klienta.',
        'steps': [
            ('gauge', 'Pomiar wyjściowy', 'Ciśnienia robocze, temperatura na nawiewach, stan sprzęgła sprężarki.'),
            ('search', 'Kontrola szczelności', 'Detektor elektroniczny, a w razie potrzeby kontrast UV.'),
            ('snow', 'Odzysk i próżnia', 'Odzyskujemy czynnik, ważymy go i osuszamy układ próżnią.'),
            ('drop', 'Napełnienie i dezynfekcja', 'Odważona dawka czynnika, ozonowanie i nowy filtr kabinowy.'),
            ('doc', 'Raport i zalecenia', 'Mówimy, co jest sprawne, a co wymaga uwagi w najbliższym sezonie.'),
        ],
        'gallery': ['diagnostyka.jpg', 'serwis-audi.jpg', 'hero.jpg'],
        'faq': [
            ('Ile trwa przegląd klimatyzacji?',
             'Standardowo 60–90 minut. Dłużej, jeśli trzeba szukać nieszczelności kontrastem UV — wtedy umawiamy się na '
             'ponowną kontrolę po kilku dniach jazdy.'),
            ('Czy po przeglądzie klimatyzacja chłodzi lepiej?',
             'Jeżeli przyczyną słabego chłodzenia był ubytek czynnika lub zabrudzony parownik — tak, różnica jest '
             'odczuwalna od razu. Jeśli problem leży w sprężarce lub zaworze, przegląd to pokaże i powiemy o tym przed naprawą.'),
            ('Czy robicie przeglądy aut z czynnikiem R1234yf?',
             'Tak, obsługujemy zarówno starsze układy na R134a, jak i nowsze na R1234yf. Każdy czynnik obsługujemy '
             'osobnym osprzętem — to wymóg, nie preferencja.'),
        ],
    },
    # ------------------------------------------------------------------ 02 --
    {
        'slug': 'serwis-gwarancyjny',
        'cta': 'serwis gwarancyjny',
        'num': '02',
        'name': 'Serwis gwarancyjny',
        'nav': 'Serwis gwarancyjny',
        'short': 'Obsługa nowych systemów zgodnie z wymaganiami producenta — bez utraty gwarancji.',
        'title': 'Serwis gwarancyjny klimatyzacji Wrocław | Dynamic AC',
        'desc': 'Mobilny serwis gwarancyjny klimatyzacji we Wrocławiu. Przeglądy zgodne z wymaganiami producenta, '
                'dokumentacja serwisowa, obsługa u klienta. Zadzwoń: 575 749 772.',
        'pill': 'Przeglądy • dokumentacja • gwarancja',
        'h1': 'Serwis gwarancyjny<br class="br-desk"> klimatyzacji',
        'lead': 'Nowe auto nie musi wracać do salonu po każdy przegląd klimatyzacji. Obsługujemy układ zgodnie '
                'z wymaganiami producenta i zostawiamy dokumentację, która to potwierdza.',
        'hero_img': 'hero.jpg',
        'highlights': [
            ('shield', 'Zgodnie z wymogami', 'Procedura i parametry według producenta'),
            ('doc', 'Dokumentacja', 'Faktura i opis wykonanych czynności'),
            ('van', 'U klienta', 'Bez zostawiania auta na cały dzień'),
            ('clock', 'Terminy', 'Także po godzinach pracy salonów'),
        ],
        'intro': 'Panuje przekonanie, że każdą obsługę nowego auta trzeba wykonać w ASO, bo inaczej „przepada gwarancja”. '
                 'W praktyce chodzi o coś innego: czynności muszą być wykonane zgodnie z zaleceniami producenta, '
                 'we właściwych odstępach i muszą być udokumentowane. Serwis gwarancyjny klimatyzacji w Dynamic AC spełnia '
                 'te trzy warunki — a przy okazji nie kosztuje Cię całego dnia i dojazdu na drugi koniec miasta.',
        'sections': [
            ('Co obejmuje obsługa gwarancyjna', [
                'Zakres ustalamy na podstawie wymagań producenta dla konkretnego modelu: rodzaj i odważona ilość czynnika, '
                'typ oleju sprężarkowego, interwał wymiany filtra kabinowego oraz zakres kontroli układu. Nowe auta '
                'w większości pracują na czynniku R1234yf, który wymaga osobnego osprzętu — mamy go i nie mieszamy obiegów.',
                'Standardowa obsługa obejmuje kontrolę szczelności, odzysk i ponowne napełnienie układu odważoną dawką '
                'czynnika, kontrolę parametrów pracy oraz wymianę filtra kabinowego. Wszystko opisujemy na fakturze, '
                'razem z datą, przebiegiem i wykonanymi czynnościami.',
            ]),
            ('Dokumentacja, która broni gwarancji', [
                'Najczęstszy błąd właścicieli aut na gwarancji to brak śladu po wykonanej obsłudze. Ustna informacja '
                '„robiłem klimę w zeszłym roku” nie jest dowodem. Dlatego każda usługa kończy się fakturą z opisem zakresu '
                'prac — to dokument, który przedstawiasz, gdyby kiedykolwiek pojawiło się pytanie o historię serwisową układu.',
                'Jeśli w Twoim aucie obowiązuje książka serwisowa lub elektroniczny rejestr obsługi, powiedz o tym przy '
                'umawianiu terminu — dostosujemy formę potwierdzenia.',
            ]),
            ('Dlaczego warto trzymać interwał', [
                'Obsługa gwarancyjna to nie formalność wymyślona po to, żeby częściej odwiedzać serwis. Układ klimatyzacji '
                'z prawidłową ilością czynnika ma prawidłową ilość oleju, a sprężarka pracuje w warunkach, na jakie została '
                'zaprojektowana. Pominięty przegląd nie objawia się od razu — objawia się po dwóch, trzech latach, '
                'zwykle awarią najdroższego elementu w układzie.',
                'Przy okazji obsługi wykonujemy pełną <a href="../diagnostyka-i-konserwacja/">diagnostykę i konserwację</a>, '
                'więc dostajesz realny obraz stanu układu, a nie tylko odhaczoną pozycję na liście.',
            ]),
        ],
        'steps_title': 'Jak wygląda obsługa gwarancyjna',
        'steps_lead': 'Ustalamy zakres, wykonujemy obsługę u Ciebie i zostawiamy dokumentację.',
        'steps': [
            ('phone', 'Ustalenie zakresu', 'Marka, model i rocznik — na tej podstawie dobieramy procedurę.'),
            ('pin', 'Dojazd na miejsce', 'Pod dom, biuro albo na firmowy parking.'),
            ('snow', 'Obsługa układu', 'Kontrola szczelności, odzysk, próżnia i odważone napełnienie.'),
            ('gear', 'Filtr i kontrola', 'Wymiana filtra kabinowego i pomiar parametrów pracy.'),
            ('doc', 'Dokumentacja', 'Faktura z opisem zakresu — dowód wykonanej obsługi.'),
        ],
        'gallery': ['hero.jpg', 'van.jpg', 'diagnostyka.jpg'],
        'faq': [
            ('Czy stracę gwarancję, robiąc przegląd poza ASO?',
             'Nie, jeśli obsługa jest wykonana zgodnie z wymaganiami producenta i udokumentowana. Dokładnie tak pracujemy '
             'i taką dokumentację zostawiamy.'),
            ('Obsługujecie auta na czynniku R1234yf?',
             'Tak. Do R1234yf używamy dedykowanego osprzętu — obiegów R134a i R1234yf nigdy nie łączymy.'),
            ('Czy możecie przyjechać pod firmę w godzinach pracy?',
             'Tak, to najczęstszy scenariusz przy autach służbowych. Ustalamy godzinę i obsługujemy auto na parkingu, '
             'bez wyłączania go z użycia na dłużej niż potrzeba.'),
        ],
    },
    # ------------------------------------------------------------------ 03 --
    {
        'slug': 'naprawy-biezace',
        'cta': 'naprawę klimatyzacji',
        'num': '03',
        'name': 'Naprawy bieżące',
        'nav': 'Naprawy bieżące',
        'short': 'Lokalizacja nieszczelności, wymiana uszczelnień, zaworków i osuszacza.',
        'title': 'Naprawa klimatyzacji samochodowej Wrocław | Dynamic AC',
        'desc': 'Naprawa klimatyzacji samochodowej we Wrocławiu z dojazdem do klienta. Lokalizacja nieszczelności, '
                'wymiana uszczelnień, zaworków i osuszacza. Wycena przed naprawą. Zadzwoń: 575 749 772.',
        'pill': 'Nieszczelności • uszczelnienia • osuszacz',
        'h1': 'Naprawy bieżące<br class="br-desk"> układu klimatyzacji',
        'lead': 'Znajdujemy przyczynę, podajemy cenę, dopiero potem naprawiamy. Większość prac wykonujemy '
                'na miejscu — bez holowania, bez zostawiania auta i bez niespodzianek na fakturze.',
        'hero_img': 'serwis-audi.jpg',
        'highlights': [
            ('search', 'Lokalizacja wycieku', 'Detektor i kontrast UV zamiast zgadywania'),
            ('wrench', 'Naprawa na miejscu', 'O-ringi, zaworki, osuszacz, przewody'),
            ('cash', 'Cena przed naprawą', 'Znamy zakres — mówimy, ile to kosztuje'),
            ('van', 'Bez warsztatu', 'Przyjeżdżamy tam, gdzie stoi auto'),
        ],
        'intro': 'Najdroższa naprawa klimatyzacji to ta, która była robiona trzy razy. Dlatego nie zaczynamy od dolewania '
                 'czynnika i sprawdzania „czy pomoże”. Najpierw ustalamy, gdzie układ traci szczelność albo dlaczego nie '
                 'osiąga parametrów — i dopiero wtedy rozmawiamy o naprawie i jej koszcie.',
        'sections': [
            ('Najczęstsze usterki i ich objawy', [
                'Stopniowo słabnące chłodzenie to prawie zawsze ubytek czynnika. Źródłem bywają zużyte o-ringi na '
                'połączeniach, zaworki serwisowe, korozja na przewodach aluminiowych albo uszkodzony skraplacz — ten '
                'ostatni stoi z przodu auta i zbiera wszystko, co leci spod kół.',
                'Chłodzenie, które znika nagle i całkowicie, wskazuje raczej na stronę elektryczną lub mechaniczną: '
                'sprzęgło sprężarki, czujnik ciśnienia, bezpiecznik albo zatartą sprężarkę. Głośna praca po włączeniu '
                'klimatyzacji to ostrzeżenie, którego nie warto ignorować — sprężarka pracująca bez oleju kończy '
                'wiórami w całym układzie, a to zamienia naprawę za kilkaset złotych w wymianę połowy instalacji.',
                'Zaparowane szyby i mokra wykładzina po stronie pasażera zwykle nie mają nic wspólnego z chłodzeniem — '
                'to zatkany odpływ skroplin. Kilkanaście minut pracy zamiast wymiany czegokolwiek.',
            ]),
            ('Jak szukamy nieszczelności', [
                'Zaczynamy od detektora elektronicznego, który reaguje na obecność czynnika w powietrzu wokół połączeń. '
                'Przy większych ubytkach to wystarcza, żeby wskazać miejsce w kilka minut. Przy mikronieszczelnościach '
                'wprowadzamy do układu kontrast UV, napełniamy go i prosimy o normalną eksploatację przez kilka dni — '
                'po tym czasie lampa UV pokazuje dokładnie, gdzie olej z kontrastem wychodzi na zewnątrz.',
                'Ta druga metoda wymaga cierpliwości, ale daje pewność. Alternatywą jest wymiana kolejnych elementów '
                '„w ciemno”, co kosztuje znacznie więcej i zwykle i tak kończy się powrotem problemu.',
            ]),
            ('Co naprawiamy bezpośrednio u klienta', [
                'Wyposażenie mobilnej jednostki pozwala wykonać na miejscu zdecydowaną większość typowych napraw: wymianę '
                'o-ringów i uszczelnień, wymianę zaworków serwisowych, wymianę filtra osuszacza, udrożnienie odpływu '
                'skroplin, wymianę czujnika ciśnienia, a często również wymianę przewodu czy skraplacza.',
                'Są prace, które wymagają podnośnika albo demontażu deski rozdzielczej — na przykład wymiana parownika. '
                'W takich przypadkach mówimy o tym otwarcie przy wycenie, zamiast zaczynać naprawę, której nie da się '
                'dokończyć na parkingu. Po każdej naprawie układ przechodzi próżnię, napełnienie odważoną dawką czynnika '
                'i kontrolę parametrów pracy.',
            ]),
            ('Ile kosztuje naprawa klimatyzacji?', [
                'Uczciwa odpowiedź brzmi: zależy od tego, co jest zepsute — i dlatego zawsze zaczynamy od diagnostyki. '
                'Wymiana o-ringa to inny rząd wielkości niż wymiana sprężarki, a bez pomiaru nikt nie jest w stanie '
                'powiedzieć, który to przypadek.',
                'Co możemy obiecać: cenę podajemy przed rozpoczęciem naprawy, a jeśli w trakcie okaże się, że zakres '
                'jest większy, dzwonimy i pytamy, zanim cokolwiek zrobimy. Klienci piszą o tym w '
                '<a href="../#opinie">opiniach</a> najczęściej — brak dopisywania kosztów po fakcie.',
            ]),
        ],
        'steps_title': 'Naprawa krok po kroku',
        'steps_lead': 'Diagnostyka, wycena, naprawa i kontrola — w tej kolejności.',
        'steps': [
            ('phone', 'Opis objawu', 'Przez telefon zwykle już wiemy, czego szukać na miejscu.'),
            ('search', 'Diagnostyka', 'Pomiar ciśnień, detektor, w razie potrzeby kontrast UV.'),
            ('cash', 'Wycena', 'Podajemy zakres i cenę, zanim zaczniemy naprawę.'),
            ('wrench', 'Naprawa', 'Wymiana uszkodzonych elementów na miejscu u klienta.'),
            ('snow', 'Próżnia i napełnienie', 'Osuszenie układu, odważona dawka czynnika, kontrola pracy.'),
        ],
        'gallery': ['serwis-audi.jpg', 'diagnostyka.jpg', 'mobilny.jpg'],
        'faq': [
            ('Czy naprawicie klimatyzację pod blokiem?',
             'Tak, to nasz standardowy tryb pracy. Potrzebujemy tylko miejsca, żeby stanąć obok auta i otworzyć maskę.'),
            ('Co, jeśli nie da się naprawić na miejscu?',
             'Mówimy o tym od razu po diagnostyce, zanim cokolwiek zaczniemy. Za samą diagnostykę wiesz wtedy, co jest '
             'uszkodzone i jakiego zakresu prac wymaga naprawa.'),
            ('Dolewacie sam czynnik, bez szukania przyczyny?',
             'Odradzamy — czynnik uciekłby ponownie, a razem z nim olej. Jeśli mimo to zależy Ci wyłącznie na dolewce, '
             'powiemy wprost, na jak długo to wystarczy.'),
        ],
    },
    # ------------------------------------------------------------------ 04 --
    {
        'slug': 'modernizacja',
        'cta': 'modernizację układu',
        'num': '04',
        'name': 'Modernizacja',
        'nav': 'Modernizacja',
        'short': 'Retrofitting starszych instalacji i dopasowanie nowoczesnych rozwiązań.',
        'title': 'Retrofitting klimatyzacji samochodowej | Dynamic AC',
        'desc': 'Modernizacja starszych układów klimatyzacji samochodowej i retrofitting we Wrocławiu. '
                'Przezbrojenie z R12, wymiana osprzętu, dopasowanie nowszych rozwiązań. Zadzwoń: 575 749 772.',
        'pill': 'Retrofitting • starsze auta • przezbrojenie',
        'h1': 'Modernizacja<br class="br-desk"> i retrofitting',
        'lead': 'Starsze auto nie znaczy „nie da się”. Zajmujemy się układami, które w większości warsztatów '
                'kwitowane są wzruszeniem ramion — i doprowadzamy je do stanu używalności.',
        'hero_img': 'van.jpg',
        'highlights': [
            ('refresh', 'Przezbrojenie', 'Starsze instalacje na aktualny czynnik'),
            ('gear', 'Dobór osprzętu', 'Zaworki, olej i osuszacz pod nowy czynnik'),
            ('sun', 'Realna wydajność', 'Pomiar po modernizacji, nie deklaracje'),
            ('shield', 'Uczciwa ocena', 'Powiemy, gdy modernizacja się nie opłaca'),
        ],
        'intro': 'Klimatyzacja w aucie z przełomu wieków to często instalacja, która stoi nieużywana od lat — bo „kiedyś '
                 'przestała chłodzić” i nikt nie chciał się nią zająć. Tymczasem w większości przypadków da się ją '
                 'przywrócić do pracy, a przy okazji przezbroić na czynnik dostępny dziś w normalnej cenie.',
        'sections': [
            ('Na czym polega retrofitting', [
                'Retrofitting to przystosowanie istniejącej instalacji do pracy z innym czynnikiem chłodniczym niż ten, '
                'na który została zaprojektowana. Dotyczy to przede wszystkim aut zbudowanych pod czynnik R12, który '
                'został wycofany z użycia — jego uzupełnienie dziś jest praktycznie niemożliwe.',
                'Sama zamiana czynnika to jednak tylko część pracy. Nowy czynnik pracuje z innym olejem, wymaga innych '
                'zaworków serwisowych i innych uszczelnień. Dlatego przezbrojenie obejmuje wymianę filtra osuszacza, '
                'przepłukanie układu ze starego oleju, wymianę o-ringów oraz montaż właściwych przyłączy. Skrócenie '
                'którejkolwiek z tych czynności kończy się tak samo: układ przestaje chłodzić w ciągu kilku miesięcy.',
            ]),
            ('Kiedy modernizacja ma sens, a kiedy nie', [
                'Modernizacja opłaca się wtedy, gdy podstawowe elementy układu — sprężarka, skraplacz i parownik — są '
                'sprawne albo dostępne w rozsądnej cenie. Wtedy całość sprowadza się do przezbrojenia, wymiany elementów '
                'eksploatacyjnych i uszczelnienia instalacji.',
                'Bywa jednak, że koszt części przekracza wartość, jaką modernizacja wnosi do auta — na przykład gdy '
                'skorodowany jest i skraplacz, i przewody, a sprężarka ma wybicie. Mówimy o tym wprost, z liczbami, '
                'zamiast zaczynać pracę i informować o tym w połowie. To Twoja decyzja, ale powinna być podjęta na '
                'podstawie pełnego obrazu.',
            ]),
            ('Co zyskujesz po modernizacji', [
                'Przede wszystkim działającą klimatyzację w aucie, w którym nie działała od lat — a to w upalny dzień '
                'różnica trudna do przecenienia. Po drugie, układ na aktualnym czynniku obsłużysz w dowolnym serwisie, '
                'bez szukania kogoś, kto ma jeszcze zapas wycofanego środka.',
                'Po trzecie, sprawna klimatyzacja to również szybsze odparowanie szyb zimą i mniej wilgoci w kabinie. '
                'Po zakończeniu prac wykonujemy pomiar wydajności i pokazujemy realną temperaturę na nawiewach, '
                'a układ obejmujemy normalną <a href="../diagnostyka-i-konserwacja/">obsługą serwisową</a>.',
            ]),
        ],
        'steps_title': 'Modernizacja krok po kroku',
        'steps_lead': 'Ocena stanu, decyzja z liczbami, przezbrojenie i pomiar efektu.',
        'steps': [
            ('search', 'Ocena stanu', 'Sprawdzamy, co w instalacji nadaje się do dalszej pracy.'),
            ('cash', 'Kosztorys', 'Pokazujemy koszt części i pracy — decyzja należy do Ciebie.'),
            ('refresh', 'Przezbrojenie', 'Przepłukanie układu, nowy olej, osuszacz i przyłącza.'),
            ('wrench', 'Uszczelnienie', 'Wymiana o-ringów i elementów, które nie trzymają ciśnienia.'),
            ('sun', 'Pomiar wydajności', 'Napełnienie, próba i realna temperatura na nawiewach.'),
        ],
        'gallery': ['van.jpg', 'mobilny.jpg', 'serwis-audi.jpg'],
        'faq': [
            ('Mam auto z 1998 roku i klimę na R12. Da się coś zrobić?',
             'W większości przypadków tak — to typowy przypadek retrofittingu. Zaczynamy od oceny stanu instalacji '
             'i kosztorysu, żebyś wiedział, czy to się opłaca.'),
            ('Czy po przezbrojeniu klimatyzacja chłodzi tak samo?',
             'Zwykle nieco słabiej niż na oryginalnym czynniku, ale różnica jest niewielka i w praktyce niezauważalna. '
             'Po zakończeniu prac mierzymy temperaturę na nawiewach i pokazujemy wynik.'),
            ('Ile trwa modernizacja?',
             'Zależy od zakresu. Samo przezbrojenie sprawnej instalacji to kilka godzin; jeśli dochodzi wymiana '
             'skraplacza czy przewodów, umawiamy się na konkretny termin i podajemy czas przy wycenie.'),
        ],
    },
]

SERVICE_BY_SLUG = {s['slug']: s for s in SERVICES}
