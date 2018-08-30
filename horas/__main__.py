# -*- coding: utf-8 -*-

import sys
import webbrowser
import datetime
import os.path
from pathlib import Path
from utils import get_OS, get_errors

now = datetime.datetime.now()
schedule_file = str(Path.home())+'/projectsSchedule.md'

# ARGS
# 1 OPTION
# 2 PROJECT
# 3 HOURS
# 4 DATE (OPTIONAL)
num_args = len(sys.argv)


def check_horas_file():
    if not os.path.exists(schedule_file):
        reset_horas()


def reset_horas():
    with open(schedule_file, 'w', encoding='UTF-8') as file:
        if("es" in get_OS().get('lang')):
            file.write('## Registro de Proyectos\n\n')
            file.write('| Proyecto | Horas |   Dia  |\n')
            file.write('|----------|:-----:|:------:|\n')
        else:
            file.write('## Project Schedule\n\n')
            file.write('| Project | Hours |   Day  |\n')
            file.write('|---------|:-----:|:------:|\n')
        file.close()


def show_horas():
    chrome_path = Path(get_OS().get('chrome'))
    try:
        chrome_path.is_dir()
        chrome = get_OS().get('chrome')
        webbrowser.get(chrome).open(
            'file:///'+schedule_file)
    except webbrowser.Error:
        print(get_errors().get('chrome_error'))
        with open(schedule_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line)
            file.close()
    except:
        raise Exception()


def new_horas():
    if num_args == 5:
        nueva_fila = '| ' + sys.argv[2] + ' | ' + \
            sys.argv[3] + 'h | ' + sys.argv[4] + ' |\n'
    elif num_args == 4:
        nueva_fila = '| ' + \
            sys.argv[2] + ' | ' + sys.argv[3] + \
            'h | ' + now.strftime("%d/%m") + ' |\n'
    else:
        raise Exception()

    with open(schedule_file, 'a') as file:
        file.write(nueva_fila)
        file.close()


def delete_last_horas():
    with open(schedule_file, 'r') as file:
        lines = file.readlines()
        file.close()

    lines = lines[0:len(lines)-1]
    with open(schedule_file, 'w') as file:
        for line in lines:
            file.write(line)
        file.close()


def main():
    check_horas_file()
    try:
        if (sys.argv[1] in ['-s', '--show']):
            show_horas()
        elif (sys.argv[1] in ['-r', '--reset']):
            reset_horas()
        elif (sys.argv[1] in ['-n', '--new']):
            new_horas()
        elif (sys.argv[1] in ['-d', '--delete']):
            delete_last_horas()
        else:
            raise Exception()
    except:
        print(get_errors().get('help_msg'))


if __name__ == '__main__':
    main()
