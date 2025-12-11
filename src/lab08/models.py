from dataclasses import dataclass
from datetime import *


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            birth = datetime.strptime(self.birthdate, "%Y-%m-%d")
            if birth > datetime.now():
                raise ValueError("Дата рождения в будущем")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        today = datetime.now()
        birth = datetime.strptime(self.birthdate, "%Y-%m-%d")
        age = today.year - birth.year
        if (today.month, today.day) < (birth.month, birth.day):
            age -= 1
        return age

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)

    def __str__(self):
        return f"Студент: {self.fio}\nГруппа: {self.group}\nGPA: {self.gpa:.2f}"


