"""Sort garbage"""
import os
import sys
import shutil
from typing import NamedTuple
from prettytable import PrettyTable


class InfoFile(NamedTuple):
    """File information"""
    name: str
    extension: str
    path: str


def is_folder(test_path: str) -> bool:
    """Checking the path for correctness"""
    if os.path.isdir(test_path):
        return True
    return False


def parse_path() -> str:
    """Get path from input data"""
    return "".join(arg for arg in sys.argv[1])


def normalize(name: str) -> str:
    """Converts Cyrillic to Latin and assigns characters to '_'."""

    trans = {}
    for key, value in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        trans[ord(key)] = value
        trans[ord(key.upper())] = value.upper()

    trans_name = ''.join(
        '_' if symbol in PUNCTUATION else symbol for symbol in name)

    return trans_name.translate(trans)


def check_for_repetition_of_names(data):
    """Check for repetition of names"""
    ...


def sorting_files_into_folders(data):
    """Sorting files into folders"""
    images = {}
    video = {}
    documens = {}
    audio = {}
    archives = {}
    unknown_extensions = {}
    print(len(data))

    for key, file_info in data.items():
        file_extension = file_info.extension
        if file_extension.upper() in IMAGES_EXTENSIONS:
            images[key] = file_info

        elif file_extension.upper() in VIDEO_EXTENSIONS:
            video[key] = file_info

        elif file_extension.upper() in DOCUMENS_EXTENSIONS:
            documens[key] = file_info

        elif file_extension.upper() in AUDIO_EXTENSIONS:
            audio[key] = file_info

        elif file_extension.upper() in ARCHIVES_EXTENSIONS:
            archives[key] = file_info

        else:
            unknown_extensions[key] = file_info
    folders = [images, video, documens, audio, archives, unknown_extensions]
    # print(f'{images}\n\n')
    # print(f'\n\n{video}')
    # print(f'\n\n{documens}')
    # print(f'\n\n{audio}')
    # print(f'\n\n{archives}')
    # print(f'\n\n{unknown_extensions}')
    return folders


def scan_files_and_folders(path: str, root_directory=None, files_info_data={}) -> dict:
    """
    Scans the specified directory and all its subdirectories for files and folders, 
    and returns a dictionary containing information about each file found.
    """

    objects = os.listdir(path)

    for object in objects:
        object_full = os.path.join(path, object)

        if os.path.isfile(object_full):
            name_file, extension = os.path.splitext(
                os.path.basename(object_full))
            file_info = InfoFile(name_file, extension, path)

            if object in files_info_data:
                copy_number = 1
                while f"{name_file}_copy{copy_number}{extension}" in files_info_data:
                    copy_number += 1
                object = f"{name_file}_copy{copy_number}{extension}"

            files_info_data[object] = file_info
        else:
            if path == root_directory:
                if object.lower() not in ['images', 'video', 'documents', 'audio', 'archives']:
                    files_info_data = scan_files_and_folders(object_full)
            else:
                files_info_data = scan_files_and_folders(object_full)

    return files_info_data


def print_list_fails(folders_data: list) -> None:
    """Print"""
    images, video, documens, audio, archives, unknown_extensions = folders_data
    
    images_folder = ['images', [file_img.name + file_img.extension
                                for file_img in images.values()]]
    video_folder = ['video', [file_video.name + file_video.extension
                              for file_video in video.values()]]
    documens_folder = ['documents', [file_doc.name + file_doc.extension
                                     for file_doc in documens.values()]]
    audio_folder = ['audio', [file_audio.name + file_audio.extension
                              for file_audio in audio.values()]]
    archives_folder = ['archives', [file_archive.name + file_archive.extension
                                    for file_archive in archives.values()]]
    unknown_extensions_folder = ['nknown_extensions', list(set(file_info.extension
                                                               for file_info in unknown_extensions.values()))]

    folders = [images_folder, video_folder, documens_folder,
               audio_folder, archives_folder, unknown_extensions_folder]

    for folder in folders:
        print(f"List with {folder[0]}: {folder[1]}, '\n'")


def normalization_and_file_movement_controller(folder_data: list):
    """Controller"""
    # images, video, documens, audio, archives = folder_data[:-1]
    
    for data in folder_data[:-1]:
        for key, file_data in data.items():
            data[key][file_data.name] = normalize(file_data.name)
            print(file_data.name)


def main(folder: str):
    """Main controller"""
    print(folder)
    files_info = scan_files_and_folders(folder, folder)
    # check_for_repetition_of_names(files_info)
    folders_with_files = sorting_files_into_folders(files_info)
    normalization_and_file_movement_controller(folders_with_files)
    
    # print_list_fails(folders_with_files)


if __name__ == '__main__':
    PUNCTUATION = "#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"  # without "."
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = [
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l",
        "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh",
        "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
    ]

    IMAGES_EXTENSIONS = ['.JPEG', '.PNG', '.JPG', '.SVG', '.IMG']
    VIDEO_EXTENSIONS = ['.AVI', '.MP4', '.MOV', '.MKV']
    DOCUMENS_EXTENSIONS = ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
    AUDIO_EXTENSIONS = ['.MP3', '.OGG', '.WAV', '.AMR']
    ARCHIVES_EXTENSIONS = ['.ZIP', '.GZ', '.TAR', '.RAR']

    folder_path = parse_path()
    if is_folder(folder_path):
        main(folder_path)
    else:
        print("Something wrong, try again")


# ['images', 'video', 'documens', 'audio', 'archives']

# python modul_06_WH/sort.py /home/alex/Desktop/garbage
