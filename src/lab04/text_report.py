from pathlib import Path
import argparse
from lib.text import normalize,tokenize,count_freq,top_n 

from lib.text import read_text, write_csv
paths = argparse.ArgumentParser()
paths.add_argument('--input',type=str, default="C:/python_labs_alg/python_labs/data/a.txt",nargs='+')
paths.add_argument('--output',type=str,default="C:/python_labs_alg/python_labs/data/out.csv")
paths.add_argument('--encoding', type =str, default='utf-8')
args = paths.parse_args()
path_in = list(map(Path,(args.input)))
path_ou = Path(args.output)
encoding = args.encoding
if len(path_in)>1:
        for path in path_in:
                if not(path.exists()):
                        raise FileNotFoundError(f'Файл не найден по пути {path}')
path_ou.parent.mkdir(parents=True, exist_ok=True)
dict_all = []
path_in.sort(key=lambda x: x.name)
if len (path_in) !=1:
        write_csv(rows=[], path="C:/python_labs_alg/python_labs/data/reprot_per_file.csv", header=("file",'word','count'))
        for path in path_in:
                text = read_text(path= path,encoding=encoding)
                text_normalize = normalize(text)
                text_tokenize = tokenize(text_normalize)
                text_freq = count_freq(text_tokenize)
                dict_all.append(text_freq)

                top_5 = top_n(text_freq)
                # text_freq = [(word,count) for word, count in text_freq.items()]
                text_freq = top_n(text_freq, len(text_freq))
                text_freq_file = list()
                for element in text_freq:
                        text_freq_file.append((str(path.name),)+element)
                header = tuple()
                write_csv(rows=text_freq_file, path="C:/python_labs_alg/python_labs/data/reprot_per_file.csv",type_write='a')
                
                # print(f"Всего слов: {len(text_tokenize)}\nУникальных слов: {len(text_freq)}\nТоп-5")

                # for i in top_5:
                # slovo, count = i
                # print(f"{slovo}:{count}")
        result_summa_dict = {}
        for d in dict_all:
                for key, value in d.items():
                        result_summa_dict[key] = result_summa_dict.get(key,0) + value
        result_summa_dict = top_n(result_summa_dict,len(result_summa_dict))
        write_csv(rows= result_summa_dict, path ="C:/python_labs_alg/python_labs/data/report_total.csv", header=('word','count'))
elif len(path_in)==1:   
        path_in=path_in[0]
        text = read_text(path = path_in,encoding=encoding)
        text_normalize = normalize(text)
        text_tokenize = tokenize(text_normalize)
        text_freq = count_freq(text_tokenize)
        top_5 = top_n(text_freq)
        text_freq = top_n(text_freq, len(text_freq))
        write_csv(rows=text_freq, path=path_ou, header=('word','count'))
        print(f"Всего слов: {len(text_tokenize)}\nУникальных слов: {len(text_freq)}\nТоп-5")
        len_generator = [len(i[0]) for i in top_5]
        if len(len_generator)!=0:
                max_len = max(len_generator)
        else:
                max_len = 0
        if max_len<=5:
                max_len = 5
        count_generator = [len(str(i[1])) for i in top_5]
        if len(count_generator)!=0:
                max_count = max(count_generator)
        else:
                max_count = 0
        if max_count<=7:
                max_count = 7
        print(f"слово{' '*(max_len-5)}| частота{' '*(max_count-7)}")
        print(f"{"-"*(max_len+max_count+2)}")
        for i in top_5:
                slovo, count = i
                print(f"{slovo}{' '*(max_len-len(slovo))}| {count}")

else:
        write_csv(path=path_ou,rows=[],header=('word','count'))