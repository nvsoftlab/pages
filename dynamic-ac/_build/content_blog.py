"""Blog posts — the demo content for `blog/index.html` and `blog/<slug>/`.

In the WordPress theme these become ordinary posts; the markup they generate is
plain Gutenberg (paragraphs, H2, lists, a Group with the `callout` class and
core/details blocks), so the editor output needs no extra classes.
"""

POSTS = [
    {
        'slug': 'jak-czesto-serwisowac-klimatyzacje-w-samochodzie',
        'title': 'Jak często serwisować klimatyzację w samochodzie?',
        'excerpt': 'Raz na rok czy raz na dwa lata? Wyjaśniamy, skąd bierze się ten interwał, '
                   'co się dzieje z układem między przeglądami i po czym poznać, że nie warto już czekać.',
        'date': '2026-04-18',
        'date_pl': '18 kwietnia 2026',
        'cat': 'Poradnik',
        'read': '6 min',
        'img': 'diagnostyka.jpg',
        'service': 'diagnostyka-i-konserwacja',
        'lead': 'Najczęstsze pytanie, jakie dostajemy przez telefon. Odpowiedź „raz na rok” jest prawdziwa, '
                'ale bez wyjaśnienia brzmi jak próba sprzedania kolejnej usługi. Poniżej — dlaczego ten interwał '
                'akurat tyle wynosi.',
        'body': [
            ('h2', 'Dlaczego czynnik ubywa nawet w sprawnym układzie'),
            ('p', 'Instalacja klimatyzacji w samochodzie nie jest szczelna w takim sensie, w jakim szczelna jest '
                  'lodówka. Zawiera elastyczne przewody i dziesiątki połączeń z o-ringami, a całość pracuje w warunkach '
                  'drgań i zmian temperatury od minus dwudziestu do plus stu stopni. Producenci zakładają, że układ '
                  'traci rocznie około 10–15% czynnika i jest to zjawisko normalne, a nie usterka.'),
            ('p', 'Problem polega na tym, że czynnik chłodniczy jest nośnikiem oleju smarującego sprężarkę. Mniej '
                  'czynnika oznacza mniej oleju w obiegu. Sprężarka pracuje wtedy w warunkach, na jakie nie została '
                  'zaprojektowana — i robi to cicho, bez ostrzeżenia, aż do momentu awarii.'),
            ('callout', ['W skrócie',
                         'Po dwóch latach bez obsługi w układzie brakuje zwykle około jednej czwartej czynnika. '
                         'Chłodzenie jest wtedy jeszcze odczuwalne, więc nikt nie reaguje — a sprężarka już pracuje '
                         'na granicy.']),
            ('h2', 'Skąd wziął się interwał roczny'),
            ('p', 'Roczna obsługa to kompromis między ubytkiem czynnika a kosztem serwisu. Przy corocznym uzupełnieniu '
                  'układ praktycznie nie schodzi poniżej poziomu, przy którym smarowanie sprężarki jest zagrożone. '
                  'Dodatkowo raz w roku wypada wymiana filtra kabinowego, a obudowa i tak jest wtedy zdejmowana — '
                  'dwie czynności w jednej wizycie zamiast dwóch osobnych.'),
            ('p', 'Drugi powód jest biologiczny. Parownik pracuje w temperaturze bliskiej zera i jest stale wilgotny, '
                  'co czyni go idealnym środowiskiem dla grzybów. Coroczna dezynfekcja nie dopuszcza do tego, żeby '
                  'osad zdążył się zadomowić — usunięcie zaniedbanego parownika jest znacznie droższe niż zapobieganie.'),
            ('h2', 'Kiedy skrócić odstęp'),
            ('ul', [
                'Auto ma powyżej dziesięciu lat — uszczelnienia straciły elastyczność i ubytek czynnika rośnie.',
                'Układ był już naprawiany — każde rozszczelnienie instalacji to nowe miejsca potencjalnego wycieku.',
                'Auto stoi na zewnątrz i sporo jeździ w mieście — skraplacz szybciej się zapycha i koroduje.',
                'Czujesz zapach przy uruchomieniu nawiewu — to sygnał, że parownik wymaga uwagi, nie kolejnego zapachu choinki.',
            ]),
            ('h2', 'Po czym poznać, że czekanie już się nie opłaca'),
            ('p', 'Najbardziej wymowny objaw to stopniowe pogarszanie chłodzenia z sezonu na sezon. Jeśli w zeszłym '
                  'roku auto chłodziło lepiej niż w tym, a nic się nie zepsuło, to znaczy dokładnie tyle: w układzie '
                  'brakuje czynnika. Drugi sygnał to głośniejsza praca po włączeniu klimatyzacji — sprężarka, która '
                  'zaczyna być słyszalna, prosi o uwagę.'),
            ('p', 'Trzeci, najczęściej ignorowany, to mokra wykładzina po stronie pasażera. Zwykle nie ma nic wspólnego '
                  'ze szczelnością układu — to zatkany odpływ skroplin, naprawa na kilkanaście minut, jeśli zająć się '
                  'nią zanim woda zdąży dobrać się do elektryki pod dywanikiem.'),
            ('h2', 'Co zrobić teraz'),
            ('p', 'Jeżeli nie pamiętasz, kiedy ostatnio ktoś zaglądał do Twojej klimatyzacji, najtańszą rzeczą jest '
                  'przegląd z pomiarem — pokaże, czy w ogóle jest problem. Zajmuje godzinę i możemy wykonać go tam, '
                  'gdzie stoi auto.'),
        ],
    },
    {
        'slug': 'dlaczego-klimatyzacja-slabo-chlodzi',
        'title': 'Klimatyzacja słabo chłodzi — pięć najczęstszych przyczyn',
        'seo_title': 'Klimatyzacja słabo chłodzi — 5 przyczyn',
        'excerpt': 'Od najbardziej prawdopodobnej do najdroższej. Co da się sprawdzić samemu w pięć minut, '
                   'a co wymaga podłączenia stacji i manometrów.',
        'date': '2026-05-22',
        'date_pl': '22 maja 2026',
        'cat': 'Diagnostyka',
        'read': '7 min',
        'img': 'serwis-audi.jpg',
        'service': 'naprawy-biezace',
        'lead': 'Ustawiasz najniższą temperaturę, dmuchawa wyje, a z nawiewów leci letnie powietrze. '
                'Poniżej pięć przyczyn w kolejności od najczęstszej — razem z tym, co możesz sprawdzić sam, '
                'zanim gdziekolwiek zadzwonisz.',
        'body': [
            ('h2', '1. Za mało czynnika w układzie'),
            ('p', 'To przyczyna numer jeden, odpowiedzialna za zdecydowaną większość zgłoszeń. Układ traci czynnik '
                  'naturalnie, a jeśli nikt go nie uzupełniał od kilku lat, poziom spada poniżej progu, przy którym '
                  'możliwe jest skuteczne chłodzenie. Charakterystyczny objaw: chłodzenie pogarszało się stopniowo, '
                  'z sezonu na sezon, a nie zniknęło z dnia na dzień.'),
            ('p', 'Czego nie robić: dolewać czynnika z puszki bez pomiaru. Przepełniony układ chłodzi gorzej niż '
                  'niedopełniony i pracuje przy zawyżonym ciśnieniu, co obciąża sprężarkę.'),
            ('h2', '2. Zabrudzony skraplacz'),
            ('p', 'Skraplacz to chłodnica klimatyzacji, umieszczona z przodu auta, przed chłodnicą silnika. Zbiera '
                  'wszystko: owady, liście, sól drogową i piasek. Zapchany skraplacz nie oddaje ciepła, więc czynnik '
                  'nie skrapla się prawidłowo i wydajność spada — szczególnie w korku, gdy brakuje naporu powietrza.'),
            ('p', 'To jedyna pozycja z tej listy, którą możesz ocenić sam: zajrzyj przez kratkę zderzaka przy '
                  'dobrym świetle. Jeśli widzisz zwartą warstwę brudu zamiast lameli, masz kandydata na przyczynę.'),
            ('h2', '3. Zatkany filtr kabinowy'),
            ('p', 'Ten przypadek często bywa mylony ze słabym chłodzeniem, choć układ działa poprawnie — po prostu '
                  'przez filtr nie przechodzi dość powietrza. Objaw rozpoznawczy: powietrze z nawiewów jest zimne, '
                  'ale jest go mało, a dmuchawa na najwyższym biegu robi więcej hałasu niż przeciągu.'),
            ('p', 'Filtr kabinowy to część eksploatacyjna wymieniana raz na rok. Jeśli nie pamiętasz, kiedy była '
                  'wymieniana ostatnio, zacznij od niej — to najtańszy element z całej listy.'),
            ('h2', '4. Sprzęgło sprężarki lub elektryka'),
            ('p', 'Jeżeli chłodzenie zniknęło nagle i całkowicie, przyczyna leży zwykle po stronie załączania '
                  'sprężarki. Może to być samo sprzęgło elektromagnetyczne, czujnik ciśnienia (który odcina sprężarkę, '
                  'gdy czynnika jest za mało — czyli wraca punkt pierwszy), przekaźnik albo bezpiecznik.'),
            ('p', 'Objaw, który to potwierdza: po włączeniu klimatyzacji nie słychać charakterystycznego kliknięcia '
                  'i obroty silnika nie zmieniają się ani o jotę.'),
            ('h2', '5. Zawór rozprężny lub sprężarka'),
            ('p', 'Najrzadsza i najdroższa grupa przyczyn. Zawór rozprężny, który przestał prawidłowo dławić, daje '
                  'objawy trudne do odróżnienia od niedoboru czynnika — rozstrzygają dopiero pomiary ciśnień po obu '
                  'stronach układu. Zużyta sprężarka nie wytwarza właściwego ciśnienia, nawet jeśli obraca się i wygląda '
                  'na sprawną.'),
            ('callout', ['Uwaga',
                         'Jeżeli po włączeniu klimatyzacji słychać metaliczny hałas z komory silnika, wyłącz ją '
                         'i nie używaj do czasu diagnostyki. Rozsypująca się sprężarka rozprowadza opiłki po całym '
                         'układzie — naprawa rośnie wtedy z jednego elementu do połowy instalacji.']),
            ('h2', 'Co sprawdzić samemu, zanim zadzwonisz'),
            ('ol', [
                'Czy dmuchawa działa na wszystkich biegach — jeśli nie, problem jest w wentylacji, nie w chłodzeniu.',
                'Czy po włączeniu A/C słychać kliknięcie sprzęgła i zmianę obrotów silnika.',
                'Jak wygląda skraplacz za kratką zderzaka.',
                'Kiedy ostatnio wymieniano filtr kabinowy.',
                'Czy chłodzenie pogarszało się stopniowo, czy zniknęło nagle — to najważniejsza informacja dla serwisu.',
            ]),
            ('p', 'Te pięć odpowiedzi wystarczy, żebyśmy przez telefon zawęzili przyczynę i przyjechali z właściwymi '
                  'częściami. Resztę pokazują manometry.'),
        ],
    },
    {
        'slug': 'nieprzyjemny-zapach-z-nawiewow',
        'title': 'Nieprzyjemny zapach z nawiewów — skąd się bierze i jak się go pozbyć',
        'seo_title': 'Zapach z nawiewów w aucie — jak go usunąć',
        'excerpt': 'Zapach wilgoci po uruchomieniu klimatyzacji to nie kwestia zapachowej choinki. '
                   'Wyjaśniamy, co rośnie na parowniku i dlaczego aerozole z półki nie pomagają.',
        'date': '2026-06-09',
        'date_pl': '9 czerwca 2026',
        'cat': 'Poradnik',
        'read': '5 min',
        'img': 'mobilny.jpg',
        'service': 'diagnostyka-i-konserwacja',
        'lead': 'Włączasz klimatyzację i przez pierwsze kilkanaście sekund w aucie czuć piwnicę. '
                'Potem zapach słabnie, więc łatwo go zignorować — i to jest błąd, bo przyczyna rośnie dalej.',
        'body': [
            ('h2', 'Co dzieje się na parowniku'),
            ('p', 'Parownik jest najzimniejszym elementem układu — pracuje w temperaturze bliskiej zera. Ciepłe '
                  'powietrze z kabiny, przechodząc przez jego lamele, oddaje wilgoć, która skrapla się na powierzchni. '
                  'W efekcie parownik jest praktycznie stale mokry, ciemny i ciepły po wyłączeniu silnika. Trudno '
                  'o lepsze warunki dla pleśni i bakterii.'),
            ('p', 'Zapach pojawia się przy pierwszym uruchomieniu nawiewu, bo strumień powietrza porywa wtedy '
                  'największą porcję zarodników i produktów rozkładu. Po chwili stężenie spada i nos się przyzwyczaja — '
                  'ale do kabiny trafiają one przez cały czas jazdy.'),
            ('h2', 'Dlaczego aerozole nie rozwiązują problemu'),
            ('p', 'Preparaty w sprayu rozpylane do kratek nawiewu maskują zapach zamiast usuwać jego źródło. Część '
                  'z nich w ogóle nie dociera do parownika, bo osadza się wcześniej w kanałach wentylacyjnych. Efekt '
                  'utrzymuje się kilka dni, po czym zapach wraca — bo osad na lamelach pozostał nietknięty.'),
            ('callout', ['W skrócie',
                         'Zapach nie bierze się z kanałów wentylacyjnych, tylko z powierzchni parownika. Środek, '
                         'który tam nie dociera, nie ma jak zadziałać.']),
            ('h2', 'Co faktycznie działa'),
            ('p', 'Ozonowanie. Ozon jest gazem, więc dociera wszędzie tam, gdzie dociera powietrze — także na '
                  'powierzchnię parownika i w głąb kanałów. Utlenia materię organiczną, na której osadzają się '
                  'drobnoustroje, i nie zostawia po sobie zapachu ani osadu. Zabieg wykonuje się przy uruchomionej '
                  'wentylacji w obiegu zamkniętym, żeby ozon przeszedł przez cały układ.'),
            ('p', 'Drugi obowiązkowy element to wymiana filtra kabinowego. Zostawienie starego filtra po ozonowaniu '
                  'jest jak wyczyszczenie mieszkania i wstawienie z powrotem pełnego worka ze śmieci — zarodniki '
                  'osadzone na filtrze wrócą do obiegu przy pierwszym uruchomieniu nawiewu.'),
            ('h2', 'Jak zapobiegać'),
            ('ul', [
                'Wyłącz klimatyzację na kilka minut przed końcem jazdy, zostawiając samą dmuchawę — parownik zdąży '
                'wtedy obeschnąć.',
                'Używaj klimatyzacji także zimą, choćby raz na dwa tygodnie — pracująca sprężarka utrzymuje smarowanie, '
                'a osuszone powietrze ogranicza wilgoć w kabinie.',
                'Wymieniaj filtr kabinowy raz na rok, a jeśli jeździsz dużo w mieście — częściej.',
                'Nie parkuj stale pod drzewami; liście w komorze wlotu powietrza to dodatkowa materia organiczna '
                'tuż przed parownikiem.',
            ]),
            ('h2', 'Kiedy zapach oznacza coś więcej'),
            ('p', 'Jeśli obok zapachu pojawia się mokra wykładzina po stronie pasażera, przyczyną jest zatkany odpływ '
                  'skroplin — woda, która powinna wypływać pod auto, zbiera się wewnątrz. To osobna usterka, tania '
                  'w naprawie, ale kosztowna, jeśli woda dobierze się do modułów elektroniki pod dywanikiem.'),
            ('p', 'Zapach słodkawy, przypominający syrop, to z kolei sygnał wycieku płynu chłodniczego z nagrzewnicy. '
                  'Nie ma związku z klimatyzacją, ale wymaga reakcji.'),
        ],
    },
]

# Placeholder cards on the blog index — the theme will not render these.
UPCOMING = [
    'Retrofitting klimatyzacji na R12 — czy to się opłaca?',
    'Klimatyzacja zimą: dlaczego warto ją włączać',
    'Auto służbowe: jak zaplanować serwis floty',
]

POST_BY_SLUG = {p['slug']: p for p in POSTS}
