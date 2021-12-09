import os
from pathlib import Path


class PUtils:
    """Вспомогательный класс для работы с путями и папками"""
    @staticmethod
    def bp(*args):
        """
            Построение пути из набора папок:
            Пример
            -----
            bp('media', 'home', 'user') -> './media/home/user'
        """
        return os.path.normpath(os.path.join(*args))

    # Reference https://stackoverflow.com/a/44228213
    @staticmethod
    def is_file_exists(path):
        """Проверка на существование файла"""
        return Path(path).exists() and Path(path).is_file()