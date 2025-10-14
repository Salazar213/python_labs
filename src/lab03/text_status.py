from text import count_freq, top_n,normalize,tokenize
vhod = input()
vhod_norm = normalize(vhod)
vhod_tokenize = tokenize(vhod_norm)
vhod_freq = count_freq(vhod_tokenize)
top_5 = top_n(vhod_freq,5)
print(f"Всего слов: {len(vhod_tokenize)}\nУникальных слов: {len(count_freq(vhod_tokenize))})
