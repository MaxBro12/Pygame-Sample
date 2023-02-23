from core import get_os, read, write
from settings import game_config, game_config_name


from os.path import exists


def main_check():
    # ? Проверяем файлы
    check_data()

    data = read(game_config_name)
    data['MAIN']['os'] = get_os()

    # ! Обработка ошибки файла конфига
    # if not data:
    #     raise ConfigException

    return data


def check_data():
    if not exists(game_config_name):
        write(game_config, game_config_name)
