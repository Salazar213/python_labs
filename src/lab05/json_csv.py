import json, csv
from pathlib import Path
import xlsxwriter

def json_to_csv(json_path: str|Path, csv_path: str|Path) -> None:
    """
    Args
        json_path - путь к файлу str|Path .json из него читаем данные - список словарей
        csv_path - путь к файлу str|Path .csv, файл может не существовать, тодгда создаём все родительские папки и сам файл

    Return
        None
        (Создаёт файл с данными)

    Raises
        TypeError(f"json_path неправильнвй тип. Ожидается str|Path, передан {type(json_path)}")
        TypeError(f"csv_path неправильнвй тип. Ожидается str|Path, передан {type(csv_path)}")
        FileNotFoundError("Файл не найден")
        raise json.JSONDecodeError(f"Ошибка чтения файла")

    
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    
    if not(isinstance(json_path,(str,Path))):
        raise TypeError(f"json_path неправильнвй тип. Ожидается str|Path, передан {type(json_path)}")
    
    if not(isinstance(csv_path,(str,Path))):
        raise TypeError(f"csv_path неправильнвй тип. Ожидается str|Path, передан {type(csv_path)}")
    

    json_path = Path(json_path)
    if not(json_path.exists()):
        raise FileNotFoundError("Файл не найден")
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
            


def csv_to_json(csv_path: str|Path, json_path:str|Path) -> None:
    """
    Args
        csv_path - путь к файлу str|Path .csv из него читаем данные
        json_path - путь к файлу str|Path .json, файл может не существовать, тогда создаём все родительские папки и сам файл

    Return
        None
        (Создаёт файл с данными)

    Raises
        TypeError(f"json_path неправильный тип. Ожидается str|Path, передан {type(json_path)}")
        TypeError(f"csv_path неправильный тип. Ожидается str|Path, передан {type(csv_path)}")
        FileNotFoundError("Файл не найден")
        ValueError("Пустой заголовок")
        ValueError("CSV файл содержит дублирующиеся заголовки")
        ValueError("Не удалось прочитать csv файл")
        ValueError("Пустой файл")
        ValueError("Не удалось записать json")

    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    
    if not(isinstance(json_path,(str,Path))):
        raise TypeError(f"json_path неправильнвй тип. Ожидается str|Path, передан {type(json_path)}")
    
    if not(isinstance(csv_path,(str,Path))):
        raise TypeError(f"csv_path неправильнвй тип. Ожидается str|Path, передан {type(csv_path)}")
    

    csv_path = Path(csv_path)
    json_path = Path(json_path)
    if not(csv_path.exists()):
        raise FileNotFoundError("Файл не найден")
    data = []
    try:
        with csv_path.open(mode='r',encoding='utf-8') as f:
            reader = csv.DictReader(f)
            if reader.fieldnames == None:
                raise ValueError("Пустой заголовок")

            if len(reader.fieldnames)!=len(set(reader.fieldnames)):
                raise ValueError("CSV файл содержит дублирующиеся заголовки")
            for row in reader:
                str_row = {}
                if any(value is not None and value.strip() != "" for value in row.values()):
                    for key, value in row.items():
                        if value is None:
                            str_row[key] = ""
                        else:
                            str_row[key] = str(value)
                data.append(str_row)

    except:
        raise ValueError("Не удалось прочитать csv файл")

    json_path.parent.mkdir(parents=True,exist_ok=True)
    if len(data) == 0:
        raise ValueError("Пустой файл")
    try:
        with json_path.open(mode ='w',encoding='utf-8') as d:
            json.dump(data, d, ensure_ascii=False, indent=2)
    except:
        raise ValueError("Не удалось записать json")
    

def csv_to_xlsx(csv_path: str|Path, xlsx_path: str|Path) -> None:
    """
     Args
        csv_path - путь к файлу str|Path .csv из него читаем данные
        xlsx_path - путь к файлу str|Path .xlsx, файл может не существовать, тогда создаём все родительские папки и сам файл

    Return
        None
        (Создаёт файл с данными)

    Raises
        FileNotFoundError(f"CSV файл не найден: {csv_path}")
        ValueError(f"Ошибка чтения CSV файла: {csv_path}")

    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    xlsx_path = Path(xlsx_path)
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    xlsx_path.parent.mkdir(parents=True,exist_ok=True)
    workbook = xlsxwriter.Workbook(xlsx_path)
    worksheet = workbook.add_worksheet('Sheet1')
    len_col = {}
    try:
        with csv_path.open(mode='r', encoding='utf-8') as d:
                csv_reader = csv.reader(d)
                for row_num, row_data in enumerate(csv_reader):
                    for col_num, cell_value in enumerate(row_data):
                        worksheet.write(row_num,col_num,cell_value)
                        if col_num in len_col:
                            len_col[col_num] = max(len_col[col_num],len(cell_value))
                        else:
                            len_col[col_num] = max(8,len(cell_value))
                        
    except:
        raise ValueError(f"Ошибка чтения CSV файла: {csv_path}")
    for col_num, max_length in len_col.items():
        worksheet.set_column(col_num, col_num, max_length)
    
    workbook.close()
# csv_to_json('python_labs/data/samples/cities.csv','python_labs/data/samples/result/cities.json')
# csv_to_json('python_labs/data/samples/people.csv','python_labs/data/samples/result/people.json')
# json_to_csv('python_labs/data/samples/people.json','python_labs/data/samples/result/cities.csv')
# csv_to_xlsx('python_labs/data/samples/people.csv','python_labs/data/samples/result/people.xlsx')
# csv_to_xlsx('python_labs/data/samples/cities.csv','python_labs/data/samples/result/cities.xlsx')

# csv_to_json('python_labs/data/samples/vegetables.csv','python_labs/data/samples/result/vegetables.json')
# csv_to_xlsx('python_labs/data/samples/vegetables.csv','python_labs/data/samples/result/vegetables.xlsx')
# csv_to_json('python_labs/data/samples/wrong.csv','python_labs/data/samples/result/wrong.json')