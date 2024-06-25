# Sprawozdanie z Etapu Projektu: Pobtanie i ibróbka zdjęć

## Wprowadzenie
Celem tego etapu było wstępne pobieranie zdjęć satelitarnych ze strony EarthExplorer oraz wstępne klasyfikacja.

## Wykonane zadania

### 1. Pobranie zdjęć ze strony
Pierwszym krokiem było zidentyfikowanie odpowiednich źródeł danych satelitarnych oraz pobranie wymaganych zdjęć. Użyliśmy strony EarthExplorer, aby uzyskać obrazy z satelity Landsat. Proces obejmował wybór odpowiednich scen, określenie interesującego nas obszaru geograficznego oraz pobranie plików w formacie GeoTIFF.

### 2. Wstępne przetwarzanie zdjęć
Po pobraniu zdjęć, przystąpiliśmy do ich wstępnego przetwarzania. Wykorzystaliśmy bibliotekę `rasterio` do wczytania poszczególnych kanałów obrazu. Następnie, za pomocą `earthpy`, połączyliśmy te kanały w jeden zstackowany obraz. Wykonaliśmy również normalizację danych, aby zapewnić spójność w dalszych etapach analizy.

### 3. Sprawdzenie zdjęć na obecność chmur
W celu zapewnienia jakości danych, sprawdziliśmy obrazy pod kątem obecności chmur. Wykorzystaliśmy algorytmy detekcji chmur, które analizują poszczególne kanały obrazu, aby wykryć i zaznaczyć obszary pokryte chmurami. Obrazy z nadmierną ilością chmur zostały odrzucone lub oznaczone do dalszej weryfikacji.

### 4. Upload zdjęć na Gita
Ostatecznym krokiem było umieszczenie przetworzonych zdjęć w repozytorium Git. Ze względu na dużą objętość danych, zdecydowaliśmy się na wykorzystanie Git Large File Storage (LFS). Proces obejmował utworzenie nowych gałęzi w repozytorium, dodanie plików, ich zatwierdzenie oraz przesłanie do zdalnego repozytorium z użyciem Git LFS, co zapewnia efektywne zarządzanie dużymi plikami.

## Podsumowanie:
W tym etapie projektu zrealizowaliśmy kluczowe zadania związane z pobieraniem i wstępną obróbką zdjęć satelitarnych. Pobranie i przetworzenie zdjęć umożliwiło nam uzyskanie wysokiej jakości danych, które będą wykorzystywane w dalszych analizach. Sprawdzenie obecności chmur oraz zarządzanie wersjami danych w repozytorium Git zapewniają solidne podstawy do kontynuowania pracy nad projektem.


