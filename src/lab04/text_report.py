from pathlib import Path
import argparse
from text import normalize,tokenize,count_freq,top_n
from text import read_text, write_csv
paths = argparse.ArgumentParser()
paths.add_argument('--input',type=str, default="data/lab04/input.txt")
paths.add_argument('--output',type=str,default="data/lab04/out.csv")
paths.add_argument('--encoding', type =str, default='utf-8')
args = paths.parse_args()
path_in = Path(args.input)
path_ou = Path(args.output)
encoding = args.encoding
if not(path_in.exists()):
        raise FileNotFoundError('Файл не найден')
path_ou.parent.mkdir(parents=True, exist_ok=True)
text = read_text(path = path_in,encoding=encoding)
text_normalize = normalize(text)
text_tokenize = tokenize(text_normalize)
text_freq = count_freq(text_tokenize)
top_5 = top_n(text_freq)
# text_freq = [(word,count) for word, count in text_freq.items()]
text_freq = top_n(text_freq, len(text_freq))
write_csv(rows=text_freq, path=path_ou, header=('word','count'))
print(f"Всего слов: {len(text_tokenize)}\nУникальных слов: {len(text_freq)}\nТоп-5")

for i in top_5:
    slovo, count = i
    print(f"{slovo}:{count}")