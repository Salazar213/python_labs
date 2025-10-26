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
    

def write_csv (rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None=None ) -> None:
    """
    Args 
        rows 
            данные, которые будем записывать - тип данных итерируемый объект с элементакми списками/кортежами(последовательностями)
        path
            путь к файлу для записи - str или Path

        header
    
            Необязательный заголовок, по умолчанию пуст, тип tuple[str,...]
    
    Returns 
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
    with path.open("w", newline="", encoding="utf-8") as f:
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

write_csv([],"data/lab04/check.csv",header=("a","b"))  # создаст CSV
