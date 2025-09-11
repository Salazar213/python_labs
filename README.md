# ** Лабораторная работа №1**
### Задача 1
```python
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age+1}.")
```
![рис. 1 — пример выполнения ](../../images\image01.png)
### Задача 2 
```python
a = float(input("a: ").replace(',','.'))
b = float(input("b: ").replace(',','.'))
print (f"sum: {a+b:.2f} avg: {(a+b)/2:.2f}")
```
Возможность вводить числа через запятую реализована с помощью ```replace```
![рис.2 - пример выполнения](../../images\image02.png)
### Задача 3
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
![рис.3 - пример выполненяия](../../images\image03.png) 
### Задача 4
```python
m = int(input("Минуты "))
print(f"{m//60}:{(m%60):02d}")
```
Формат времени с впередистоящими нулями реализован через `:02d`
![рис.4 - пример выполнения](../../images/image04.png)
### Задача 5
```python
name, surname, patronymic  = input("ФИО: ").split()
initials = f"{name[0]}.{surname[0]}.{patronymic[0]}."
print(f"Инициалы: {initials}\nДлина: {len(name + surname + patronymic)+2}")
```
![рис.5 - пример выполнения](../../images/image05.png)
### Задача 6

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
![рис.6 - пример выполнения](../../images/image06.png)
### Задача 7
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
![рис.7 - пример выполнения](../../images/image07.png)
