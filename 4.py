# подключаем модуль разбора параметров командной строки
import argparse
# подключаем модуль sys
import sys
import os

"""
    Напишите аналог утилиты tree, которая отображает древовидную структуру каталогов и файлов. Пример работы программы:

    python3 ./tree.py ~/file
    Указанный путь не существует или не является папкой


    python3 ./tree.py ~/test


    /home/user/test
       -T
          4.txt
       a
          1.txt
          2.txt
       b
          3.txt

    Программа должна поддерживать следующие опции командной строки:

        --folders-only — не отображать файлы в дереве;
        --include SOME_TEXT — отображать только те элементы, в названии которых встречается текст SOME_TEXT
        --exclude SOME_TEXT — не отображать те элементы, в названии которых встречается текст SOME_TEXT

    Для разбора параметров используйте модуль argparse.
"""

# эта функция делает основную работу
def print_tree(items,tab_count,incl,excl,fo):
    # рекурсивно печатает список items как фрагмент дерева вглубь, оставляя слева отступ tab_count
    # учитывает фильтры include, exclude, folders-only
    for i in items:
        if os.path.isdir( os.path.join(os.getcwd(),i) ):
            print(' '*(tab_count), i)
            save_dir=os.getcwd() # запомним текущую директорию
            os.chdir(i) # перейдем на уровень глубже
            print_tree(os.listdir(os.getcwd()),tab_count+4,incl,excl,fo) # рекурсия
            os.chdir(save_dir) # вернемся в родительскую деректорию
        else: # это файл и к нему надо применить все фильтры
            if not fo: # опция --folders-only
                if not incl or str(i).count(incl)>0:  # если есть опция --include учтем фильтр включения
                    if not excl or str(i).count(excl)==0: # если есть опция --exclude учтем фильтр исключения
                        print(' '*(tab_count+4), i)



# создаём парсер и описываем все параметры командной строки, которые может
# принимать наша программа
parser = argparse.ArgumentParser(
    # краткое описание программы
    description='Pethon TREE'
)


# описываем позиционные параметры
parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values',
    # название параметров, которое будет отображено в справке
    metavar='VALUES',
    # сообщаем парсеру, что ожидаются строки - это тип по-умолчанию
    #type=float,
    # параметров будет не меньше одного
    nargs='+',
    # краткое описание параметров
    help='входные данные'
)

# описываем опцию --include
parser.add_argument(
    # короткое название опции
    '-i',
    # длинное название опции
    '--include',
    # название параметра, которое будет отображено в справке
    metavar='VALUE',
    # сообщаем парсеру, что ожидаются строки - это тип по-умолчанию
    #type=float,
    # парсер сохранит значение параметра, если встретит эту опцию
    action='store',
    # краткое описание опции
    help='отображать только те элементы, в названии которых встречается текст SOME_TEXT'
)
# описываем опцию --exclude
parser.add_argument(
    # короткое название опции
    '-e',
    # длинное название опции
    '--exclude',
    # название параметра, которое будет отображено в справке
    metavar='VALUE',
    # сообщаем парсеру, что ожидаются строки - это тип по-умолчанию
    #type=float,
    # парсер сохранит значение параметра, если встретит эту опцию
    action='store',
    # краткое описание опции
    help='не отображать те элементы, в названии которых встречается текст SOME_TEXT'
)
# описываем опцию --folders-only
parser.add_argument(
    # короткое название опции
    '-f',
    # длинное название опции
    '--folders-only',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='вывести только имена папок'
)
# вызываем функцию разбора параметров командной строки
args = parser.parse_args()

# проверяем, что есть хотя бы один из параметров
if len(args.values)==0:
    # выводим сообщение об ошибке в стандартный поток вывода ошибок (stderr)
    print('Укажите хотя бы один путь')
    # завершаем программу
    sys.exit(-1)
# проверим, что все указанные пути существуют
values = args.values
for v in values:
    if not os.path.exists(v):
        print('Указанный путь не существует или не является папкой')
        # завершаем программу
        sys.exit(-1)

# выведем дерево с учетом условий --include и --exclude
tab_count=0 # счетчик отступов

print_tree(values,tab_count,args.include,args.exclude,args.folders_only)

