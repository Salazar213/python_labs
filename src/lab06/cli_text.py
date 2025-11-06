from lib.text import count_freq, count_freq_top,read_text,normalize,tokenize,top_n
import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        cat_input = args.input
        cat_n = args.n
        i_stroka = 1
        cat_input = Path(cat_input)
        if not(cat_input.exists()):
            raise FileNotFoundError('Файл не найден')
        try:
            with cat_input.open('r',encoding = 'utf-8') as d:
                if cat_n:
                    for line in d.readlines():
                        print(f'{i_stroka} строка: {line}',end='')
                        i_stroka+=1
                else:
                    for line in d.readlines():
                        print(f'{line}',end='')
        except:
            raise UnicodeDecodeError('Не удалось прочитать файл')
            """ Реализация команды cat """
    elif args.command == "stats":
        stars_input = args.input
        stats_top_n = args.top
        stars_input = Path(stars_input)
        if not(stars_input.exists()):
            raise FileNotFoundError(f"Файл не найден по пути {stars_input}")
        try:
            text = read_text(path= stars_input)
        except:
            raise UnicodeEncodeError("Ошибка чтения файла")
        if not(type(stats_top_n) == int):
            raise TypeError(f"Ошибка type(n) = {type(stats_top_n)}, а должен быть int")

        text_normalize = normalize(text)
        text_tokenize = tokenize(text_normalize)
        text_freq = count_freq(text_tokenize)
        text_top = top_n(text_freq,stats_top_n)
        print('word','count')
        for word, count in text_top:
            print(word,count)
        """ Реализация команды stats """