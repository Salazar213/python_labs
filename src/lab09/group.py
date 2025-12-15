import csv
from pathlib import Path
from src.lab08.models import Student
from src.lab08.serialize import read_json_file, students_to_json
from src.lib.text import csv_to_json, json_to_csv, write_csv, normalize
class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("", encoding="utf-8") 

    def _read_all(self):
        csv_path = self.path
        data = []
        try:
            with csv_path.open(mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                if reader.fieldnames == None:
                    raise ValueError("Пустой заголовок")

                if len(reader.fieldnames) != len(set(reader.fieldnames)):
                    raise ValueError("CSV файл содержит дублирующиеся заголовки")
                for row in reader:
                    str_row = {}
                    if any(
                        value is not None and value.strip() != "" for value in row.values()
                    ):
                        for key, value in row.items():
                            if value is None:
                                str_row[key] = ""
                            else:
                                str_row[key] = str(value)
                    data.append(str_row)

        except:
            raise ValueError("Не удалось прочитать csv файл")
        return data
    def list(self):
        return self._read_all()
    def add(self, student: Student):
        if self.path.exists():
            try:
                with self.path.open('r', encoding='utf-8') as f:
                    content = f.read()
                    if content and not content.endswith('\n'):
                        with self.path.open('a', encoding='utf-8') as f2:
                            f2.write('\n')
            except:
                raise ("Не удалось прочитать файл")
        rows = [[student.fio,student.birthdate,student.group,student.gpa]]
         # TODO: реализовать метод add()
        return write_csv(path=self.path,header=None, type_write='a', rows=rows)
    def find(self, substr: str):
        substr = normalize(substr)
        rows = self.list()
        return [r for r in rows if substr in normalize(r["fio"])]  


    def remove(self, fio: str):
        rows = self._read_all()
        initial_count = len(rows)
        if initial_count == 0:
            return False, "Файл пуст, нечего удалять"
        normalized_target = normalize(fio)
        index_to_remove = -1
        removed_student = None
        for i, row in enumerate(rows):
            normalized_row_fio = normalize(row["fio"])
            if normalized_row_fio == normalized_target:
                index_to_remove = i
                removed_student = row
                break
        
        if index_to_remove == -1:
            return False, f"Студент с ФИО '{fio}' не найден"
        
        rows.pop(index_to_remove)
        
        header = ('fio', 'birthdate', 'group', 'gpa')
        
        rows_to_write = []
        for row in rows:
            rows_to_write.append([
                row['fio'],
                row['birthdate'],
                row['group'],
                row['gpa']
            ])
        
        try:
            write_csv(
                rows=rows_to_write,
                path=self.path,
                header=header,
                type_write='w'
            )
        except Exception as e:
            return False, f"Ошибка при записи файла: {e}"
        
        return True, f"Удален студент: {removed_student['fio']}"

    def update(self, fio: str, **fields):
        rows = self._read_all()
        normalized_target = normalize(fio)  
        found_index = -1
        for i, row in enumerate(rows):
            if normalize(row["fio"]) == normalized_target:
                found_index = i
                break
        
        if found_index == -1:
            return False
        
        current_data = rows[found_index]
        
        updated_data = current_data.copy()
        for key, value in fields.items():
            if key in updated_data:
                updated_data[key] = value
        
        try:
            student_data = {
                "fio": updated_data["fio"],
                "birthdate": updated_data["birthdate"],
                "group": updated_data["group"],
                "gpa": float(updated_data["gpa"])
            }
            student = Student.from_dict(student_data)
        except Exception as e:
            return False, f"Некорректные данные: {e}"
        
        rows[found_index] = {
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        }
        
        data_to_write = []
        for row in rows:
            data_to_write.append([row["fio"], row["birthdate"], row["group"], row["gpa"]])
        
        write_csv(
            rows=data_to_write,
            path=self.path,
            header=('fio', 'birthdate', 'group', 'gpa'),
            type_write='w'
        )
        
        return True, f"Студент '{fio}' успешно обновлен"
    
    def stats(self) -> dict:
    
        rows = self._read_all()
        
        if not rows:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }
        
        students_float = []
        for row in rows:
            try:
                gpa = float(row["gpa"])
                students_float.append({
                    "fio": row["fio"],
                    "birthdate": row["birthdate"],
                    "group": row["group"],
                    "gpa": gpa
                })
            except:
                    raise('Некорректный gpa')
        
        if not students_float:
            return {
                "count": 0,
                "min_gpa": None,
                "max_gpa": None,
                "avg_gpa": None,
                "groups": {},
                "top_5_students": []
            }
        
        count = len(students_float)
        gpa_values = [s["gpa"] for s in students_float]
        min_gpa = min(gpa_values)
        max_gpa = max(gpa_values)
        avg_gpa = sum(gpa_values) / count
        
        groups_dict = {}
        for student in students_float:
            group = student["group"]
            if group not in groups_dict:
                groups_dict[group] = 0
            groups_dict[group] += 1
        
        top_5 = sorted(students_float, key=lambda x: x["gpa"], reverse=True)[:5]
        top_5_students = [
            {"fio": s["fio"], "gpa": s["gpa"]}
            for s in top_5
        ]
        
        return {
            "count": count,
            "min_gpa": round(min_gpa, 2),
            "max_gpa": round(max_gpa, 2),
            "avg_gpa": round(avg_gpa, 2),
            "groups": groups_dict,
            "top_5_students": top_5_students
        }

student = Student.from_dict({
    "fio": "Иванов Иван Иванович",
    "birthdate": "2000-05-15",
    "group": "ИТ-101",
    "gpa": 4.5
  })
group = Group(storage_path="C:/python_labs_alg/python_labs/data/lab09/students.csv")
print(group.stats())