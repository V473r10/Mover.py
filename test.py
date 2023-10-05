import json
import os
import platform
from main import separator

settings = json.load(open('settings.json'))
test_folder = settings['testFolder']


def make_folders():
    for format_name in settings['formats']:
        folder = format_name['folder']
        if not os.path.exists(f'{test_folder}{separator}{folder}'):
            os.makedirs(f'{test_folder}{separator}{folder}')


def make_files():
    for format_name in settings['formats']:
        folder = format_name['folder']
        for extension in format_name['extensions']:
            file_name = 'test.' + extension
            file_path = f'{test_folder}{separator}{file_name}'
            open(file_path, 'a').close()


# make_folders()
make_files()
