from lib.text import json_to_csv,csv_to_json,csv_to_xlsx
import argparse
from pathlib import Path
def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv",help="Конвертировать JSON в CSV")
    p1.add_argument("--input", dest="input", required=True,help="Путь к входному JSON файлу")
    p1.add_argument("--out", dest="output", required=True,help="Путь для сохранения CSV файла")

    p2 = sub.add_parser("csv2json",help="Конвертировать CSV в JSON")
    p2.add_argument("--input", dest="input", required=True,help="Путь к входному CSV файлу (с заголовком в первой строке)")
    p2.add_argument("--out", dest="output", required=True,help="Путь для сохранения JSON файла")

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--input", dest="input", required=True,help="Путь к входному CSV файлу")
    p3.add_argument("--out", dest="output", required=True,help="Путь для сохранения XLSX файла")

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """
    if args.cmd == "json2csv":
        path_in = args.input
        path_ou = Path(args.out)
        json_to_csv(path_in,path_ou)


    elif args.cmd == "csv2json":
        path_in = args.input
        path_ou = Path(args.out)
        csv_to_json(path_in,path_ou)


    elif args.cmd =='csv2xlsx':
        path_in = args.input
        path_ou = Path(args.out)
        csv_to_xlsx(path_in,path_ou)