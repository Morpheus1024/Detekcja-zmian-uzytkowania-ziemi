# Analiza Danych

## Wstęp

W ramach naszego projektu skupiliśmy się na analizie danych satelitarnych w celu zbadania zmian na powierzchni Ziemi. Początkowo wykorzystaliśmy obrazy z satelity Landsat 7, jednak ze względu na problemy z jakością i niedoskonałością zdjęć - patrz czarne paski po lewej i po prawej zdjęcia, zmieniliśmy podejście na obrazy z nowszego satelity Landsat 8. Oferuje ona zdjęcia od 2013 roku. Przeprowadziliśmy szczegółową analizę porównawczą tych zdjęć, aby ocenić zmiany zachodzące w badanym obszarze.
W tym sprawozdaniu przedstawiono ewolucję metodologi analizy obrazów satelitarnych.

## Metodologia

### Wykorzystanie Landsat 7

Na początku projektu korzystaliśmy z obrazów Landsat 7, który dostarczał danych od 1999 roku. Satelita ten jest wyposażony w Enhanced Thematic Mapper Plus (ETM+). Naszym celem było przeanalizowanie zmian w wybranych latach. Niestety, napotkaliśmy istotne problemy związane z jakością danych. Największym problemem były czarne paski na pobranych obrazach.

### Przejście na Landsat 8

Ze względu na wspomniane trudności, zdecydowaliśmy się na wykorzystanie obrazów z satelity Landsat 8, uruchomionego w 2013 roku. Satelita ten jest wyposażony w Operational Land Imager (OLI) i Thermal Infrared Sensor (TIRS), co pozwoliło na uzyskanie bardziej szczegółowych i precyzyjnych danych. Obrazy z Landsat 8 nie miały problemu z czarnymi paskami, co znacznie ułatwiło naszą analizę.

### Próby Użycia Modeli Analizy Obrazów

Przed przejściem do bezpośredniego porównania zdjęć, podjęliśmy próby zastosowania różnych modeli analizy obrazów w celu automatyzacji procesu. Przetestowaliśmy takie modele jak ResNet 50, ResNet 101, YOLO v8, YOLO v9 oraz pięć innych modeli. Niestety, żaden z tych modeli nie przyniósł zadowalających wyników w kontekście analizy danych satelitarnych z Landsat. Modele miały trudności z dokładnym identyfikowaniem zmian w pokryciu terenu, co zmusiło nas do zmiany podejścia.

### Analiza oparta na segmentacji z thresholdingiem

Po zrezygnowaniu z użycia gotowych modeli przystąpiono do opracowywania innego rozwiązania. Pierwotny proces składał się z następujących etapów:

1. Wczytanie odpowiednich zdjęć
2. Przycięcie obrazów w celu zniwelowania przesunięcia reprezentowanego terenu
3. Wyliczenie różnic pomiędzy pixelami, normalizacja, zastosowanie thresholdingu w celu wyświetlenia różnic
4. Zastosowanie algorytmu K-Means w celu znalezienia dominujących kolorów obazu różnic
5. Przypisanie klasy do wykrytych kolorów: las, miasto, woda, pole

Przykład działania algorytmu na zdjęciu z lasu deszczowego:

![image](https://github.com/knrdsmt/AWS-Klasyfikacja/assets/97449172/1c49f25b-2f75-4c2b-bbf9-06ecf149c2c6)

## Proces Analizy

Ostatecznie proces analizy został usprawniony.

1. **Zbieranie Danych**: Rozpoczęliśmy od zebrania odpowiednich obrazów z obu satelitów dla wybranych lat.
2. **Przygotowanie i Wstępne Przefiltrowanie Danych**: Przeprowadziliśmy wstępną obróbkę danych, usuwając artefakty i kalibrując obrazy, Odrzucono obrazy, które nie nadawały się do analizy.
3. **Proces Porównanie Obrazów**
   1. Odnalezienie ze zbioru danych dwóch obrazów, które reprezentują ten sam obszar Ziemi poprzez dekodowanie informacji znalezionych w nazwie plików: odczytanie parametrów path, row oraz roku wykonania zdjęcia. Określenie, które zdjęcie jest starsze, a które młodsze.
   2. Zamiana kolorów zdjęć na skalę szarości, wykorzystanie algorytmu Oriented FAST and Rotated BRIEF w celu ekstrakcji cech, identyfikacja punktów podobieństwa za pomocą BFMacher.
   3. Obliczenie macierzy homografii i wyrównanie obrazów w celu niwelacji przesunięcia przedstawionego terenu.
   4. Wyznaczenie wspólnego obszaru przedstawionego na obu zdjęciach i docięcie ich.
   5. Obliczenie różnic między obrazami, normalizacja i redukcja do jednego kanału
   6. Analiza zmian
   7. Wizualizacja wyników: pokazanie obrazów wejściowych, map ciepła, zbiżenie na największe wykryte zmiany między obrazami.

![alt text](1.png)

## Wnioski

Nasza praca pokazała, że przejście na dane z Landsat 8 było kluczowe dla uzyskania bardziej wiarygodnych i dokładnych wyników. Dzięki nowocześniejszym sensorom i lepszej jakości obrazów mogliśmy dokładniej przeanalizować zmiany zachodzące na powierzchni Ziemi.Stwierdziliśmy, że bezpośrednie porównanie zdjęć okazało się najbardziej efektywną metodą analizy, mimo wcześniejszych prób zastosowania różnych modeli analitycznych.

## PySpark

Oprócz zadania zwiazanego z analizą danych zapoznaliśmy się z PySparkiem, którego użycie zostało wskazane w opisie zadania projektowego. Wykorzystano go do agregacji zdjęć wybranych przez nas zdjeć oraz do częściowej obróbki danych.
PySpark został wykorzystany tak na lokalnej maszynie jak i na klastrze obliczeniowym w serwisie AWS.
Z naszej obserwacji wynikła, że zastosowanie Sparka przyśpieszyło tempo wykonywania operacji na pobranych zdjęciach.
