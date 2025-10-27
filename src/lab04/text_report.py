from pathlib import Path
import argparse
from text import normalize,tokenize,count_freq,top_n
from text import read_text, write_csv
paths = argparse.ArgumentParser()
paths.add_argument('--input',type=str, default="data/a.txt data/b.txt")
paths.add_argument('--output',type=str,default="data/lab04/out.csv")
paths.add_argument('--encoding', type =str, default='utf-8')
args = paths.parse_args()
path_in = list(map(Path,((args.input).split())))
path_ou = Path(args.output)
encoding = args.encoding
for path in path_in:
        if not(path.exists()):
                raise FileNotFoundError(f'Файл не найден по пути {path}')
path_ou.parent.mkdir(parents=True, exist_ok=True)
dict_all = []
path_in.sort(key=lambda x: x.name)
if len (path_in) !=1:
        write_csv(rows=[], path="data/reprot_per_file.csv", header=("file",'word','count'))

        for path in path_in:
                text = read_text(path= path,encoding=encoding)
                text_normalize = normalize(text)
                text_tokenize = tokenize(text_normalize)
                text_freq = count_freq(text_tokenize)
                top_5 = top_n(text_freq)
                # text_freq = [(word,count) for word, count in text_freq.items()]
                text_freq = top_n(text_freq, len(text_freq))
                text_freq_file = list()
                for element in text_freq:
                        text_freq_file.append((str(path.name),)+element)
                dict_all.append(text_freq)
                header = tuple()
                write_csv(rows=text_freq_file, path="data/reprot_per_file.csv",type_write='a')
                
                # print(f"Всего слов: {len(text_tokenize)}\nУникальных слов: {len(text_freq)}\nТоп-5")

                # for i in top_5:
                # slovo, count = i
                # print(f"{slovo}:{count}")