from text import count_freq, top_n,normalize,tokenize
vhod = input("Введите текст строкой")
fl = input("Табличный вывод.\n 0 - выключить \n 1 - включить")

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