# Detekcja zmian użytkowania ziemi

## Zgrubny opis wykonanej pracy

Zadaniem projektowym było napisanie algorytmu, który przy pomocy serwisu AWS, interfejsu Spark oraz języka Python analizować zdjęcia satelitarne na przestrzeni lat w celu wskazania zmian użytkowania ziemi. Grupa została podzielona na zespoły 2 i 3 osobowe w celu okiełznania kolejnych etapów realizacji proejktu.
Ostatecznie udało się opracować algorytm wykrywania zmian na zdęciach satelitarych landsat 8 za pomocą m.in. segmentacji progowej, heatmapy. Wykorzystano AWS i Spark w celu operacji na dużej ilosci danych.

Stuck technologiczny:

- AWS EMR i S3
- PySpark
- Python
  - OpenCV
  - Numpy
  - Matplotlib
  - Rasterio

## Podział grupy na zespoły

- Michał Kolada, Kewin Trochowski - konfiguracja AWS
- Anna Ivanytska, Jakub Dobruchowski, Maksym Małek - pobranie i wstępne przefiltrowanie zdjęć Landsat
- Oliwer Lisek, Mikołaj Galant - Analiza danych, operowanie przy pomocy PySpark
- Konrad Siemiątkowski, Przemek Piątkiewicz, Michał Pryba - detekcja zmian użytkowania ziemi
- Jakub Dufke, Mateusz Drzewiecki - prezentacja wyników, grupa pomocy

## Sprawozdania

Odnośniki do sprawozdań z poszczególnych etapów:

- **[Konfiguracja AWS](sprawozdania/AWS.md)**
- **[Pobranie i wstępne przefiltrowanie zdjęć](sprawozdania/Pobranie_wstepna_obrobka.md)**
- **[Analiza danych i detekcja zmian](sprawozdania/Analiza_Danych.md)**
