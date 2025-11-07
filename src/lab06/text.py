def min_max(nums1):
    if len(nums1) == 0 or [''] == nums1:
        return "ValueError"
    else:
        miimum = min(nums1)
        maximum = max(nums1)
        return (miimum,maximum)
    

def unique_sorted(nums2):
    a = list()
    if nums2 != ['']:
        nums2 = sorted(set(nums2))
        return nums2
    else:
        return a
    

def flatten(nums3):
    fl = 0
    spis = list()
    for item in nums3:
        if type(item) == tuple or type(item) == list:

            spis.extend(item)
        elif type(item) == str:
            fl = 1 
            return "TypeError"
        else:
            spis.append(item)
    if fl!=1:
        return spis
    

def transpose(mat1):
    rez_mat1 = []
    size_stolb = 0
    size_strok = 0 
    try:
        size_strok = len(mat1)
        size_stolb = int(list(map(len,mat1))[0]) 
    except:
        return []
    i = 0
    j = 0
    rvanost = set(map(len,mat1))
    if (len(rvanost) !=1 and mat1!=[]) or type(mat1) == str :
        return "ValueError"
    j = 0
    k = 0
    for k in range(0,size_stolb):
        rez_mat1.append([])
        for j in range(0,size_strok):
            dobavl = mat1[j][k]
            if dobavl != None:
                rez_mat1[k].append(dobavl)
    return rez_mat1


def row_sums(mat2):
    # rez_mat2 = []
    try:
        dlin_strok = set(list(map(len,mat2)))
        # size_strok = len(mat2)
        # size_stolb = int(list(map(len,mat2))[0]) 
    except:
        pass
    # i = 0
    # j = 0
    # dict ={}
    if (len(dlin_strok) !=1 and mat2!=[]) or mat2 == [] or type(mat2) == str:
        return "ValueError"
    else:
        return list(map(sum,mat2))
    


def format_record(rec):
    # rec = list(rec)
    if len(rec) == 3:

        fio = rec[0]
        group = rec[1]
        gpa = rec[2]
    if len(rec)!=3 or group == '':
        return"ValueError"
    if type(fio) == str and type(group) == str and type(gpa) == float:
            try:
                name, surname, patronymic  = fio.split()
            except:
                 fio+=" None"
                 name, surname, patronymic  = fio.split()
            if patronymic == "None":
                 patronymic = ""
            else:
                 patronymic = patronymic[:-4]
            name = name.capitalize()
            surname = surname.capitalize()
            patronymic = patronymic.capitalize()
            if patronymic != '':
                initials = f"{name} {surname[0]}.{patronymic[0]}."
            else:
                 initials = f"{name} {surname[0]}."
    else:
        return "TypeError"
    ans = f"{initials}, гр. {group}, GPA {gpa:.2f}"
    return ans



def normalize (text1: str, casefold: bool = True , yo2e:bool = True)-> str:
    if type(text1) != str:
        raise TypeError("Неверный тип данныхх")
    if yo2e:
        text1 = text1.replace('ё','е')
        text1 = text1.replace("Ё","Е")
    
    if casefold:
        text1 = text1.casefold()

    text1 = ' '.join(text1.split())
    text1 = ' '.join(text1.split('\t'))
    text1 = ' '.join(text1.split('\r'))
    text1 = ' '.join(text1.split('\n'))

    return text1
def tokenize(text2: str) -> list[str]:
    
    alph1 = ',./~!@#$%^&*()<>}{=+!"№;%:?*()—'
    alph2 = "'"
    alph3 = '_-'
    alph_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789'
    for i in alph1:
        text2 = text2.replace(i, ' ')
    for j in alph2:
        text2 = text2.replace(j, ' ')
    text2 = [_ for _ in text2]
    for i in range(len(text2)):
        try:
            if (text2[i] in alph3) and (text2[i-1] in alph_letters and text2[i+1] in alph_letters):
                pass
            else:
                if text2[i] in alph3:
                    text2[i] = ' '
        except:
            if text2[i] in alph3:
                text2[i] = ' '
    text2 = ''.join(text2)
    text2 = text2.split()
    i = 0
    for element in text2:
        
        for letter in element:
            if not(letter in alph_letters) and letter not in alph3:
                element = element.replace(letter,'')
                text2[i] = element
        i+=1
    text2 = [i for i in text2 if i!=""]
    return text2


def count_freq(tokens: list[str]) -> dict[str, int]:
    ans = dict()
    if type(tokens) != list:
        raise TypeError(f"Не верный тип данных должно быть list, передано {type(tokens)}")
    try:

        if type(tokens[0])!=str:
            raise TypeError(f'"Не верный тип данных должно быть list[str], передано list[{type(tokens[0])}]"')
    except:
        pass

    try:
        type_tokens = set(list(map(type, tokens)))
        if len(set)!=1:
            raise TypeError(f"Внутри списка строки разных типов данных {type_tokens}")
    except:
        pass
    for element in tokens:
        if element not in ans:
            ans.update({element : tokens.count(element)})
    return ans


def top_n(freq: dict[str, int], n: int = 5)-> list[tuple[str, int]]:
    if  type(freq) != dict:
        raise TypeError(f'Не верный тип данных должно быть dict, передано {type(freq)}')
    if  type(n) != int:
        raise TypeError(f'Не верный тип данных должно быть int, передано {type(n)}')
    freq = sorted(freq.items(),key=lambda x: (-x[1],x[0]))
    if n >len(freq):
        return freq
    else:
        return freq[:n]


def count_freq_top(tokens: list[str]) -> dict[str, int]:
    tokens = list(input().split())
    ans = dict()
    for element in tokens:
        if element not in ans:
            ans.update({element : tokens.count(element)})
    return(f"Всего слов: {len(tokens)}")
from pathlib import Path
import csv
from typing import Iterable, Sequence

def read_text (path:str | Path, encoding: str = "utf-8")->str:
    """
    Args
        path - путь к файлу str или Path
        encoding - кодировка, по умолчанию utf-8, возможен выбор других, например cp1251

    Returns
        Содержимое файла как одна строка

    Raises:
        Если файл не найден ошибка FileNotFoundError
        Если кодировка не подходит UnicodeDecodeError
        Если not(isinstance(path,str,Path)), тогда  TypeError("Неверный тип path")
        Если not(isinstance(encoding,str)), тогда TypeError("Неверный тип encoding")
    
    """
    if not(isinstance(path,(str,Path))):
        raise TypeError(f"Неверный тип path type={type(path)}, должно быть str/Path")
    if not(isinstance(encoding,str)):
        raise TypeError(f"Неверный тип encoding type={type(encoding)}, должно быть str")
    path = Path(path)
        
    if not(path.exists()):
        raise FileNotFoundError('Файл не найден')
    try:
        return path.read_text(encoding=encoding)
    except:
        raise UnicodeDecodeError("Неверная кодировка файла")
    

def write_csv (rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None=None, type_write: str="w" ) -> None:
    """
    Args 
        rows 
            данные, которые будем записывать - тип данных итерируемый объект с элементакми списками/кортежами(последовательностями)
        path
            путь к файлу для записи - str или Path

        header
    
            Необязательный заголовок, по умолчанию пуст, тип tuple[str,...]
    
    Returns 
        None
        Записывает данные в файл в кодировке utf-8, ничего не возвращает

    Raises
        Неверный тип данных rows TypeError()
        неверный тип данных path TypeError()
        Неверный тип данных header TypeError()
        в rows есть int or str
        в header разные типы данных
        
    """
    if not(isinstance(path,(str,Path))):
        raise TypeError(f"Неверный тип path type={type(path)}, должно быть str/Path")
    if not(isinstance(rows,Iterable)):
        raise TypeError(f"Неверный тип rows type={type(rows)}, должно быть Iterable")
    if not(isinstance(header,(tuple))) and header!=None:
        raise TypeError(f"Неверный тип header type={type(header)}, должно быть tuple")
    if header!=None and len(set(map(type,header)))>1 :
         raise TypeError(f"В header разные типы данных")
    for row in rows:
        if not(isinstance(row,Sequence)):
            raise TypeError(f"Элемент rows {row} не последовательность")
    
    
    path = Path(path)
    rows = list(rows)
    with path.open(type_write, newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

def ensure_parent_dir (path: str | Path):
    """
    Arg
        path
            путь к файлу для записи - str или Path
    Returns
        создаёт все папки по указаному пути, ничего не возвращает
    
    Raises
        Неверный тип данных path TypeError()

    """
    if not(isinstance(path,(str,Path))):
        raise TypeError(f"Неверный тип path type={type(path)}, должно быть str/Path")
    path.parent.mkdir(parents=True, exist_ok=True)


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