# **Лабораторная работа №1**
## Задача 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
![рис. 1 — пример выполнения ](images/lab01/image01.png)
## Задача 2 
```python
a = float(input("a: ").replace(',','.'))
b = float(input("b: ").replace(',','.'))
print (f"sum: {a+b:.2f} avg: {(a+b)/2:.2f}")
```
Возможность вводить числа через запятую реализована с помощью ```replace```
![рис.2 - пример выполнения](images/lab01/image02.png)
## Задача 3
```python
price = float(input("Цена: "))
discount = float(input("Скидка: "))
vat = float (input("Налог: "))
base = price*(1-(discount/100))
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки {base:.2f}")
print(f"НДС {vat_amount:.2f}")
print(f"Итого к оплате {total:.2f}")
```
Округение до 2 знаков реализовано с помощью ```.2f```
![рис.3 - пример выполненяия](images/lab01/image03.png) 
## Задача 4
```python
m = int(input("Минуты "))
days = 0
if m <1440:
    print(f"{m//60}:{(m%60):02d}")
else:
    while m>1440:
        m-=1440
        days+=1
print(f"{days}\n{m//60}:{(m%60):02d}")
```
Формат времени с впередистоящими нулями реализован через `:02d`
![рис.4 - пример выполнения](images/lab01/image04.png)
## Задача 5
```python
name, surname, patronymic  = input("ФИО: ").split()
initials = f"{name[0]}.{surname[0]}.{patronymic[0]}."
print(f"Инициалы: {initials}\nДлина: {len(name + surname + patronymic)+2}")
```
![рис.5 - пример выполнения](images/lab01/image05.png)
## Задача 6

```python
n = int(input("N: "))
person = 0
online = 0
for i in range(n):
    surname, name, age, form = input().split()
    if form == 'True':
        person+=1
    else:
        online+=1
print(person, online)
```
![рис.6 - пример выполнения](images/lab01/image06.png)
## Задача 7
```python
alphabet_big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_number = "0123456789"
stroka = input()
no_chiper = str()
k = 0

for i in stroka:
    if i in alphabet_big:
        break
    k += 1 
        
stroka = stroka[k:]
for j in range(len(stroka)):
    if stroka[j] in alphabet_number:
        shag = j+1
        break
for l in range(0, len(stroka), shag):
    no_chiper+=stroka[l]
    
print(no_chiper)

```
![рис.7 - пример выполнения](images/lab01/image07.png)



# **Лабораторная работа №2**
## Задача 1(A)
`min_max(nums: list[float | int]) -> tuple[float | int, float | int]`  
   Вернуть кортеж `(минимум, максимум)`. Если список пуст — `ValueError`.
```python
def min_max(nums1):
    if len(nums1) == 0 or [''] == nums1:
        return "ValueError"
    else:
        miimum = min(nums1)
        maximum = max(nums1)
        return (miimum,maximum)
```
Здесь nums1 - готоый список, состоящий из `int` и/или `float` , если же требуется ввод с клавиатуры, то можно сделать так: 
```python
def beauty(x):
    if '.' in x:
        return float(x)
    elif '' == x:
        return x
    else:
        return int(x)


spis = list(input().split(','))
spis = list(map(beauty, spis))
```
Функция сохраняет исходный тип числа `int` или `float` чтобы при выводе могла вохникнуть ситуация `(-3.1, 2)` - `min` и `max` разные типы. Это - для ввода списка таким образом `3, -1 , 5, 5, 0`
Если же мы хотим вводить с клавиатуры именно вот так `[3, -1, 5, 5, 0]` (т.е. используя `[]`  ), то тут поможет функция ```python eval```
Вроде все случаи вводра разобрал, далее они упоминаться не будут
Пример работы `min_max`

![рис1 - пример min max](images/lab02/image01.png)

Следующая функция 
 `unique_sorted(nums: list[float | int]) -> list[float | int]`  
   Вернуть **отсортированный** список **уникальных** значений (по возрастанию).
```python
def unique_sorted(nums2):
    a = list()
    if nums2 != ['']:
        nums2 = sorted(set(nums2))
        return nums2
    else:
        return a
```
Уникальность добивается `set`
Пример работы `unique_sorted`

![пример работы `unique_sorted`](images/lab02/image02.png)

Последняя функция `flatten`
```python
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
```
Пример работы

![рис flatten](images/lab02/image03.png)

## Задача 2 (B)
Первая функция
`transpose(mat: list[list[float | int]]) -> list[list]`  
   Поменять строки и столбцы местами. Пустая матрица `[]` → `[]`.  
   Если матрица «рваная» (строки разной длины) — `ValueError`.


```python
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
```
Пример работы

![транс](images/lab02/image04.png)

Вторая функция
`row_sums(mat: list[list[float | int]]) -> list[float]`  
   Сумма по каждой строке. Требуется прямоугольность (см. выше).

```python
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
```
![сумма по строкам](images/lab02/image05.png)

Следующая функция - Сумма по строкам, это просто 2 предыдущие функции
```python
def col_sums(mat3):
    return row_sums(transpose(mat3))
```
Пример выполнения

![сумма столбцов](images/lab02/image06.png)


## Задача 3 (C)
Реализуйте `format_record(rec: tuple[str, str, float]) -> str`
```python
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
```

Примеры выполнения программы(доп примеры для показания возможных ошибок)
![format_record](images/lab02/image07.png)

Все функции дополнительно сохранены в lib

# **Лабораторная работа №3**
## Задание A
1. `normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str`  
   - Если `casefold=True` — привести к **casefold** (лучше, чем `lower` для Юникода).  
   - Если `yo2e=True` — заменить все `ё`/`Ё` на `е`/`Е`.  
   - Убрать невидимые управляющие символы (например, `\t`, `\r`) → заменить на пробелы, схлопнуть повторяющиеся пробелы в один.

```python
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
```
Тесты:
```python
a = "ПрИвЕт\nМИр\t"
b = "ёжик, Ёлка"
c = "Hello\r\nWorld"
d = "  двойные   пробелы  "
print(f'Строка:\n{a}\nНормализованная строка:\n{normalize(a)}\nСтрока:\n{b}\nНормализованная строка:\n{normalize(b)}\nСтрока:\n{c}\nНормализованная строка:\n{normalize(c)}\nСтрока:\n{d}\nНормализованная строка:\n{normalize(d)} ')
```

![normilize](images/lab03/image01.png)

2. `tokenize(text: str) -> list[str]`  
   - Разбить на «слова» по небуквенно-цифровым разделителям.  
   - В качестве слова считаем последовательности символов `\w` (буквы/цифры/подчёркивание) **плюс** дефис внутри слова (например, `по-настоящему`).  
   - Числа (например, `2025`) считаем словами.

```python
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

```
Тесты
```python
a = "привет мир"
b = "hello,world!!!"
c = "по-настоящему круто"
d = "2025 год"
e = "emoji 😀 не слово"

print(f'Строка:\n{a}\nОтдельно слова:\n{tokenize(a)}\nСтрока:\n{b}\nОтдельно слова:\n{tokenize(b)}\nСтрока:\n{c}\nОтдельно слова:\n{tokenize(c)}\nСтрока:\n{d}\nОтдельно слова:\n{tokenize(d)}\nСтрока:\n{e}\Отдельно слова:\n{tokenize(e)} ')
```

![tokenize_0](images/lab03/image02.png)

Дополнительные тесты:
```python
a = ""
b = "😀😀😀.ha ha-ha😀😀😀😀😀"
c = "В таком диапазоне: 2020-2025!!!!"
-//-
```

![tonize_1](images/lab03/image03.png)

3. `count_freq(tokens: list[str]) -> dict[str, int]`  
   - Подсчитать частоты, вернуть словарь `слово → количество`.
  
```python
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
```

```python
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
```
![count_frq+top_n](images/lab03/image04.png)

## Задание B*
Находится lab_03 -> text_status.py,
При вводе табличный вывод можно включить, введя `1` stdin или выключить `0` stdin

```python
from text import count_freq, top_n,normalize,tokenize
vhod = input("Введите текст строкой:\n")
fl = int(input("Табличный вывод.\n 0 - выключить \n 1 - включить\n"))
if fl!=0 and fl!=1:
    if type(fl) == int:
        raise ValueError("Нужно 1 или 0")
    else:
        raise TypeError("Нужно int")
vhod_norm = normalize(vhod)
vhod_tokenize = tokenize(vhod_norm)
vhod_freq = count_freq(vhod_tokenize)
top_5 = top_n(vhod_freq,5)
print(f"Всего слов: {len(vhod_tokenize)}\nУникальных слов: {len(count_freq(vhod_tokenize))}\nТоп-5")

len_generator = [len(i[0]) for i in top_5]
max_len = max(len_generator)
if max_len<=5:
    max_len = 5
count_generator = [len(str(i[1])) for i in top_5]
max_count = max(count_generator)
if max_count<=7:
    max_count = 7

if fl == 0:
    for i in top_5:
        slovo, count = i
        print(f"{slovo}:{count}")
else:
    len_generator = [len(i[0]) for i in top_5]
    max_len = max(len_generator)
    if max_len<=5:
        max_len = 5
    count_generator = [len(str(i[1])) for i in top_5]
    max_count = max(count_generator)
    if max_count<=7:
        max_count = 7
    print(f"слово{' '*(max_len-5)}| частота{' '*(max_count-7)}")
    print(f"{"-"*(max_len+max_count+2)}")
    for i in top_5:
        slovo, count = i
        print(f"{slovo}{' '*(max_len-len(slovo))}|{count}")
```
![B0](images/lab03/image05.png)

Если все слова маленькие, то табличный вывод такой(| ставится по уровню "слово"):
![B1](images/lab03/image06.png)
 