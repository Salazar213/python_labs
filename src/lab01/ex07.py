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
        shag = j + 1
        break
for l in range(0, len(stroka), shag):
    no_chiper += stroka[l]

print(no_chiper)
