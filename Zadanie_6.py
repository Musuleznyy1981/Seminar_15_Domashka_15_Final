# Мусулезный Максим 03.09.2023
# Задание №6
# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.


import  argparse
import Seminar_15.dir_walker


def parse_ars():
    parser = argparse.ArgumentParser(description="zd15t03_s15t09")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директорию')
    args = parser.parse_args()
    return args.p

def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))

if __name__ == '__main__':
    main()