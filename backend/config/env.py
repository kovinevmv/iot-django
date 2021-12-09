import os
import pathlib

from dotenv import load_dotenv

from backend.utils.pUtils import PUtils

_current_file_path = pathlib.Path(__file__).parent.absolute()


def parse_dotenv():
    base_dir = PUtils.bp(_current_file_path, '..', '..')
    env = PUtils.bp(base_dir, '.env')
    env_example = PUtils.bp(base_dir, '.env.example')

    load_dotenv(env if PUtils.is_file_exists(env) else env_example)

    _SECRET_KEY = os.getenv("SECRET_KEY")
    if not _SECRET_KEY:
        raise Exception('Secret key is not provided')

    _DEBUG = os.getenv('DEBUG', 'True') == 'True'

    _DB_NAME = os.getenv('DB_NAME')
    _DB_USER = os.getenv('DB_USER')
    _DB_PASSWORD = os.getenv('DB_PASSWORD')
    _DB_HOST = os.getenv('DB_HOST')
    _DB_PORT = os.getenv('DB_PORT')

    if not _DB_NAME or not _DB_USER or not _DB_PASSWORD or not _DB_HOST or not _DB_PORT:
        raise Exception('Database connection is not provided')

    _DB_PORT = int(_DB_PORT)

    _SECURE_ADMIN_URL = os.getenv('SECURE_ADMIN')

    SUPER_USER = {
        'first_name': os.getenv('SUPERUSER_FIRST_NAME'),
        'last_name': os.getenv('SUPERUSER_LAST_NAME'),
        'snils': os.getenv('SUPERUSER_SNILS'),
        'gender': os.getenv('SUPERUSER_GENDER'),
        'email': os.getenv('SUPERUSER_EMAIL'),
        'password': os.getenv('SUPERUSER_PASSWORD')
    }

    return _SECRET_KEY, _DEBUG, _DB_NAME, _DB_USER, _DB_PASSWORD, _DB_HOST, _DB_PORT, \
           _SECURE_ADMIN_URL, SUPER_USER
