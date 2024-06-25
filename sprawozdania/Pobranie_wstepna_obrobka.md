# Sprawozdanie z Etapu Projektu: Pobranie i wstępna obróbka danych

## Wprowadzenie

Celem tego etapu projektu był wybór i wczytanie zdjęć satelitarnych z dobrą widocznością zachodzących zmian. Proces ten obejmował współpracę z zespołami obrabiającymi dane, stworzenie konta na platformie Earthexplorer i wybranie bezchmurnych zdjęć z satelity Landsat8. Dodatkowo stworzeny został kod w Pythonie pozwalający na wczytanie zdjęć w formatach .TIF oraz .jpg, a także podział zdjęć na mniejsze fragmenty.

## Wykonane Zadania

### 1. Wybór satelity oraz zdjęć z niskim pokryciem chmur

Na platformie Eartexplorer wybrana została satelita Landsat 8-9 umożliwiająca pobranie zdjęć bez zniekształceń oraz bez czarnych pasków. Pobrane zdjęcia pochodzą z lat 2013-2024. W wyszukiwarce udostępnionej przez serwis wybrane zostało pokrycie chmur poniżej 10%, aby umożliwić dobrą widoczność. Istotny w tym etapie był wybór zdjęć pochodzących z podobnej pory roku oraz pory dnia.

#### Proces:

1. Stworzenie konta na platformie Earthexplorer.
2. Wybór zdjęć kluczowych terenów z dobrą widocznością.

  <img src="https://github.com/Morpheus1024/Detekcja-zmian-uzytkowania-ziemi/assets/108287744/c4975466-4bbf-4cd3-9e78-579dfaa817fb" alt="Earthexplorer" height="250">

### 2. Pobranie zdjęć

Po wyborze zdjęć zostały one pobrane w formatach .TIF oraz .jpg.

#### Proces:

1. Wybór paczek zdjęć z kanałami w formacie .TIF oraz zdjęć w formacie .jpg.
2. Pobranie zdjęć jako Bulk Download

### 3. Wczytanie zdjęć w różnych formatach

Napisany został kod do wczytania i wyświetlenia zdjęć.

#### Proces:

1. Napisanie części odpowiedzialnej za wczytanie poszczególnych kanałów .TIF. 
2. Połączenie kanałów w celu uzyskania kolorowego zdjęcia terenu w dobrej rozdzielczości.

```python
stacked_array, meta = es.stack(band_paths)
output_path = os.path.join(image_directory, 'stacked_landsat.tif')

with rasterio.open(
        output_path,
        'w',
        driver='GTiff',
        height=stacked_array.shape[1],
        width=stacked_array.shape[2],
        count=stacked_array.shape[0],
        dtype=stacked_array.dtype
) as dst:
    for i in range(stacked_array.shape[0]):
        dst.write(stacked_array[i, :, :], i + 1)
```

3. Dodanie linii odpowiedzialnych za wczytanie zdjęcia z rozszerzeniem .jpg.

  <img src="https://github.com/Morpheus1024/Detekcja-zmian-uzytkowania-ziemi/assets/108287744/28d75f03-b8e9-4d36-916a-2b6d5ac79094" alt="Earthexplorer" height="250">

### 4. Fragmentacja zdjęcia

Ze względu na duży rozmiar zdjęcie zostało podzielone na mniejsze części w celu łatwiejszej analizy bądź możliwości dostosowania kodu do wycinania kluczowych fragmentów zdjęć np. miejsc z największymi zmianami.

#### Proces:

1. Wpisanie wielkości końcowych małych fragmentów.
2. Podział na mniejsze fragmenty o podanej wcześniej wielkości i zapisanie ich do folderu wyjściowego.

```python
    for i in range(num_rows):
        for j in range(num_cols):
            section = stacked_array[:, i * section_size[0]:(i + 1) * section_size[0],
                      j * section_size[1]:(j + 1) * section_size[1]]
            section_rgb = np.dstack([section[4], section[3], section[2]])
            section_rgb_normalized = normalize_to_uint8(section_rgb)
            section_path = os.path.join(output_dir, f'section_{i}_{j}.png')
            plt.imsave(section_path, section_rgb_normalized)
            print(f"Section saved to {section_path}")

```

## Podsumowanie

W tym etapie projektu zrealizowane zostały zadania związane z pobieraniem i wstępną obróbką zdjęć satelitarnych. Pobranie i przetworzenie zdjęć umożliwiło nam uzyskanie wysokiej jakości danych, które będą wykorzystywane w dalszych analizach. Sprawdzenie przejrzystości zdjęć oraz zarządzanie wersjami danych w repozytorium Git zapewniają solidne podstawy do kontynuowania pracy nad projektem.
