import string


def normalize(text1: str, casefold: bool = True, yo2e: bool = True) -> str:
    if type(text1) != str:
        raise TypeError("Неверный тип данныхх")
    if yo2e:
        text1 = text1.replace("ё", "е")
        text1 = text1.replace("Ё", "Е")

    if casefold:
        text1 = text1.casefold()

    text1 = " ".join(text1.split())
    text1 = " ".join(text1.split("\t"))
    text1 = " ".join(text1.split("\r"))
    text1 = " ".join(text1.split("\n"))

    return text1


def tokenize(text2: str) -> list[str]:

    alph1 = ',./~!@#$%^&*()<>}{=+!"№;%:?*()—'
    alph2 = "'"
    alph3 = "_-"
    alph_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789"
    for i in alph1:
        text2 = text2.replace(i, " ")
    for j in alph2:
        text2 = text2.replace(j, " ")
    text2 = [_ for _ in text2]
    for i in range(len(text2)):
        try:
            if (text2[i] in alph3) and (
                text2[i - 1] in alph_letters and text2[i + 1] in alph_letters
            ):
                pass
            else:
                if text2[i] in alph3:
                    text2[i] = " "
        except:
            if text2[i] in alph3:
                text2[i] = " "
    text2 = "".join(text2)
    text2 = text2.split()
    i = 0
    for element in text2:

        for letter in element:
            if not (letter in alph_letters) and letter not in alph3:
                element = element.replace(letter, "")
                text2[i] = element
        i += 1
    text2 = [i for i in text2 if i != ""]
    return text2


def count_freq(tokens: list[str]) -> dict[str, int]:
    ans = dict()
    if type(tokens) != list:
        raise TypeError(
            f"Не верный тип данных должно быть list, передано {type(tokens)}"
        )
    try:

        if type(tokens[0]) != str:
            raise TypeError(
                f'"Не верный тип данных должно быть list[str], передано list[{type(tokens[0])}]"'
            )
    except:
        pass

    try:
        type_tokens = set(list(map(type, tokens)))
        if len(set) != 1:
            raise TypeError(f"Внутри списка строки разных типов данных {type_tokens}")
    except:
        pass
    for element in tokens:
        if element not in ans:
            ans.update({element: tokens.count(element)})
    return ans


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if type(freq) != dict:
        raise TypeError(f"Не верный тип данных должно быть dict, передано {type(freq)}")
    if type(n) != int:
        raise TypeError(f"Не верный тип данных должно быть int, передано {type(n)}")
    freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    if n > len(freq):
        return freq
    else:
        return freq[:n]


def count_freq_top(tokens: list[str]) -> dict[str, int]:
    tokens = list(input().split())
    ans = dict()
    for element in tokens:
        if element not in ans:
            ans.update({element: tokens.count(element)})
    return f"Всего слов: {len(tokens)}"


# a = "ПрИвЕт\nМИр\t"
# b = "ёжик, Ёлка"
# c = "Hello\r\nWorld"
# d = "  двойные   пробелы  "

# print(f'Строка:\n{a}\nНормализованная строка:\n{normalize(a)}\nСтрока:\n{b}\nНормализованная строка:\n{normalize(b)}\nСтрока:\n{c}\nНормализованная строка:\n{normalize(c)}\nСтрока:\n{d}\nНормализованная строка:\n{normalize(d)} ')
# a = "привет мир"
# b = "hello,world!!!"
# c = "по-настоящему круто"
# d = "2025 год"
# e = "emoji 😀 не слово"

# print(f'Строка:\n{a}\nОтдельно слова:\n{tokenize(a)}\nСтрока:\n{b}\nОтдельно слова:\n{tokenize(b)}\nСтрока:\n{c}\nОтдельно слова:\n{tokenize(c)}\nСтрока:\n{d}\nОтдельно слова:\n{tokenize(d)}\nСтрока:\n{e}\nНормализованная строка:\n{tokenize(e)} ')
# a = ""
# b = "😀😀😀.ha ha-ha😀😀😀😀😀"
# c = "В таком диапазоне: 2020-2025!!!!"
# print(f'Строка:\n{a}\nОтдельно слова:\n{tokenize(a)}\nСтрока:\n{b}\nОтдельно слова:\n{tokenize(b)}\nСтрока:\n{c}\nОтдельно слова:\n{tokenize(c)}')
