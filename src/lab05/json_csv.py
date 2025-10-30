import json, csv
from pathlib import Path
def json_to_csv(json_path: str|Path, csv_path: str|Path) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    # Тут будут raises


    json_path = Path(json_path)
    csv_path = Path(csv_path)
    try:
        with json_path.open(mode='r',encoding='utf-8') as f:
            data = json.load(f)
    except:
        raise json.JSONDecodeError(f"Ошибка чтения файла")
    
    if not isinstance(data, list):
        raise TypeError(f"JSON должен содержать list")
    
    if len(data)==0:
        raise ValueError("Пустой JSON файл")
    if not all(isinstance(item,dict) for item in data):
        raise TypeError("Все элементы JSON должны быть словарями")
    
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())

    field_names = sorted(all_keys)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with csv_path.open(mode='w', encoding='utf-8',newline='') as d:
        writer = csv.DictWriter(d, fieldnames=field_names)
        writer.writeheader()
        for item in data:
            row = {key:item.get(key,'')for key in field_names}
            writer.writerow(row)
            

    
    