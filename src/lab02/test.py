# a = "ПрИвЕт\nМИр\t"
# b = "ёжик, Ёлка"
# c = "Hello\r\nWorld"
# d = "  двойные   пробелы  "

# print(f'Строка:\n{a}\nНормализованная строка:\n{tokenize(a)}\nСтрока:\n{b}\nНормализованная строка:\n{tokenize(b)}\nСтрока:\n{c}\nНормализованная строка:\n{tokenize(c)}\nСтрока:\n{d}\nНормализованная строка:\n{tokenize(d)} ')
header = ("a", "b")
print(tuple(list(map(type, header))))
