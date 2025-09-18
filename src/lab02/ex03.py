def format_record(rec):
    rec = list(rec)
    if len(rec) == 3:

        fio = rec[0]
        group = rec[1]
        gpa = rec[2]
    if len(rec)!=3 or group == '' or  :
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

        
print(format_record(("  сидорова  анна   сергеевна ", "", 3.999)))