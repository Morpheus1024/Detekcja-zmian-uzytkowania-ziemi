# Sprawozdanie z Etapu Projektu: Zarządzanie AWS

## Wprowadzenie

Celem tego etapu projektu było skonfigurowanie środowiska AWS, załadowanie danych oraz przygotowanie klastra AWS EMR do pracy z Apache Spark. Proces ten obejmował współpracę z zespołem odpowiedzialnym za pobieranie zdjęć, konfigurację polityk bezpieczeństwa, utworzenie klastra EMR oraz instalację Apache Spark na klastrze.

## Wykonane Zadania

### 1. Załadowanie danych do AWS

Współpraca z zespołem pobierającym zdjęcia: Pracowaliśmy z zespołem odpowiedzialnym za pobieranie zdjęć, aby upewnić się, że dane zostały poprawnie załadowane do AWS S3.

#### Proces:

1. Stworzenie bucketu S3 do przechowywania danych.
2. Załadowanie zdjęć do bucketu.

![img.png](img.png)

### 2. Konfiguracja Polityk Bezpieczeństwa

Bezpieczeństwo dostępu do danych: Skonfigurowaliśmy polityki IAM, aby zapewnić bezpieczeństwo dostępu do danych.

#### Proces:

1. Stworzenie roli IAM z odpowiednimi uprawnieniami do dostępu do S3 i EMR.
2. Utworzenie IAM user z odpowiednimi do pracy uprawnieniami.

### 3. Konfiguracja AWS EMR

Przygotowaliśmy klaster EMR do analizy danych za pomocą Apache Spark.

#### Proces:

1. Stworzenie klastra EMR.
2. Konfiguracja instancji i ustawień klastra.

![img_1.png](img_1.png)

### 4. Instalacja Apache Spark na Klastrze

Zainstalowaliśmy Apache Spark na klastrze EMR i przygotowaliśmy środowisko do analizy danych.

#### Proces:

1. Instalacja Spark na klastrze EMR (jest automatycznie instalowana przy tworzeniu klastra z aplikacją Spark).
2. Konfiguracja Spark dla optymalnej wydajności.
  
### 5. Integracja EMR Studio z Jupyter Notebook

Zintegrowaliśmy EMR Studio z Jupyter Notebook w celu przeprowadzania interaktywnych analiz danych.

![img_2.png](img_2.png)

## Workflow

1. **AWS S3**: Przechowywanie danych (zdjęć).
2. **AWS IAM**: Zarządzanie dostępem do zasobów.
3. **AWS EMR**: Analiza danych za pomocą Apache Spark.
4. **EMR Studio**: Tworzenie i uruchamianie aplikacji Spark.
5. **Jupyter Notebook**: Interaktywne analizy danych.

## Podsumowanie

W ramach tego etapu projektu udało nam się skonfigurować środowisko AWS, załadować dane oraz przygotować klastrę AWS EMR do pracy z Apache Spark. Dzięki temu będziemy mogli przystąpić do analizy danych i wizualizacji wyników w kolejnych etapach projektu.
