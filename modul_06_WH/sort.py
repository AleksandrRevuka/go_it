"""Sort garbage"""
import os
import sys
import shutil
from typing import NamedTuple
# from prettytable import PrettyTable


class InfoFile(NamedTuple):
    """File information"""
    name: str
    extension: str
    path: str
    old_path: str


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
    documents = {}
    audio = {}
    archives = {}
    unknown_extensions = {}
    print(len(data))

    for key, file_info in data.items():
        file_extension = file_info.extension
        if file_extension.upper() in IMAGES_EXTENSIONS:
            images[key] = ['images', file_info]

        elif file_extension.upper() in VIDEO_EXTENSIONS:
            video[key] = ['video', file_info]

        elif file_extension.upper() in DOCUMENTS_EXTENSIONS:
            documents[key] = ['documents', file_info]

        elif file_extension.upper() in AUDIO_EXTENSIONS:
            audio[key] = ['audio', file_info]

        elif file_extension.upper() in ARCHIVES_EXTENSIONS:
            archives[key] = ['archives', file_info]

        else:
            unknown_extensions[key] = file_info
    folders = [images, video, documents, audio, archives, unknown_extensions]
    
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
            file_info = InfoFile(name_file, extension, path, None)
            files_info_data[id(object)] = file_info
            
        else:
            if path == root_directory:
                if object.lower() not in ['images', 'video', 'documents', 'audio', 'archives']:
                    files_info_data = scan_files_and_folders(object_full)
            else:
                files_info_data = scan_files_and_folders(object_full)

    return files_info_data


def print_list_fails(folders_data: list, unknown_extensions) -> None:
    """Print"""
    images, video, documents, audio, archives = folders_data[:-1]
    
    folder_img = []
    for file_img in images.values():
        folder_img.append(file_img[1].name + file_img[1].extension)
        folder_name = file_img[0]
    print(f"List with {folder_name}: {folder_img} \n")
    
    folder_video = []
    for file_video in video.values():
        folder_video.append(file_video[1].name + file_video[1].extension)
        folder_name = file_video[0]
    print(f"List with {folder_name}: {folder_video} \n")
    
    folder_documents = []
    for file_doc in documents.values():
        folder_documents.append(file_doc[1].name + file_doc[1].extension)
        folder_name = file_doc[0]
    print(f"List with {folder_name}: {folder_documents} \n")
    
    folder_audio = []
    for file_audio in audio.values():
        folder_audio.append(file_audio[1].name + file_audio[1].extension)
        folder_name = file_audio[0]
    print(f"List with {folder_name}: {folder_audio} \n")
    
    folder_archives = []
    for file_archives in archives.values():
        folder_archives.append(file_archives[1].name + file_archives[1].extension)
        folder_name = file_archives[0]
    print(f"List with {folder_name}: {folder_archives} \n")
    
    
    folder_un_ext = []
    for file_un_ext in unknown_extensions.values():
        folder_un_ext.append(file_un_ext.extension)
    print(f"List with unknown_extensions: {list(set(folder_un_ext))} \n")
    

def normalization_and_file_movement_controller(folder_data: list, path: str):
    """Controller"""
    new_files_info_data = {}
    for data in folder_data[:-1]:
        for key, file_data in data.items():

            normalize_name = normalize(file_data[1].name)
            normalize_name_path = ''.join(path + '/' + file_data[0])
            normalize_name_with_path = os.path.join(normalize_name_path, normalize_name + file_data[1].extension)

            if not os.path.exists(normalize_name_with_path):
                # shutil.move(file_old, normalize_name_with_path)
                new_files_info_data[key] = InfoFile(normalize_name, file_data[1].extension, normalize_name_path, file_data[1].path)
            else:
                copy_number = 1
                while True:    
                    new_name = f"{normalize_name}_copy{copy_number}"
                    new_path = os.path.join(normalize_name_path, new_name + file_data[1].extension)
                    
                    if not os.path.exists(new_path):
                        # shutil.move(file_old, new_path)
                        new_files_info_data[key] = InfoFile(normalize_name, file_data[1].extension, normalize_name_path, file_data[1].path)
                        break
                    copy_number += 1
                    
    return new_files_info_data                


def main(folder: str):
    """Main controller"""
    print(folder)
    files_info = scan_files_and_folders(folder, folder)
    # check_for_repetition_of_names(files_info)
    # print(files_info)
    folders_with_files = sorting_files_into_folders(files_info)
    unknown_extensions_folder = folders_with_files[-1]
    files_info_new = normalization_and_file_movement_controller(folders_with_files, folder)
    folders_with_files_new = sorting_files_into_folders(files_info_new)
    print_list_fails(folders_with_files_new, unknown_extensions_folder)


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
    DOCUMENTS_EXTENSIONS = ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
    AUDIO_EXTENSIONS = ['.MP3', '.OGG', '.WAV', '.AMR']
    ARCHIVES_EXTENSIONS = ['.ZIP', '.GZ', '.TAR', '.RAR']

    folder_path = parse_path()
    if is_folder(folder_path):
        main(folder_path)
    else:
        print("Something wrong, try again")


# ['images', 'video', 'documens', 'audio', 'archives']

# python modul_06_WH/sort.py /home/alex/Desktop/garbage
