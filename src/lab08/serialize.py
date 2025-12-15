from .models import Student
import json
from typing import Any, Dict
from pathlib import Path
def students_to_json(students:list[Dict],path):
    """
    Записывает в json файл(путь - path) список студентов
    
    Args:
        students - список словарей
        path - путь к файлу json
    """
    path = Path(path)
    if not(isinstance(students,(list,dict))):
        raise TypeError("students не список словарей/словарь")
    if isinstance(students,dict):
        students = list(students)


    data = [s.to_dict() for s in students]
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open(mode="w", encoding="utf-8") as d:
            json.dump(data, d, ensure_ascii=False, indent=2)

def read_json_file(file_path: str | Path) -> Dict[str, Any]:
    """
    Читает JSON файл и возвращает его содержимое в виде словаря.
    
    Args:
        file_path: Путь к JSON файлу (строка или объект Path)
    
    Returns:
        Словарь с данными из JSON файла
    
    Raises:
        FileNotFoundError: Если файл не существует
        json.JSONDecodeError: Если файл содержит невалидный JSON
        ValueError: путь не ведёт к файлу
        TypeError: файл не полностью состоит из словарей
    """
    students = []
    try:
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        
        if not path.is_file():
            raise ValueError(f"Указанный путь не является файлом: {file_path}")
        
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        for item in data:
            if not isinstance(item, dict):
                raise TypeError("Каждый элемент массива должен быть объектом.")
            students.append(Student.from_dict(item))

        return students
    
    except:
        raise json.JSONDecodeError(f"Ошибка декодирования JSON в файле {file_path}")
