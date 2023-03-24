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
    folder: str
    new_name: str


def is_folder(test_path: str) -> bool:
    """Checking the path for correctness"""
    if os.path.isdir(test_path):
        return True
    return False


def parse_path() -> str:
    """Get path from input data"""
    return "".join(arg for arg in sys.argv[1])


def get_max_depth(path):
    """
    Returns the greatest folder nesting depth for the given path.
    """
    max_depth = 0
    for root, dirs, files in os.walk(path):
        depth = root.count(os.sep)
        if depth > max_depth:
            max_depth = depth
    return max_depth


def normalize(name: str) -> str:
    """Converts Cyrillic to Latin and assigns characters to '_'."""

    trans = {}
    for key, value in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        trans[ord(key)] = value
        trans[ord(key.upper())] = value.upper()

    trans_name = ''.join(
        '_' if symbol in PUNCTUATION else symbol for symbol in name)

    return trans_name.translate(trans)


def check_for_repetition_of_names(path: str, folder: str, name: str, extension: str) -> str:
    """Check for repetition of names"""
    file_path = os.path.join(path, folder)
    file_path_full = os.path.join(file_path, name + extension)
    if os.path.exists(file_path_full):
        copy_number = 1
        while True:
            new_name = f"{name}_copy{copy_number}"
            new_path = os.path.join(file_path, new_name + extension)

            if not os.path.exists(new_path):
                return new_name
            copy_number += 1
    else:
        return name


def  extract_files_from_archive(file_info: InfoFile):
    """Extract files from archive"""
    archive_path = os.path.join(file_info.old_path, file_info.new_name + file_info.extension)
    
    path_to_unpack = os.path.join()
    shutil.unpack_archive(archive_path, path_to_unpack)


def move_the_file(file_info: InfoFile):
    """Move the file"""
    file_old = os.path.join(file_info.old_path, file_info.name + file_info.extension)
    path_file_new = os.path.join(file_info.path, file_info.folder)
    file_new = os.path.join(path_file_new, file_info.new_name)
    shutil.move(file_old, file_new)


def write_the_file_info_to_the_file(file_info: InfoFile):
    """Write the file info to the file"""
    ...


def file_controller(file_info: InfoFile):
    """Controller"""
    file_name_normal = normalize(file_info.name)
    file_name_new = check_for_repetition_of_names(file_info.path, file_info.folder, 
                                                    file_name_normal, file_info.extension)
    file_info_new = InfoFile(file_info.name, file_info.extension, file_info.path, 
                             file_info.old_path, file_info.folder, file_name_new)
    
    if DIRECTORY['archives'] == file_info.folder:
        extract_files_from_archive(file_info)
    else:
        move_the_file(file_info_new)
        
    write_the_file_info_to_the_file(file_info_new)


def sorting_files_into_folders(file_info: InfoFile) -> InfoFile:
    """Sorting files into folders"""

    file_extension = file_info.extension
    if file_extension.upper() in IMAGES_EXTENSIONS:
        file_info_new = InfoFile(file_info.name, file_info.extension,
                                 file_info.path, file_info.old_path, DIRECTORY['images'], None)
        file_controller(file_info_new)

    elif file_extension.upper() in VIDEO_EXTENSIONS:
        file_info_new = InfoFile(file_info.name, file_info.extension,
                                 file_info.path, file_info.old_path, DIRECTORY['video'], None)
        file_controller(file_info_new)

    elif file_extension.upper() in DOCUMENTS_EXTENSIONS:
        file_info_new = InfoFile(file_info.name, file_info.extension,
                                 file_info.path, file_info.old_path, DIRECTORY['documents'], None)
        file_controller(file_info_new)

    elif file_extension.upper() in AUDIO_EXTENSIONS:
        file_info_new = InfoFile(file_info.name, file_info.extension,
                                 file_info.path, file_info.old_path, DIRECTORY['audio'], None)
        file_controller(file_info_new)

    elif file_extension.upper() in ARCHIVES_EXTENSIONS:
        file_info_new = InfoFile(file_info.name, file_info.extension,
                                 file_info.path, file_info.old_path, DIRECTORY['archives'], None)
        file_controller(file_info_new)

    else:
        file_info_new = InfoFile(file_info.name, file_info.extension,
                                 file_info.path, file_info.old_path, DIRECTORY['unknown_extensions'], None)


def scan_files_and_folders(path: str, root_directory=None):
    """
    Scans the specified directory and all its subdirectories for files and folders, 
    and returns a dictionary containing information about each file found.
    """

    objects = os.listdir(path)

    for unk_object in objects:
        object_path = os.path.join(path, unk_object)

        if os.path.isfile(object_path):
            name_file, extension = os.path.splitext(
                os.path.basename(object_path))
            file_info = InfoFile(name_file, extension,
                                 root_directory, path, None, None)
            sorting_files_into_folders(file_info)

        else:
            if path == root_directory:
                if unk_object.lower() not in DIRECTORY:
                    scan_files_and_folders(object_path, root_directory)
            else:
                scan_files_and_folders(object_path, root_directory)


def print_list_fails(folders_data: list, extensions_data) -> None:
    """Print"""
    images, video, documents, audio, archives = folders_data
    unknown_extensions, known_extensions = extensions_data

    if images:
        folder_img = []
        for file_img in images.values():
            folder_img.append(file_img[1].name + file_img[1].extension)
            folder_name = file_img[0]
        print(f"List with {folder_name}: {folder_img} \n")

    if video:
        folder_video = []
        for file_video in video.values():
            folder_video.append(file_video[1].name + file_video[1].extension)
            folder_name = file_video[0]
        print(f"List with {folder_name}: {folder_video} \n")

    if documents:
        folder_documents = []
        for file_doc in documents.values():
            folder_documents.append(file_doc[1].name + file_doc[1].extension)
            folder_name = file_doc[0]
        print(f"List with {folder_name}: {folder_documents} \n")

    if audio:
        folder_audio = []
        for file_audio in audio.values():
            folder_audio.append(file_audio[1].name + file_audio[1].extension)
            folder_name = file_audio[0]
        print(f"List with {folder_name}: {folder_audio} \n")

    if archives:
        folder_archives = []
        for file_archives in archives.values():
            folder_archives.append(
                file_archives[1].name + file_archives[1].extension)
            folder_name = file_archives[0]
        print(f"List with {folder_name}: {folder_archives} \n")

    if known_extensions:
        folder_kn_ext = []
        for file_kn_ext in known_extensions.values():
            folder_kn_ext.append(file_kn_ext.extension)
        print(f"List with known_extensions: {list(set(folder_kn_ext))} \n")

    if unknown_extensions:
        folder_un_ext = []
        for file_un_ext in unknown_extensions.values():
            folder_un_ext.append(file_un_ext.extension)
        print(f"List with unknown_extensions: {list(set(folder_un_ext))} \n")


def deletes_empty_folders(path_folder, root_directory):
    """Del"""
    for object in os.listdir(path_folder):
        object_full_path = os.path.join(path_folder, object)
        if os.path.isdir(object_full_path):

            if path_folder == root_directory:
                if object.lower() not in ['images', 'video', 'documents', 'audio', 'archives']:
                    if os.listdir(object_full_path):
                        deletes_empty_folders(object_full_path, root_directory)
                    else:
                        os.rmdir(object_full_path)
            else:
                if os.listdir(object_full_path):
                    deletes_empty_folders(object_full_path, root_directory)
                else:
                    os.rmdir(object_full_path)

        elif os.path.isfile(object_full_path):
            continue


def main(folder: str):
    """Main controller"""
    print(folder)
    max_depth = get_max_depth(folder)

    while max_depth > 0:
        print('_____________________max_depth: ', max_depth)
        scan_files_and_folders(folder, folder)

        max_depth -= 1
    # print_list_fails(folders_with_files_new, folders_extensions)

    max_depth = get_max_depth(folder)
    while max_depth > 0:
        print('_____________________max_depth: ', max_depth)
        deletes_empty_folders(folder, folder)
        max_depth -= 1


if __name__ == '__main__':
    PUNCTUATION = "#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"  # without "."
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = [
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l",
        "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh",
        "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
    ]

    DIRECTORY = {
        'images': 'images', 'video': 'video', 'documents': 'documents',
        'audio': 'audio', 'archives': 'archives', 'unknown_extensions':'unknown_extensions'
    }

    IMAGES_EXTENSIONS = ['.JPEG', '.PNG', '.JPG', '.SVG', '.IMG']
    VIDEO_EXTENSIONS = ['.AVI', '.MP4', '.MOV', '.MKV', '.FLV']
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
