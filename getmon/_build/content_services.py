# -*- coding: utf-8 -*-
"""Content of every GETMON sub-page.

Text is taken 1:1 from getmon.pl (scraped 2026-09-20). Slugs match the live
site so this can replace it without breaking a single indexed URL.

Each entry:
  group     nav group the page belongs to (klimatyzacja / wentylacja / pompy /
            monitoring / alarmy) -> drives the header dropdown highlight
  nav       label in the dropdown
  title     <title>
  desc      meta description
  eyebrow   small caps label above the H1
  h1        hero headline
  lead      hero paragraph
  bg        assets/img/bg/<bg>.jpg behind the hero
  ticks     3-4 short lines under the lead (optional)
  chip      which chip the hero form preselects
  blocks    body; every block is a dict:
              {'h2': ..., 'p': [...], 'ul': [...], 'img': 'bg/name', 'cap': ...}
            'callout' renders the blue "W skrócie" box.
  related   slugs shown in "Sprawdź również"
"""

SERVICES = {

# ---------------------------------------------------------- klimatyzacja ----

'klimatyzacja-wroclaw': {
  'group': 'klimatyzacja', 'nav': 'Klimatyzacja Wrocław', 'chip': 'Klimatyzacja',
  'title': 'Klimatyzacja Wrocław — montaż i serwis | GETMON',
  'desc': 'Montaż klimatyzacji we Wrocławiu i okolicach. Split, multisplit, kanałowa, '
          'kasetonowa. Dobór urządzenia, montaż, przegląd i serwis. Darmowa wycena.',
  'eyebrow': 'KLIMATYZACJA', 'bg': 'klimatyzacja',
  'h1': 'Klimatyzacja we Wrocławiu — od doboru po serwis',
  'lead': 'Nie musisz wiedzieć, czy potrzebujesz splita, multisplita czy kasetonu. Powiedz, jakie masz pomieszczenia i czego od nich oczekujesz — dobierzemy urządzenie, zamontujemy je zgodnie z wymaganiami producenta i zostaniemy z Tobą na czas przeglądów.',
    'ticks': ['Darmowa wycena — koszt znasz przed rozpoczęciem prac', 'Dobór mocy do metrażu i przeznaczenia pomieszczenia', 'Montaż przez ekipę z certyfikatami i uprawnieniami', 'Przegląd i serwis po montażu — nie znikamy po odbiorze'],
  'blocks': [
    {'p': ['Jeśli nie wiesz, czy potrzebujesz klimatyzacji kasetonowej, split czy multisplit — '
           'zapraszamy do kontaktu. Mamy wieloletnie doświadczenie w tym temacie i na pewno nasi '
           'eksperci pomogą Ci wybrać klimatyzację idealną do Twojego biura czy mieszkania.']},
    {'h2': 'Na co zwrócić uwagę, wybierając klimatyzację?',
     'img': 'klimatyzacja-2', 'cap': 'Klimatyzacja ścienna w pomieszczeniu biurowym',
     'p': ['Cieplejsze pory roku to czas, kiedy trudno wyobrazić sobie funkcjonowanie bez dobrze '
           'działającej klimatyzacji. Urządzenia zapewniające odpowiednią temperaturę oraz wilgotność '
           'znajdują powszechne zastosowanie w samochodach i pojazdach transportu publicznego, prywatnych '
           'mieszkaniach, sklepach lub innych lokalach usługowych, a także we wszelkiego rodzaju miejscach '
           'pracy, gdzie klimatyzacja tworzy warunki sprzyjające wykonywaniu obowiązków. W wielu zakładach '
           'czy fabrykach urządzenia tego typu są potrzebne także do zapewnienia odpowiedniej temperatury '
           'dla procesów produkcyjnych oraz poprawnego działania maszyn i komputerów.',
           'Wybierając klimatyzację, należy kierować się takimi czynnikami, jak wielkość czy przeznaczenie '
           'pomieszczenia, aby dobrać urządzenie, które w takich warunkach sprawdzi się najlepiej. '
           'Konsekwencją właściwej decyzji będzie wysoka efektywność oraz zadowolenie użytkowników. '
           'Do najbardziej istotnych parametrów klimatyzatorów zalicza się: moc, poziom hałasu, zużycie '
           'prądu, sposób montażu. Warto też zwrócić uwagę, czy dane urządzenie posiada jedynie funkcję '
           'ochładzania, czy także dogrzewania. Profesjonalne klimatyzatory zapewniają podwójne działanie.']},
    {'h2': 'Dlaczego nie warto montować klimatyzacji samodzielnie?',
     'img': 'serwis', 'cap': 'Montaż jednostki wewnętrznej — realizacja GETMON',
     'p': ['Instalacja złożonych systemów klimatyzacji to zadanie wymagające pewnej wiedzy oraz '
           'doświadczenia. Niewłaściwe umieszczenie jednostki wewnętrznej lub zewnętrznej, albo '
           'nieodpowiednio wykonany odpływ powietrza i wilgoci, to tylko niektóre z najczęściej '
           'popełnianych błędów podczas samodzielnego montażu klimatyzacji. Rezultaty takich działań '
           'to przede wszystkim ryzyko częstych awarii, a nawet utrata gwarancji.',
           'Najpewniejsze rozwiązanie, aby uniknąć takich niepożądanych efektów, to zatrudnienie '
           'specjalistów, posiadających niezbędne certyfikaty oraz uprawnienia. We Wrocławiu i okolicach '
           'montaż klimatyzacji mogą Państwo zlecić doświadczonej firmie GETMON. Nasze kompetencje w tej '
           'dziedzinie potwierdzają odpowiednie dokumenty, będące gwarancją bezpiecznego oraz sprawnego '
           'wykonania wszystkich prac związanych z instalacją klimatyzatorów. Oprócz montażu klimatyzacji '
           'zakres naszych usług obejmuje przegląd, a także serwis klimatyzatorów każdego rodzaju.']},
    {'callout': ['W skrócie',
                 'Dobieramy urządzenie do metrażu i przeznaczenia pomieszczenia, wykonujemy montaż '
                 'zgodnie z wymaganiami producenta i zostajemy z Tobą na czas przeglądów i serwisu.']},
  ],
  'related': ['klimatyzacja-scienna-split-wroclaw', 'klimatyzacja-multi-split-wroclaw',
              'klimatyzacja-kanalowa-wroclaw', 'rodzaje-klimatyzacji'],
},

'klimatyzacja-scienna-split-wroclaw': {
  'group': 'klimatyzacja', 'nav': 'Ścienna (split)', 'chip': 'Klimatyzacja',
  'title': 'Klimatyzacja ścienna split Wrocław — montaż | GETMON',
  'desc': 'Klimatyzatory ścienne typu split — montaż we Wrocławiu. Doradztwo, dobór modelu, '
          'instalacja, serwis i konserwacja. Darmowa wycena: 884 884 823.',
  'eyebrow': 'KLIMATYZACJA', 'bg': 'klimatyzacja',
  'h1': 'Klimatyzacja ścienna split — najczęstszy wybór do mieszkań',
  'lead': 'Jeśli chcesz schłodzić pomieszczenie bez remontu i bez hałasu, split jest rozwiązaniem, po które sięga większość naszych klientów. Doradzimy model, zamontujemy i zajmiemy się serwisem.',
    'ticks': ['Cicha praca — hałaśliwa jednostka zostaje na zewnątrz', 'Chłodzi latem, dogrzewa w miesiącach przejściowych', 'Niewielkie wymiary — nie dominuje we wnętrzu', 'Doradztwo, dobór modelu, montaż, serwis i konserwacja'],
  'blocks': [
    {'p': ['System składa się z dwóch jednostek — wewnętrznej (montowanej na ścianie) i zewnętrznej '
           '— co zapewnia efektywną pracę przy minimalnym hałasie w pomieszczeniu.']},
    {'h2': 'Co dostajesz w ramach montażu?',
     'img': 'klimatyzacja-2', 'cap': 'Jednostka ścienna w salonie',
     'p': ['Oferujemy kompleksową usługę montażu klimatyzatorów split — od doradztwa i doboru '
           'odpowiedniego modelu, przez instalację, aż po serwis i konserwację.',
           'Zadbaj o komfort termiczny przez cały rok — sprawnie, estetycznie i w pełni dopasowane '
           'do Twoich potrzeb.']},
    {'h2': 'Do jakich wnętrz pasuje split?',
     'p': ['Klimatyzatory ścienne zaliczają się do urządzeń typu split. Jak sama nazwa wskazuje, '
           'montuje się je na ścianie (jednostka zewnętrzna i wewnętrzna są po różnych stronach). '
           'W związku z tym montaż klimatyzatorów ściennych jest relatywnie prosty i mało czasochłonny. '
           'Klimatyzację ścienną najczęściej montuje się w niewielkich pomieszczeniach — biurowych, '
           'jak i domowych — a także w lokalach handlowo-usługowych.',
           'Jednym z największych plusów klimatyzatorów ściennych są ich niewielkie wymiary. Dla wielu '
           'osób jest to ważne ze względu na estetykę wnętrza. Wybierając klimatyzator ścienny, warto '
           'zwrócić uwagę na ewentualne dodatkowe funkcje urządzenia, jakimi są chociażby jonizator '
           'czy filtry, tak istotne w kontekście alergików.']},
  ],
  'related': ['klimatyzacja-wroclaw', 'klimatyzacja-multi-split-wroclaw', 'rodzaje-klimatyzacji'],
},

'klimatyzacja-multi-split-wroclaw': {
  'group': 'klimatyzacja', 'nav': 'Multi Split', 'chip': 'Klimatyzacja',
  'title': 'Klimatyzacja multi split Wrocław — montaż | GETMON',
  'desc': 'Klimatyzacja multi split we Wrocławiu — jedna jednostka zewnętrzna, kilka pomieszczeń. '
          'Bezpłatna konsultacja i wycena. GETMON, tel. 884 884 823.',
  'eyebrow': 'KLIMATYZACJA', 'bg': 'multisplit',
  'h1': 'Multi split — kilka pomieszczeń, jedna jednostka na elewacji',
  'lead': 'Chcesz klimatyzację w salonie i dwóch sypialniach, ale nie chcesz trzech agregatów na ścianie budynku? Multi split podłącza nawet pięć jednostek wewnętrznych do jednego urządzenia zewnętrznego — taniej i z mniejszą ingerencją w elewację.',
    'ticks': ['Jeden agregat zamiast kilku — niższy koszt i mniej miejsca', 'Każdy pokój ustawia temperaturę niezależnie', 'Cicha praca — sprawdza się w sypialni i biurze', 'Bezpłatna konsultacja przed wyborem zestawu'],
  'blocks': [
    {'h2': 'Jak działa system multi split?',
     'img': 'multisplit', 'cap': 'System multi split — jednostki wewnętrzne',
     'p': ['Klimatyzatory typu multi split to rodzaj klimatyzatorów wykorzystujących wiele parowników '
           'i sprężarek do chłodzenia wielu pomieszczeń lub obszarów. Zaletą systemu multi split '
           'w porównaniu z systemem pojedynczym jest to, że pozwala on na indywidualną regulację '
           'temperatury w każdym pomieszczeniu lub obszarze.',
           'Systemy typu multi split mogą być również bardziej energooszczędne niż systemy typu single '
           'split, ponieważ wymagają one jedynie pracy sprężarki i parownika, które aktywnie chłodzą dany '
           'obszar. Ponadto systemy multi split są zazwyczaj cichsze niż systemy single split, dzięki '
           'czemu idealnie nadają się do stosowania w sypialniach lub innych cichych pomieszczeniach.']},
    {'h2': 'Kiedy multi split wygrywa z kilkoma splitami?',
     'p': ['Klimatyzatory split doskonale sprawdzają się w przypadku pojedynczego pomieszczenia. '
           'Co jednak zrobić w przypadku, gdy chcemy korzystać z klimatyzacji w całym mieszkaniu lub '
           'biurze? Czy w każdym pokoju trzeba instalować osobne urządzenia? Na szczęście istnieje '
           'nieco tańsze rozwiązanie, znane jako multi split. W tym przypadku wystarczy tylko jedna '
           'jednostka zewnętrzna, do której można podłączyć kilka urządzeń wewnętrznych. Ich liczba '
           'zależy od modelu. Najczęściej pojedynczy agregat chłodzący może obsługiwać do pięciu '
           'pomieszczeń.',
           'Warto wiedzieć, że każdy z podłączonych w ten sposób klimatyzatorów ściennych będzie '
           'działał niezależnie od pozostałych. Istnieje możliwość indywidualnej regulacji temperatury '
           'do potrzeb osób znajdujących się w poszczególnych pokojach. Klimatyzacja multi split '
           'sprawdzi się zatem wszędzie tam, gdzie istnieje potrzeba instalacji kilku klimatyzatorów, '
           'a mniejsza liczba urządzeń zewnętrznych pozwoli zmniejszyć koszty oraz oszczędzić miejsce.']},
  ],
  'related': ['klimatyzacja-scienna-split-wroclaw', 'klimatyzacja-wroclaw', 'rodzaje-klimatyzacji'],
},

'klimatyzacja-kanalowa-wroclaw': {
  'group': 'klimatyzacja', 'nav': 'Kanałowa', 'chip': 'Klimatyzacja',
  'title': 'Klimatyzacja kanałowa Wrocław — montaż | GETMON',
  'desc': 'Klimatyzacja kanałowa we Wrocławiu — montaż w biurach, mieszkaniach i obiektach. '
          'Bezpłatna konsultacja. GETMON, tel. 884 884 823.',
  'eyebrow': 'KLIMATYZACJA', 'bg': 'kanalowa',
  'h1': 'Klimatyzacja kanałowa — komfort, którego nie widać',
  'lead': 'W pokojach zostają tylko dyskretne kratki nawiewne — całą instalację chowamy w suficie. Rozwiązanie dla większych domów, biur i lokali, gdzie estetyka wnętrza jest równie ważna jak temperatura.',
    'ticks': ['We wnętrzu widać wyłącznie kratki nawiewne', 'Równomierna temperatura, bez gorących punktów', 'Kanały prostokątne lub okrągłe — do niemal każdego budynku', 'Najtaniej na etapie projektu lub remontu — doradzimy kiedy'],
  'blocks': [
    {'h2': 'Dlaczego dobór kanałów decyduje o rachunkach?',
     'img': 'kanalowa', 'cap': 'Kanały wentylacyjne instalacji klimatyzacji',
     'p': ['Kanały wentylacyjne są podstawowym elementem każdego systemu klimatyzacji i odgrywają '
           'kluczową rolę w rozprowadzaniu chłodnego powietrza w całym domu lub biurze. Kanały to system '
           'połączonych rur, które transportują czynnik chłodniczy z jednostki klimatyzacyjnej do różnych '
           'pomieszczeń w budynku.',
           'Aby przewody działały prawidłowo, muszą być odpowiednio zwymiarowane i zainstalowane. '
           'W przeciwnym razie urządzenie klimatyzacyjne nie będzie w stanie dostarczyć wystarczającej '
           'mocy chłodniczej do pomieszczeń, a w przestrzeni będzie panował dyskomfort. Ponadto źle '
           'dobrane kanały mogą powodować wysokie rachunki za energię, ponieważ urządzenie klimatyzacyjne '
           'będzie musiało pracować ciężej, aby schłodzić pomieszczenie.']},
    {'h2': 'Kiedy najlepiej zaplanować instalację kanałową?',
     'img': 'wentylacja', 'cap': 'Rozprowadzenie kanałów w stropie',
     'p': ['Klimatyzacja kanałowa stanowi złożony system rur połączonych ze sobą, które są rozprowadzone '
           'po powierzchni całego schładzanego budynku. Elementy instalacji klimatyzacyjnej przechodzą '
           'zarówno przez ściany, jak i przez strop w zależności od rodzaju projektu. Nowoczesne '
           'rozwiązania technologiczne pozwalają na zastosowanie kanałów prostokątnych lub okrągłych, '
           'dzięki czemu łatwo zainstalować klimatyzację praktycznie w dowolnym budynku.',
           'Aby poprawnie zamontować klimatyzację kanałową, najpierw należy wykonać odpowiednie '
           'przepusty. Dlatego też o takich rozwiązaniach powinno się myśleć jeszcze na etapie '
           'projektowania budynku, co pozwoli zaoszczędzić na późniejszych pracach remontowych. Montaż '
           'klimatyzacji kanałowej w gotowym budynku jest naturalnie możliwy, ale wymaga większego '
           'nakładu czasu oraz kosztów. Należy pamiętać, że urządzenie sterujące, które odpowiada za '
           'chłodzenie, musi zostać umieszczone w osobnym pomieszczeniu.']},
  ],
  'related': ['klimatyzacja-kasetonowa-wroclaw', 'klimatyzacja-wroclaw', 'wentylacja-wroclaw'],
},

'klimatyzacja-kasetonowa-wroclaw': {
  'group': 'klimatyzacja', 'nav': 'Kasetonowa', 'chip': 'Klimatyzacja',
  'title': 'Klimatyzacja kasetonowa Wrocław — montaż | GETMON',
  'desc': 'Klimatyzatory kasetonowe montowane w suficie podwieszanym — Wrocław i okolice. '
          'Dobór jednostki, montaż i serwis. GETMON, tel. 884 884 823.',
  'eyebrow': 'KLIMATYZACJA', 'bg': 'kasetonowa',
  'h1': 'Klimatyzacja kasetonowa — chłodzi równomiernie, nie rzuca się w oczy',
  'lead': 'Montowana w suficie podwieszanym, widoczna tylko jako kratka. Rozprowadza powietrze nawet w czterech kierunkach, więc sprawdza się w biurach, salonach i lokalach usługowych o większej powierzchni.',
    'ticks': ['Widoczna tylko kratka — reszta ukryta w suficie', 'Nawiew jedno-, dwu- lub czterokierunkowy', 'Chłodzi, ogrzewa i — z filtrem — oczyszcza powietrze', 'Technicy dobiorą jednostkę do rozstawu stelaża'],
  'blocks': [
    {'p': ['Dzięki wieloletniemu doświadczeniu jesteśmy pewni, że możemy zapewnić Ci najlepszą możliwą '
           'obsługę. Jeśli więc szukasz niezawodnej firmy, która zainstaluje Twój klimatyzator — '
           'jesteśmy idealnym wyborem.']},
    {'h2': 'Dlaczego klienci wybierają kaseton?',
     'img': 'kasetonowa', 'cap': 'Jednostka kasetonowa w suficie podwieszanym',
     'p': ['Jednym z najpopularniejszych typów klimatyzatorów jest klimatyzator kasetonowy. Jak sama '
           'nazwa wskazuje, ten typ klimatyzatora jest przeznaczony do montażu w kasecie lub wnęce '
           'w suficie. Klimatyzatory kasetonowe to dobry wybór z wielu powodów. Po pierwsze, są bardzo '
           'dyskretne, ponieważ po zainstalowaniu urządzenia widoczna jest tylko kratka. Po drugie, są '
           'bardzo skuteczne w chłodzeniu pomieszczeń, ponieważ urządzenie można umieścić bezpośrednio '
           'nad obszarem, który wymaga chłodzenia. Wreszcie, są one stosunkowo łatwe w instalacji '
           'i konserwacji.']},
    {'h2': 'Jak to jest zbudowane i montowane?',
     'p': ['W przeważającej większości klimatyzatory kasetonowe są urządzeniami typu split — oznacza to, '
           'że ich konstrukcja zakłada istnienie dwóch jednostek: zewnętrznej (skraplającej) oraz '
           'wewnętrznej (w formie parownika). Na rynku dostępne są także klimatyzatory pozwalające na '
           'przepływ powietrza prosto do pomieszczenia, które sąsiaduje z pomieszczeniem klimatyzowanym.',
           'Klimatyzacja kasetonowa zarówno chłodzi, jak i ogrzewa powietrze w pomieszczeniach. '
           'Po wyposażeniu urządzeń w specjalne filtry są one w stanie także oczyszczać powietrze we '
           'wnętrzach. Tego typu rozwiązanie jest niezwykle wydajne, a przy tym energooszczędne. Można je '
           'bez problemu wyposażyć w nawiew jedno-, dwu-, a także czterokierunkowy. Ostatni rodzaj '
           'umożliwia najbardziej równomierne rozprowadzanie powietrza w pomieszczeniu.',
           'Charakterystyczną cechą klimatyzacji kasetonowej jest metoda jej montażu. Jednostka '
           'znajdująca się wewnątrz pomieszczenia instalowana jest w suficie podwieszanym, a jej forma '
           'oraz wymiary należy dostosować do rozstawu stelaża używanego w tego typu zabudowach.']},
  ],
  'related': ['klimatyzacja-kanalowa-wroclaw', 'klimatyzacja-wroclaw', 'rodzaje-klimatyzacji'],
},

'klimatyzacja-przypodlogowo-podsufitowa-wroclaw': {
  'group': 'klimatyzacja', 'nav': 'Przypodłogowo-podsufitowa', 'chip': 'Klimatyzacja',
  'title': 'Klimatyzacja przypodłogowo-podsufitowa Wrocław | GETMON',
  'desc': 'Klimatyzacja przypodłogowo-podsufitowa we Wrocławiu — do restauracji, banków, sklepów '
          'i dużych przestrzeni. Bezpłatna konsultacja: 884 884 823.',
  'eyebrow': 'KLIMATYZACJA', 'bg': 'przypodlogowa',
  'h1': 'Klimatyzacja przypodłogowo-podsufitowa — do dużych przestrzeni',
  'lead': 'Restauracja, bank, salon czy sklep wielkopowierzchniowy? Ten typ zamontujesz tam, gdzie akurat jest miejsce — przy podłodze albo pod sufitem — a powietrze i tak rozchodzi się równomiernie.',
    'ticks': ['Montaż przy podłodze albo pod sufitem — pełna swoboda', 'Równomierny nawiew nawet w największe upały', 'Sterowanie pilotem, filtr antybakteryjny w wybranych modelach', 'Dyskretny montaż, który nie psuje aranżacji wnętrza'],
  'blocks': [
    {'h2': 'Co zyskujesz na tym rozwiązaniu?',
     'img': 'przypodlogowa', 'cap': 'Jednostka przypodłogowo-podsufitowa',
     'p': ['Korzyści płynące z zastosowania klimatyzacji od podłogi do sufitu są liczne. Nie tylko '
           'zapewnia ona stały dopływ chłodnego, świeżego powietrza, ale również pomaga poprawić jakość '
           'powietrza w pomieszczeniach poprzez jego cyrkulację i filtrowanie. Ponadto klimatyzacja '
           'przypodłogowa może pomóc w obniżeniu kosztów energii poprzez utrzymanie temperatury na '
           'stałym poziomie. Dzieje się tak, ponieważ chłodne powietrze jest równomiernie rozprowadzane '
           'w całej przestrzeni, zapobiegając powstawaniu gorących punktów.']},
    {'h2': 'Gdzie sprawdza się najlepiej?',
     'p': ['Klimatyzacja przypodłogowo-podsufitowa to nowoczesne rozwiązanie o uniwersalnym charakterze. '
           'Sprawdza się doskonale w przypadku potrzeby chłodzenia dość dużych przestrzeni, do których '
           'zaliczyć można restauracje, banki czy różnego rodzaju sklepy. Jak sama nazwa wskazuje, '
           'urządzenia można z łatwością zamontować zarówno przy podłodze, jak i pod sufitem. To z kolei '
           'wpływa na oszczędność przestrzeni, a przy tym poprawia funkcjonalność całego systemu.',
           'Długa instalacja chłodnicza pozwala na zamontowanie urządzenia praktycznie w dowolnie '
           'wybranym w budynku miejscu. Dyskretny montaż nie zaburza w żaden sposób designu wnętrza '
           'i pozwala na swobodną aranżację przestrzeni. Tego typu klimatyzatory sterowane są za pomocą '
           'pilota, co pozwala na szybką i wygodną regulację temperatury z odległości. Zastosowanie '
           'specjalnego filtra antybakteryjnego pozwala na oczyszczanie powietrza z nieprzyjaznych '
           'zdrowiu drobnoustrojów.']},
  ],
  'related': ['klimatyzacja-kasetonowa-wroclaw', 'klimatyzacja-wroclaw', 'rodzaje-klimatyzacji'],
},

'klimatyzacja-przenosna-wroclaw': {
  'group': 'klimatyzacja', 'nav': 'Przenośna', 'chip': 'Klimatyzacja',
  'title': 'Klimatyzacja przenośna Wrocław | GETMON',
  'desc': 'Klimatyzacja przenośna we Wrocławiu — jak działa, czy warto i na co uważać przy '
          'rurze wywiewnej. Bezpłatna konsultacja GETMON: 884 884 823.',
  'eyebrow': 'KLIMATYZACJA', 'bg': 'przenosna',
  'h1': 'Klimatyzacja przenośna — chłód bez stałej instalacji',
  'lead': 'Wynajmujesz mieszkanie albo nie możesz powiesić jednostki na elewacji? Klimatyzator przenośny przestawisz z pokoju do pokoju. Zanim go kupisz, warto wiedzieć, jak wyprowadzić rurę wywiewną, żeby nie stracić wydajności.',
    'ticks': ['Bez stałej instalacji i bez ingerencji w elewację', 'Przenosisz z pokoju do pokoju, chowasz po sezonie', 'Doradzimy, jak poprowadzić rurę wywiewną', 'Uczciwie powiemy, kiedy lepszy będzie split'],
  'blocks': [
    {'h2': 'Jak działa klimatyzator przenośny?',
     'img': 'przenosna', 'cap': 'Klimatyzator przenośny w pomieszczeniu',
     'p': ['Przenośna klimatyzacja może być doskonałym sposobem na zapewnienie chłodu w domu podczas '
           'gorących miesięcy letnich. W przeciwieństwie do jednostek okiennych klimatyzatory przenośne '
           'można łatwo przenosić z pokoju do pokoju i nie wymagają one żadnej stałej instalacji. '
           'Dodatkowo klimatyzatory przenośne są znacznie bardziej energooszczędne niż centralne systemy '
           'klimatyzacji, co czyni je doskonałym wyborem dla każdego, kto chce zaoszczędzić na rachunkach '
           'za energię. Klimatyzatory przenośne są również stosunkowo ciche.']},
    {'h2': 'Wady, o których warto wiedzieć przed zakupem',
     'p': ['Każdy rodzaj klimatyzacji działa na podobnej zasadzie — w instalacji umieszczany jest '
           'specjalny czynnik, którego krążenie schładza masy powietrza. Klimatyzacja przenośna nie jest '
           'tutaj wyjątkiem. Warto jednak pamiętać, że jednostka klimatyzacyjna montowana na stałe na '
           'ścianie potrzebuje rury, którą odprowadza zużyte masy powietrza poza budynek. W przypadku '
           'klimatyzacji mobilnej mamy do czynienia z rurą wywiewną.',
           'Urządzenia przenośne z reguły wyglądają jak walizki na kółkach. Można je bez problemu '
           'ustawić w dowolnym miejscu. Występujące w nich rury wywiewne z reguły mają średnicę '
           '15 centymetrów i należy je wyprowadzić na zewnątrz. Optymalnym rozwiązaniem jest ich '
           'połączenie z istniejącym kominowym przewodem instalacyjnym. Warto jednak mieć na uwadze, '
           'że jednostka pobiera powietrze z wnętrza pomieszczenia, więc może powstać podciśnienie, '
           'które zaburzy cały ciąg wentylacyjny. Dlatego też częstym zabiegiem jest wypuszczenie rury '
           'przez okno, co jednak wpływa bezpośrednio na spadek wydajności klimatyzacji.']},
  ],
  'related': ['klimatyzacja-scienna-split-wroclaw', 'rodzaje-klimatyzacji', 'klimatyzacja-wroclaw'],
},

'rodzaje-klimatyzacji': {
  'group': 'klimatyzacja', 'nav': 'Rodzaje klimatyzacji', 'chip': 'Klimatyzacja',
  'title': 'Rodzaje klimatyzacji — czym się różnią | GETMON Wrocław',
  'desc': 'Monoblock, split, multi split, ścienna, kasetonowa, kanałowa, przenośna — '
          'poznaj rodzaje klimatyzacji i wybierz najlepszy dla swojego domu lub firmy.',
  'eyebrow': 'PORADNIK', 'bg': 'rodzaje',
  'h1': 'Rodzaje klimatyzacji — który typ pasuje do Twojego wnętrza?',
  'lead': 'Split, multi split, kaseton czy kanałówka? Różnią się budową i sposobem montażu, a od tego zależy koszt, estetyka i liczba pomieszczeń, które schłodzisz. Poniżej krótki przewodnik — a jeśli wolisz od razu konkret, zadzwoń po darmową wycenę.',
    'ticks': ['Ze względu na budowę: monoblock, split, multi split', 'Ze względu na montaż: ścienna, kasetonowa, kanałowa, przypodłogowa, przenośna', 'Pomożemy dobrać typ do metrażu i przeznaczenia pomieszczenia'],
  'blocks': [
    {'h2': 'Podział ze względu na budowę',
     'p': ['Klimatyzatory dzielimy ze względu na ilość jednostek zewnętrznych. Mogą posiadać jeden moduł '
           '(wtedy mówimy o klimatyzatorach typu monoblock) lub kilka modułów (klimatyzatory typu split '
           'lub multi split).'],
     'h3': [('Klimatyzatory typu split',
             ['Klimatyzatory split to jedne z najczęściej montowanych urządzeń klimatyzacyjnych. Ich '
              'popularność nie bierze się znikąd — są ciche (z uwagi na fakt, że jednostka wytwarzająca '
              'hałas nie znajduje się w klimatyzowanym pomieszczeniu), estetyczne i mają również funkcję '
              'grzania.',
              'Składają się z jednej jednostki zewnętrznej i jednej jednostki wewnętrznej. Obie jednostki '
              'łączy tzw. linia freonowa (chłodnicza). Jest to nic innego jak dwie rury miedziane, dzięki '
              'którym istnieje swobodny przepływ chłodzenia. Klimatyzatory split najlepiej sprawdzają się '
              'do chłodzenia pojedynczego pomieszczenia.']),
            ('Klimatyzatory typu multi split',
             ['Klimatyzatory typu multi split są zbudowane analogicznie do klimatyzatorów typu split. '
              'Tym, co je wyróżnia, jest natomiast to, że do jednej jednostki zewnętrznej podłączonych '
              'może być wiele jednostek wewnętrznych. System multi split dzięki temu pozwala na regulację '
              'temperatury osobno dla każdego pomieszczenia, co jest jego olbrzymią zaletą.'])]},
    {'ul': ['energooszczędność',
            'cicha praca — system multi split jest wykorzystywany nawet w sypialni czy biurze',
            'uniwersalność — idealnie sprawdzi się do chłodzenia całego mieszkania lub biura']},
    {'h2': 'Podział ze względu na sposób montażu',
     'img': 'klimatyzacja-2', 'cap': 'Różne typy jednostek wewnętrznych',
     'p': ['Systemy klimatyzacyjne różnią się również w zależności od rodzaju ich montażu. Klimatyzatory '
           'ścienne, kasetonowe, kanałowe, a może podsufitowe lub przypodłogowe — które z nich wybrać?'],
     'h3': [('Klimatyzatory ścienne',
             ['Klimatyzatory ścienne zaliczają się do urządzeń typu split. Montuje się je na ścianie, '
              'przez co montaż jest relatywnie prosty i mało czasochłonny. Klimatyzację ścienną najczęściej '
              'montuje się w niewielkich pomieszczeniach biurowych i domowych, a także w lokalach '
              'handlowo-usługowych. Jednym z największych plusów są niewielkie wymiary urządzenia.']),
            ('Klimatyzatory przypodłogowo-podsufitowe',
             ['Klimatyzacja przypodłogowo-sufitowa jest nowoczesnym rozwiązaniem, szeroko wykorzystywanym '
              'w przypadku dużych przestrzeni, takich jak sklepy wielkopowierzchniowe, restauracje, banki '
              'czy urzędy. Klimatyzatory tego typu można montować zarówno przy podłodze, jak i pod '
              'sufitem — są więc bardzo uniwersalne.'])]},
  ],
  'related': ['klimatyzacja-scienna-split-wroclaw', 'klimatyzacja-multi-split-wroclaw',
              'klimatyzacja-kasetonowa-wroclaw', 'klimatyzacja-kanalowa-wroclaw'],
},

# ------------------------------------------------------------- wentylacja ---

'wentylacja-wroclaw': {
  'group': 'wentylacja', 'nav': 'Wentylacja Wrocław', 'chip': 'Wentylacja',
  'title': 'Wentylacja i rekuperacja Wrocław — montaż | GETMON',
  'desc': 'Projektowanie i montaż wentylacji oraz rekuperacji we Wrocławiu — domy, biura, '
          'restauracje i lokale usługowe. Od projektu po uruchomienie. Tel. 884 884 823.',
  'eyebrow': 'WENTYLACJA', 'bg': 'wentylacja',
  'h1': 'Wentylacja i rekuperacja — świeże powietrze bez otwierania okien',
  'lead': 'Rekuperacja odzyskuje ciepło, które w tradycyjnej wentylacji ucieka przez kratki. Efekt: niższe rachunki za ogrzewanie, przefiltrowane powietrze i mniejsze ryzyko wilgoci na ścianach. Projektujemy i montujemy w domach, biurach i lokalach usługowych.',
    'ticks': ['Odzysk ciepła zamiast strat przez kratki wentylacyjne', 'Filtry zatrzymują kurz i pyłki — ważne dla alergików', 'Domy jednorodzinne, biura, restauracje i salony', 'Projekt, montaż, uruchomienie, regulacja, serwis i gwarancja'],
  'blocks': [
    {'h2': 'Wentylacja czy rekuperacja — czym się różnią?',
     'img': 'wentylacja', 'cap': 'Instalacja kanałów wentylacyjnych',
     'p': ['Firma GETMON specjalizuje się w projektowaniu i montażu nowoczesnych systemów klimatyzacji, '
           'wentylacji oraz rekuperacji. W praktyce najczęściej stosowane rozwiązania w budynkach '
           'mieszkalnych dzielą się na dwa główne typy: wentylację tradycyjną oraz rekuperację, czyli '
           'wentylację mechaniczną z odzyskiem ciepła. Oba systemy odpowiadają za wymianę powietrza '
           'w budynku, jednak różnią się sposobem działania, efektywnością oraz komfortem użytkowania.'],
     'h3': [('Wentylacja — podstawowa wymiana powietrza w budynku',
             ['Wentylacja odpowiada za usuwanie zużytego powietrza z pomieszczeń i dostarczanie świeżego '
              'z zewnątrz. W starszych budynkach najczęściej stosowana jest wentylacja grawitacyjna, '
              'działająca w oparciu o naturalne różnice temperatur i ciśnienia. W nowoczesnych '
              'realizacjach coraz częściej stosuje się wentylację mechaniczną, która pozwala na większą '
              'kontrolę przepływu powietrza oraz stabilniejsze warunki w budynku.']),
            ('Rekuperacja — wentylacja z odzyskiem ciepła',
             ['Rekuperacja to nowoczesna forma wentylacji mechanicznej, która oprócz wymiany powietrza '
              'umożliwia także odzysk ciepła. W systemie rekuperacji zużyte powietrze jest usuwane '
              'z budynku, a świeże powietrze nawiewane z zewnątrz przechodzi przez wymiennik ciepła. '
              'Dzięki temu energia cieplna zostaje odzyskana i wykorzystana ponownie.'])]},
    {'ul': ['świeże i przefiltrowane powietrze w domu',
            'mniejsze straty ciepła',
            'niższe koszty ogrzewania',
            'wyższy komfort codziennego użytkowania']},
    {'h2': 'Co daje rekuperacja w domu jednorodzinnym?',
     'p': ['Rekuperacja to obecnie jedno z najczęściej wybieranych rozwiązań w nowoczesnym budownictwie '
           'jednorodzinnym. System ten, znany jako wentylacja mechaniczna z odzyskiem ciepła, zapewnia '
           'stałą wymianę powietrza w budynku przy jednoczesnym ograniczeniu strat energii. W praktyce '
           'oznacza to, że do wnętrza domu trafia świeże, przefiltrowane powietrze, a jednocześnie ciepło '
           'z powietrza usuwanego jest odzyskiwane i wykorzystywane ponownie.',
           'Dobrze zaprojektowany system rekuperacji pozwala utrzymać stałą jakość powietrza w całym domu '
           'bez konieczności otwierania okien. To szczególnie ważne w sezonie zimowym oraz w okresach '
           'podwyższonego smogu.']},
    {'ul': ['stały dopływ świeżego powietrza',
            'redukcja strat ciepła w budynku',
            'niższe rachunki za ogrzewanie',
            'ograniczenie wilgoci i ryzyka powstawania pleśni',
            'filtracja powietrza z kurzu i pyłków']},
    {'h2': 'Wentylacja w lokalu usługowym — komfort i wymogi sanitarne',
     'img': 'kanalowa', 'cap': 'Wentylacja w lokalu usługowym',
     'p': ['Systemy wentylacyjne w obiektach komercyjnych mają szczególne znaczenie, ponieważ muszą '
           'działać wydajnie przy dużym obciążeniu i intensywnej eksploatacji. Firma GETMON realizuje '
           'instalacje wentylacyjne w restauracjach i lokalach gastronomicznych, biurach oraz '
           'przestrzeniach pracy, salonach kosmetycznych i fryzjerskich, a także w sklepach i innych '
           'lokalach usługowych. W takich miejscach odpowiednia wentylacja zapewnia nie tylko komfort '
           'użytkowników, ale również spełnienie obowiązujących wymogów sanitarnych i technicznych.']},
    {'h2': 'Co bierzemy na siebie?',
     'p': ['Posiadamy duże doświadczenie w montażu systemów wentylacji i rekuperacji, dzięki czemu '
           'możemy oferować rozwiązania dopasowane zarówno do nowych inwestycji, jak i modernizacji '
           'istniejących budynków. Każdy projekt realizujemy indywidualnie, zaczynając od doboru '
           'optymalnego systemu wentylacji lub rekuperacji, przez profesjonalny montaż instalacji, aż po '
           'uruchomienie i regulację całego systemu. Zapewniamy również serwis oraz bieżącą obsługę '
           'urządzeń, a także gwarancję na wykonane instalacje.']},
    {'callout': ['Czytaj dalej',
                 'Więcej o tym, czy rekuperacja się opłaca i ile kosztuje, piszemy w artykule '
                 '„Czy warto montować rekuperację w domu?”.']},
  ],
  'related': ['klimatyzacja-kanalowa-wroclaw', 'pompy-ciepla-wroclaw', 'klimatyzacja-wroclaw'],
},

# ------------------------------------------------------------ pompy ciepla --

'pompy-ciepla-wroclaw': {
  'group': 'pompy', 'nav': 'Pompy ciepła Wrocław', 'chip': 'Pompa ciepła',
  'title': 'Pompy ciepła Wrocław — montaż i dobór | GETMON',
  'desc': 'Pompy ciepła powietrzne, gruntowe i powietrze-powietrze. Dobór, projekt, montaż '
          'i serwis we Wrocławiu. Pomoc w dotacjach „Czyste Powietrze”. Tel. 884 884 823.',
  'eyebrow': 'POMPY CIEPŁA', 'bg': 'pompy',
  'h1': 'Pompy ciepła — nawet o 70% niższe rachunki za ogrzewanie',
  'lead': 'Ciepło z powietrza, gruntu lub wody zamiast spalania paliw. Jedno urządzenie ogrzewa dom, chłodzi go latem i podgrzewa wodę użytkową. Pomożemy też dobrać model i przejść przez formalności dotacji „Czyste Powietrze”.',
    'ticks': ['Nawet o 70% niższe rachunki za ogrzewanie', 'Ogrzewanie, chłodzenie i ciepła woda z jednego urządzenia', 'Pomoc w uzyskaniu dotacji, np. „Czyste Powietrze”', 'Dobór, projekt, montaż i serwis u jednego wykonawcy'],
  'blocks': [
    {'h2': 'Co realnie zyskujesz na pompie ciepła?',
     'img': 'pompy', 'cap': 'Jednostka zewnętrzna pompy ciepła',
     'ul': ['Niskie koszty eksploatacji — nawet o 70% niższe rachunki za ogrzewanie',
            'Ekologiczne rozwiązanie — zero emisji spalin i CO₂',
            'Wielofunkcyjność — ogrzewanie, chłodzenie i podgrzewanie wody użytkowej',
            'Wysoki komfort użytkowania — cicha praca i pełna automatyzacja',
            'Dofinansowania i ulgi — pomoc w uzyskaniu dotacji (np. „Czyste Powietrze”)'],
     'p': ['Oferujemy kompleksową obsługę: dobór urządzenia, projekt, montaż i serwis. Korzystamy tylko '
           'ze sprawdzonych, renomowanych producentów, co daje Ci gwarancję jakości i niezawodności '
           'przez lata.']},
    {'h2': 'Którą pompę wybrać do swojego budynku?',
     'h3': [('1. Powietrzne pompy ciepła (powietrze–woda)',
             ['Najpopularniejszy i najszybszy w montażu system. Wykorzystuje energię zawartą w powietrzu '
              'zewnętrznym. Zalety: niskie koszty inwestycji, szybki montaż, działanie nawet przy −25°C, '
              'idealne do modernizacji i nowych budynków.',
              'Zastosowanie: ogrzewanie podłogowe, grzejniki niskotemperaturowe, klimakonwektory, '
              'przygotowanie c.w.u.']),
            ('2. Gruntowe pompy ciepła (solanka–woda)',
             ['Najbardziej stabilne i najwydajniejsze źródło ciepła. Energia pobierana jest z gruntu '
              'poprzez sondy pionowe lub kolektor poziomy. Zalety: najwyższa efektywność sezonowa (SCOP), '
              'bardzo niskie koszty eksploatacji, cicha praca, idealne dla dużych domów i budynków '
              'pasywnych.',
              'To inwestycja premium dla klientów oczekujących maksymalnej niezawodności oraz '
              'oszczędności przez wiele lat.']),
            ('3. Pompy ciepła powietrze–powietrze',
             ['Rozwiązanie oparte na technologii klimatyzatorów z funkcją grzania. Szybkie i tanie '
              'w instalacji. Zalety: najniższy koszt montażu, szybkie nagrzewanie pomieszczeń, możliwość '
              'chłodzenia latem, dobre rozwiązanie dla biur, mieszkań i małych domów.'])]},
  ],
  'related': ['klimatyzacja-wroclaw', 'wentylacja-wroclaw', 'klimatyzacja-kanalowa-wroclaw'],
},

# ------------------------------------------------------------- monitoring ---

'montaz-monitoringu-wroclaw': {
  'group': 'monitoring', 'nav': 'O monitoringu', 'chip': 'Monitoring',
  'title': 'Montaż monitoringu Wrocław — kamery CCTV | GETMON',
  'desc': 'Montaż monitoringu we Wrocławiu — projekt, rozmieszczenie kamer CCTV, rejestratory '
          'i zdalny podgląd. Dla firm i posesji prywatnych. Tel. 884 884 823.',
  'eyebrow': 'MONITORING', 'bg': 'monitoring',
  'h1': 'Montaż monitoringu we Wrocławiu — wiesz, co dzieje się u Ciebie',
  'lead': 'Kamery w kluczowych punktach, nagrania na dysku i podgląd z telefonu — z dowolnego miejsca. Zaprojektujemy rozmieszczenie pod Twój obiekt albo zamontujemy sprzęt, który już masz.',
    'ticks': ['Podgląd na telefonie z dowolnego miejsca', 'Nagrania na dysku — wiele godzin materiału', 'Kamery widoczne odstraszają, ukryte dokumentują', 'System od podstaw albo montaż Twoich urządzeń'],
  'blocks': [
    {'img': 'monitoring', 'cap': 'Kamery monitoringu na elewacji budynku',
     'p': ['Obraz zostaje przekazany do tak zwanej telewizji przemysłowej, obserwowanej samodzielnie, '
           'przez strażnika lub przez wybraną agencję ochrony.',
           'Obecnie coraz powszechniej stosuje się kamery rejestrujące obraz w wysokiej rozdzielczości, '
           'wyposażone w dysk twardy, na którym mieści się wiele godzin nagranego materiału, a także '
           'zapewniające zdalny podgląd obrazu za pomocą internetu. Najbardziej zaawansowane modele są '
           'w stanie umożliwić odczytanie numerów tablic rejestracyjnych nawet w nocy lub złych warunkach '
           'meteorologicznych.',
           'Montaż monitoringu na zewnątrz zwykle następuje w dobrze widocznych miejscach, aby odstraszyć '
           'potencjalnych włamywaczy lub wandali. Jeszcze lepszą ochronę zapewnia połączenie widocznych '
           'kamer z ukrytymi.']},
    {'h2': 'Gotowy zestaw czy system projektowany pod obiekt?',
     'p': ['Możliwy jest zakup gotowego systemu monitoringu lub wykonanie go na specjalne zamówienie. '
           'W pierwszym przypadku instalację należy przeprowadzić samodzielnie, a w przypadku bardziej '
           'zaawansowanych realizacji konieczne okazuje się wynajęcie profesjonalnej firmy. Warto '
           'skorzystać z pomocy doświadczonych specjalistów, którzy wiedzą najlepiej, jak skutecznie '
           'rozmieścić kamery do monitoringu, aby zapewnić maksimum bezpieczeństwa poprzez możliwie '
           'najlepszą funkcjonalność systemu.',
           'Jeśli są Państwo zainteresowani usługą montażu monitoringu — Wrocław i okolice to teren '
           'działalności firmy GETMON, specjalizującej się m.in. w tego typu realizacjach i posiadającej '
           'wieloletnią praktykę. Na Państwa życzenie możemy stworzyć system monitorowania od podstaw, '
           'według indywidualnych zaleceń, a także przeprowadzić sam montaż wcześniej zakupionych '
           'urządzeń rejestrujących.']},
    {'callout': ['Nie czekaj, aż będzie za późno',
                 'Chroń swój majątek — zadzwoń i umów bezpłatny przegląd obiektu pod kątem monitoringu.']},
  ],
  'related': ['montaz-monitoringu-cyfrowego-ip-wroclaw', 'montaz-monitoringu-analogowego-wroclaw',
              'systemy-alarmowe-wroclaw'],
},

'montaz-monitoringu-cyfrowego-ip-wroclaw': {
  'group': 'monitoring', 'nav': 'Cyfrowy IP', 'chip': 'Monitoring',
  'title': 'Monitoring IP Wrocław — montaż monitoringu cyfrowego | GETMON',
  'desc': 'Monitoring cyfrowy IP we Wrocławiu — HD, Full HD i 4K, zasilanie PoE, zdalny podgląd '
          'i łatwa rozbudowa systemu. GETMON, tel. 884 884 823.',
  'eyebrow': 'MONITORING', 'bg': 'ip',
  'h1': 'Monitoring IP — jakość 4K i podgląd z dowolnego miejsca',
  'lead': 'Kamery IP wysyłają obraz przez sieć, więc podejrzysz go z telefonu praktycznie z każdego miejsca i skonfigurujesz system zdalnie. Bez zakłóceń typowych dla analogu i z możliwością rozbudowy w dowolnym momencie.',
    'ticks': ['Rozdzielczość HD, Full HD i 4K, także w nocy', 'Zdalny podgląd i konfiguracja przez internet', 'Zasilanie PoE — mniej kabli, niższy koszt instalacji', 'Dokładasz kolejne kamery bez przebudowy systemu'],
  'blocks': [
    {'h2': 'Dlaczego IP zamiast analogu?',
     'img': 'ip', 'cap': 'Kamera IP na nowoczesnym budynku',
     'p': ['Połączenie sieciowe umożliwia także zdalną konfigurację systemu. Monitoring cyfrowy '
           'charakteryzuje się ponadto wysoką jakością obrazu. Do powszechnego użytku weszły urządzenia '
           'z rozdzielczością HD, Full HD oraz 4K, przystosowane również do pracy w nocy. W przeciwieństwie '
           'do monitoringu analogowego praktycznie nie występują żadne zakłócenia na wizji.',
           'Kolejna innowacja to zasilanie monitoringu IP przez PoE, czyli dostarczanie energii w ramach '
           'transmisji danych. Dzięki takiemu rozwiązaniu ogranicza się ilość kabli, a tym samym koszty '
           'związane z instalacją elektryczną. To jednak nie wszystko, gdyż monitoring IP można bardzo '
           'łatwo rozbudować o kolejne kamery, bez konieczności zmian w całym systemie. Wystarczy '
           'odpowiednio skonfigurować sieć, by otrzymywać także obraz z dodatkowych urządzeń.']},
  ],
  'related': ['montaz-monitoringu-wroclaw', 'montaz-monitoringu-analogowego-wroclaw',
              'systemy-alarmowe-wroclaw'],
},

'montaz-monitoringu-analogowego-wroclaw': {
  'group': 'monitoring', 'nav': 'Analogowy', 'chip': 'Monitoring',
  'title': 'Monitoring analogowy AHD Wrocław — montaż | GETMON',
  'desc': 'Monitoring analogowy AHD we Wrocławiu — kompatybilność wsteczna, modernizacja CCTV '
          'do 1080p, niższy koszt systemu. GETMON, tel. 884 884 823.',
  'eyebrow': 'MONITORING', 'bg': 'analogowy',
  'h1': 'Monitoring analogowy AHD — tańsza modernizacja istniejącego CCTV',
  'lead': 'Masz już instalację analogową? Nie musisz wymieniać wszystkiego. AHD jest z nią kompatybilny wstecznie, więc system modernizujesz etapami, a obraz podnosisz do 1080p tam, gdzie to naprawdę potrzebne.',
    'ticks': ['Kompatybilność wsteczna z istniejącą instalacją CCTV', 'Modernizacja etapami, bez wymiany całego sprzętu', 'AHD-HD i Full HD — jakość zbliżona do IP', 'Tańsze kamery tam, gdzie wystarczą; 1080p przy bramie'],
  'blocks': [
    {'h2': 'Kiedy analog wciąż ma sens?',
     'img': 'analogowy', 'cap': 'Kamera analogowa w instalacji CCTV',
     'p': ['Istnieją rozwiązania o znacznie lepszej jakości niż kiedyś. Dla przykładu system telewizji '
           'przemysłowej AHD-HD oraz Full HD pozwala na transmisję obrazu w jakości IP. Monitoring '
           'analogowy AHD wykorzystuje w tym celu przewód koncentryczny 75 Ω. Można też zastosować pary '
           'skrętek komputerowych wyposażonych w transformatory wideo. Warto dodać, że każda kamera musi '
           'mieć swój własny konwerter.',
           'Utrata jakości staje się widoczna dopiero w konkretnej sytuacji. Mowa o przekroczeniu '
           'odległości 200 m (przy wykorzystaniu skrętki komputerowej) lub 500 m (w przypadku kabla RG-6, '
           'czyli koncentryka). W wielu obiektach problem więc nie występuje ze względu na ograniczoną '
           'przestrzeń do kontrolowania.']},
    {'h2': 'Jak zmodernizować CCTV bez wymiany wszystkiego?',
     'p': ['Monitoring analogowy AHD może współpracować bez problemów z istniejącymi już systemami '
           'analogowymi dzięki kompatybilności wstecznej. W efekcie możliwa jest migracja z niskiej '
           'rozdzielczości typowej dla analogów do obrazu 2-megapikselowego. W praktyce tworzy się '
           'monitoring składający się z kamer o różnych rozdzielczościach i podłączonych do jednego '
           'rejestratora. To z kolei przydaje się do obserwacji mniej istotnych miejsc przy pomocy tanich '
           'kamer analogowych (960H) i zabezpieczaniu np. bram wjazdowych kamerą AHD 1080p 2 Mpx.',
           'Ze względu na kompatybilność wsteczną warto zdecydować się na modernizację systemów telewizji '
           'CCTV do AHD. Proces przebiega wieloetapowo, ale nie wymaga wymiany całego sprzętu.']},
  ],
  'related': ['montaz-monitoringu-wroclaw', 'montaz-monitoringu-cyfrowego-ip-wroclaw',
              'systemy-alarmowe-wroclaw'],
},

# ---------------------------------------------------------------- alarmy ----

'systemy-alarmowe-wroclaw': {
  'group': 'alarmy', 'nav': 'O systemach alarmowych', 'chip': 'Alarm',
  'title': 'Systemy alarmowe Wrocław — montaż alarmów | GETMON',
  'desc': 'Systemy alarmowe we Wrocławiu i na Dolnym Śląsku — ochrona przed włamaniem, pożarem '
          'i wandalizmem. Dobór i montaż instalacji. GETMON, tel. 884 884 823.',
  'eyebrow': 'SYSTEMY ALARMOWE', 'bg': 'alarmy',
  'h1': 'Systemy alarmowe we Wrocławiu — spokój o dom i firmę',
  'lead': 'Czujki ruchu, wykrywacze dymu i czujniki otwarcia okien — dobrane do obiektu i połączone w system, który wykrywa zagrożenie, zanim zrobi się poważnie. Dla domów, mieszkań i firm na Dolnym Śląsku.',
    'ticks': ['Ochrona przed włamaniem, pożarem i wandalizmem', 'Rozwiązania dla domów, mieszkań i obiektów firmowych', 'Dobór urządzeń i wykonanie niezawodnej instalacji', 'Darmowa wycena po oględzinach obiektu'],
  'blocks': [
    {'p': ['Niezbędny do tego okazuje się zarówno wybór właściwych rozwiązań, jak i stworzenie '
           'niezawodnej instalacji. Pomocne w osiągnięciu takiego efektu będą specjalistyczne urządzenia, '
           'a także renomowany ekspert od instalacji systemów. We Wrocławiu i okolicach mogą Państwo '
           'skorzystać z usług firmy GETMON.']},
    {'h2': 'Alarm dobrany do obiektu, nie z katalogu',
     'img': 'alarmy', 'cap': 'Czujniki systemu alarmowego',
     'p': ['Posiadamy szeroki asortyment systemów alarmowych dostosowanych do potrzeb i oczekiwań '
           'Klienta. Systemy alarmowe pozwalają zwiększyć ochronę monitorowanych obiektów — zarówno '
           'domowych, jak i firmowych. Zmniejszają ryzyko zagrożenia, gwarantują poczucie bezpieczeństwa '
           'i komfortu. Systemy alarmowe doskonale sprawdzą się w miejscach, gdzie znaczenie ma ochrona '
           'przed pożarem, włamaniem czy aktami wandalizmu. Pozwalają na szybkie wykrycie zagrożenia.']},
  ],
  'related': ['systemy-alarmowe-przewodowe-wroclaw', 'systemy-alarmowe-bezprzewodowe-wroclaw',
              'montaz-monitoringu-wroclaw'],
},

'systemy-alarmowe-przewodowe-wroclaw': {
  'group': 'alarmy', 'nav': 'Przewodowe', 'chip': 'Alarm',
  'title': 'Systemy alarmowe przewodowe Wrocław — montaż | GETMON',
  'desc': 'Przewodowe systemy alarmowe we Wrocławiu — montaż w budynkach nowych i istniejących. '
          'Niezawodna ochrona domu i firmy. GETMON, tel. 884 884 823.',
  'eyebrow': 'SYSTEMY ALARMOWE', 'bg': 'alarm-przewodowy',
  'h1': 'Alarmy przewodowe — niezawodność bez zasięgu i baterii',
  'lead': 'Sygnał idzie kablem, więc nie zakłóci go sąsiednia sieć ani awaria internetu. Najlepszy moment na montaż to budowa lub remont — ale okablowanie da się też poprowadzić w listwach, bez kucia ścian.',
    'ticks': ['Transmisja kablem — bez zakłóceń radiowych', 'Dla budynków nowych i już istniejących', 'Okablowanie pod tynkiem, w peszlu albo w listwach', 'Ochrona przed włamaniem i pożarem'],
  'blocks': [
    {'h2': 'Co daje przewodowy system alarmowy?',
     'img': 'alarm-przewodowy', 'cap': 'Centrala i czujniki systemu przewodowego',
     'p': ['Oferujemy wysokiej jakości przewodowe systemy alarmowe, które zostały zaprojektowane z myślą '
           'o ochronie Twojego domu lub firmy. Nasze systemy są łatwe w instalacji i obsłudze, a ponadto '
           'stanowią niezawodną warstwę zabezpieczeń przed intruzami.',
           'Domowy system alarmowy to opłacalna inwestycja dla każdego właściciela domu. Oprócz '
           'odstraszania włamywaczy system alarmowy może również zapewnić ochronę w razie pożaru lub '
           'innego nagłego zdarzenia. Systemy alarmowe są dostępne w różnych wariantach, od prostych '
           'czujników dymu po kompleksowe systemy bezpieczeństwa. Bez względu na rodzaj wybranego systemu '
           'ważne jest, aby został on profesjonalnie zainstalowany przez wykwalifikowanego technika.']},
    {'h2': 'Kiedy montować i jak poprowadzić okablowanie?',
     'p': ['Alarmy przewodowe to doskonałe rozwiązanie zarówno do budynków nowo projektowanych, jak '
           'i już istniejących. W przypadku tych ostatnich, jeśli zdecydujemy się na zamontowanie tej '
           'technologii, możemy zrobić to na dwa sposoby. Wybierając pełną modernizację instalacji '
           'elektrycznej, musimy liczyć się z prawdopodobną wymianą okablowania. Remont będzie znakomitą '
           'okazją do instalacji przewodowego systemu alarmowego.',
           'Obwody instalacji łatwo jest położyć pod warstwą tynku — można też zdecydować się na '
           'położenie rur typu „peszel”, prowadzonych w ścianie. W przypadku gdy nie chcemy decydować się '
           'na tak inwazyjne rozwiązanie, możemy wybrać rozmieszczenie okablowania w dedykowanych listwach '
           'na ścianach czy suficie. To rozwiązanie jest zdecydowanie mniej kosztowne, nie wymaga dużych '
           'nakładów pracy, ale jednocześnie psuje estetykę pomieszczeń.']},
  ],
  'related': ['systemy-alarmowe-bezprzewodowe-wroclaw', 'systemy-alarmowe-wroclaw',
              'montaz-monitoringu-wroclaw'],
},

'systemy-alarmowe-bezprzewodowe-wroclaw': {
  'group': 'alarmy', 'nav': 'Bezprzewodowe', 'chip': 'Alarm',
  'title': 'Alarmy bezprzewodowe Wrocław — montaż systemów | GETMON',
  'desc': 'Bezprzewodowe systemy alarmowe we Wrocławiu — bezinwazyjny montaż, sterowanie z aplikacji, '
          'szyfrowana transmisja. GETMON, tel. 884 884 823.',
  'eyebrow': 'SYSTEMY ALARMOWE', 'bg': 'alarm-bezprzewodowy',
  'h1': 'Alarmy bezprzewodowe — montaż bez kucia ścian',
  'lead': 'Czujki komunikują się radiowo lub przez internet, więc instalacja nie wymaga remontu, a system rozbudujesz w każdej chwili. Powiadomienia trafiają na telefon, a w razie potrzeby — prosto do agencji ochrony.',
    'ticks': ['Bezinwazyjny montaż — bez remontu i kucia ścian', 'Sterowanie i powiadomienia z aplikacji w telefonie', 'Szyfrowana transmisja, możliwy sygnał do agencji ochrony', 'Dokładasz czujki w dowolnym momencie'],
  'blocks': [
    {'p': ['Jeśli szukasz bezprzewodowego systemu alarmowego we Wrocławiu, jesteśmy firmą, do której '
           'powinieneś zadzwonić. Przyjedziemy do Ciebie, ocenimy Twoje potrzeby i zaproponujemy najlepszy '
           'dla Ciebie system. Następnie bezbłędnie zainstalujemy system, dzięki czemu będziesz mieć '
           'pewność, że Twoja nieruchomość jest bezpieczna.']},
    {'h2': 'Jak działa alarm bezprzewodowy?',
     'img': 'alarm-bezprzewodowy', 'cap': 'Bezprzewodowe czujniki systemu alarmowego',
     'p': ['Technologia systemów alarmowych rozwija się w bardzo szybkim tempie. Tradycyjne rozwiązania '
           'zostają niemal całkowicie wypierane przez nowoczesne urządzenia. Wśród obecnie dostępnych na '
           'rynku produktów zdecydowanie dominują bezprzewodowe alarmy, umożliwiające komunikację na '
           'większą odległość. Zainstalowane w danym obiekcie czujniki ruchu, wykrywacze dymu oraz czujki '
           'otwarcia drzwi i okien nie uruchamiają syreny, lecz przekazują stosowną informację za pomocą '
           'sygnału radiowego lub sieci internetowej.',
           'Konfiguracja takiego systemu odbywa się zdalnie, najczęściej za pomocą aplikacji '
           'zainstalowanej na telefonie lub tablecie. To niewątpliwie duże ułatwienie dla użytkowników, '
           'którzy natychmiast dowiedzą się o wszystkich niepożądanych zdarzeniach, nawet znajdując się '
           'w dużej odległości od obiektu. Systemy bezprzewodowe mogą również wysyłać sygnał bezpośrednio '
           'do agencji ochrony, umożliwiając ich błyskawiczną interwencję.']},
    {'h2': 'Wady, o których powiemy Ci wprost',
     'p': ['Mogłoby się wydawać, że tego typu technologia rozwiązuje wszystkie problemy tradycyjnych '
           'instalacji alarmowych. Należy jednak pamiętać o kilku wadach, dotyczących przede wszystkim '
           'systemów wykorzystujących do powiadamiania sygnał radiowy. Taka transmisja okazuje się podatna '
           'na zewnętrzne zakłócenia, a komunikacja staje się możliwa jedynie na ograniczoną odległość. '
           'Problemy te nie występują w przypadku łączności internetowej, jednak zawsze istnieje ryzyko '
           'awarii sieci. Pewną niedogodnością są także wyższe koszty takich systemów.',
           'Wady te wydają się jednak akceptowalne, jeśli wziąć pod uwagę liczne zalety. Alarmy '
           'bezprzewodowe charakteryzują się bezinwazyjną instalacją, niewymagającą remontu obiektu, '
           'a także bardzo prostą, intuicyjną konfiguracją oraz obsługą. Rozbudowa systemu o dodatkowe '
           'czujki jest możliwa w każdym momencie. Najważniejszą zaletą jest jednak możliwość zdalnego '
           'zarządzania systemem oraz otrzymywanie w ten sam sposób powiadomień. Warto też wiedzieć, że '
           'wszystkie przesyłane dane podlegają szyfrowaniu, co gwarantuje bezpieczeństwo transmisji.']},
  ],
  'related': ['systemy-alarmowe-przewodowe-wroclaw', 'systemy-alarmowe-wroclaw',
              'montaz-monitoringu-wroclaw'],
},

}

# Header dropdowns: (group key, label, hub slug, [child slugs])
NAV_GROUPS = [
  ('klimatyzacja', 'Klimatyzacja', 'klimatyzacja-wroclaw', [
      'klimatyzacja-wroclaw', 'klimatyzacja-scienna-split-wroclaw',
      'klimatyzacja-multi-split-wroclaw', 'klimatyzacja-kanalowa-wroclaw',
      'klimatyzacja-kasetonowa-wroclaw', 'klimatyzacja-przypodlogowo-podsufitowa-wroclaw',
      'klimatyzacja-przenosna-wroclaw', 'rodzaje-klimatyzacji']),
  ('wentylacja', 'Wentylacja', 'wentylacja-wroclaw', []),
  ('pompy', 'Pompy ciepła', 'pompy-ciepla-wroclaw', []),
  ('monitoring', 'Monitoring', 'montaz-monitoringu-wroclaw', [
      'montaz-monitoringu-wroclaw', 'montaz-monitoringu-cyfrowego-ip-wroclaw',
      'montaz-monitoringu-analogowego-wroclaw']),
  ('alarmy', 'Systemy alarmowe', 'systemy-alarmowe-wroclaw', [
      'systemy-alarmowe-wroclaw', 'systemy-alarmowe-przewodowe-wroclaw',
      'systemy-alarmowe-bezprzewodowe-wroclaw']),
]

# Short label used in "Sprawdź również" cards
SHORT = {s: d['nav'] for s, d in SERVICES.items()}
