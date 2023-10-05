import json
import os
import pathlib
import platform

settings = json.load(open('settings.json'))
target_folder = settings['targetFolder']

counts = {}

separator = ''

if platform.system() != 'Windows':
    separator = '/'
else:
    separator = '\\'


def initialize_counts_object():
    for format_name in settings['formats']:
        counts[format_name['name']] = 0
    counts['Others'] = 0


def get_files():
    files = os.listdir(target_folder)
    # remove directories from list
    files = [file for file in files if os.path.isfile(os.path.join(target_folder, file))]
    # remove desktop.ini files from list
    files = [file for file in files if file != 'desktop.ini']
    return files


def get_file_format(file):
    extension = pathlib.Path(file).suffix[1:]
    for format_name in settings['formats']:
        if extension in format_name['extensions']:
            return format_name['name']


def process_other_files(file):
    if not os.path.exists(target_folder + f'{separator}Others'):
        os.makedirs(target_folder + f'{separator}Others')
    new_path = target_folder + f'{separator}Others{separator}' + file
    os.rename(file_path, new_path)


def process_files():
    for format_object in settings['formats']:
        if file_format == format_object['name']:
            folder = format_object['folder']
            # new_file_path = target_folder + '\\' + folder + '\\' + _file
            new_file_path = f'{target_folder}{separator}{folder}{separator}{_file}'
            # Move file to folder
            if not os.path.exists(f'{target_folder}{separator}{folder}'):
                os.makedirs(f'{target_folder}{separator}{folder}')
            os.rename(file_path, new_file_path)
            counts[format_object['name']] += 1
            break


def print_counts():
    print('Files sorted:')
    for key, value in counts.items():
        print(key, ':', value)


if __name__ == '__main__':
    initialize_counts_object()

    if settings['testMode']:
        import test
        test.make_folders()
        test.make_files()
        target_folder = settings['testFolder']

    for _file in get_files():
        file_format = get_file_format(_file)
        file_path = f'{target_folder}{separator}{_file}'
        if file_format is None:
            process_other_files(_file)

        process_files()
    print_counts()
