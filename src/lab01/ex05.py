name, surname, patronymic = input("ФИО: ").split()
initials = f"{name[0]}.{surname[0]}.{patronymic[0]}."
print(f"Инициалы: {initials}\nДлина: {len(name + surname + patronymic)+2}")
