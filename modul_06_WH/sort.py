"""Sort garbage"""
import os
import sys
import shutil

from typing import NamedTuple, List, Dict, Tuple
# from prettytable import PrettyTable

PUNCTUATION = "#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"  # without "."
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = [
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l",
    "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh",
    "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
]

DIRECTORY = {
    'images': 'images', 
    'video': 'video', 
    'documents': 'documents',
    'audio': 'audio', 
    'archives': 'archives', 
    'unknown_extensions': 'unknown_extensions'
}

IMAGES_EXTENSIONS = ['.JPEG', '.PNG', '.JPG', '.SVG', '.IMG']
VIDEO_EXTENSIONS = ['.AVI', '.MP4', '.MOV', '.MKV', '.FLV']
DOCUMENTS_EXTENSIONS = ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX']
AUDIO_EXTENSIONS = ['.MP3', '.OGG', '.WAV', '.AMR']
ARCHIVES_EXTENSIONS = ['.ZIP', '.GZ', '.TAR']

folders_ext = [IMAGES_EXTENSIONS, VIDEO_EXTENSIONS, DOCUMENTS_EXTENSIONS,
           AUDIO_EXTENSIONS, ARCHIVES_EXTENSIONS]

FOLDERS_WITH_EXT = dict(zip(DIRECTORY.values(), folders_ext))

current_dir = os.getcwd()
FILE_UN_EXT = os.path.join(current_dir, 'un_extension.txt')
FILE_KN_EXT = os.path.join(current_dir, 'kn_extension.txt')


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


def get_max_depth(path: str) -> int:
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
    """
    Converts Cyrillic characters in a string to their Latin equivalents, and replaces any 
    other non-alphanumeric or non-underscore characters with underscores. Returns the normalized 
    string.
    """

    trans = {}
    for key, value in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        trans[ord(key)] = value
        trans[ord(key.upper())] = value.upper()

    trans_name = ''.join(
        '_' if symbol in PUNCTUATION else symbol for symbol in name)

    return trans_name.translate(trans)


def check_for_repetition_of_names(file_info: InfoFile, name: str) -> str:
    """
    The function checks if a file with the given name already exists in the destination directory. 
    If it does, the function adds a "_copy{number}" suffix to the name and returns the new name. 
    If the new name is also taken, it increments the number and tries again until it finds an 
    available name. If the given name is not taken, the function returns the original name.
    """

    file_path = os.path.join(file_info.path, file_info.folder)
    file_extension = f"{name}{file_info.extension}"
    file_path_full = os.path.join(file_path, file_extension)

    if os.path.exists(file_path_full):
        copy_number = 1
        while True:
            new_name = f"{name}_copy{copy_number}"
            new_name_extension = f"{new_name}{file_info.extension}"
            new_path = os.path.join(file_path, new_name_extension)

            if not os.path.exists(new_path):
                return new_name
            copy_number += 1
    else:
        return name


def move_the_file(file_info: InfoFile) -> None:
    """The function moves a file from the old location to the new location."""

    file_name_extension = f"{file_info.name}{file_info.extension}"
    file_old = os.path.join(file_info.old_path, file_name_extension)
    path_file_new = os.path.join(file_info.path, file_info.folder)

    file_new_name_extension = f"{file_info.new_name}{file_info.extension}"
    file_new = os.path.join(path_file_new, file_new_name_extension)
    try:
        shutil.move(file_old, file_new)
    except PermissionError as error:
        print(error)
    except FileNotFoundError as error:
        print(error)


def extract_files_from_archive(file_info: InfoFile) -> None:
    """
    This function creates a new directory with the same name as the archive file in the 
    directory where the archive file is located. The files in the archive are then extracted 
    into this new directory using the `shutil.unpack_archive()` function from the `shutil` 
    module. 
    """

    archive_name = f"{file_info.new_name}{file_info.extension}"
    archive_path = os.path.join(file_info.path, file_info.folder)
    path_to_unpack = os.path.join(archive_path, file_info.new_name)
    archive_path_full = os.path.join(archive_path, archive_name)

    try:
        os.mkdir(path_to_unpack)
        shutil.unpack_archive(archive_path_full, path_to_unpack)
    except PermissionError as error:
        print(error)
    except RuntimeError:
        print(
            f"Archive {archive_name} is encrypted, password required for extraction")


def write_the_file_info_to_the_file(file_info: InfoFile) -> None:
    """
    This function writes the information about a file to a file named 'kn_extension.txt' if the 
    file belongs to a known extension and to a file named 'un_extension.txt' if the file belongs 
    to an unknown extension. The function takes an instance of the InfoFile class as an argument, 
    extracts the file information from it, and writes it to the appropriate file. The function 
    does not return anything.
    """

    data_file = [
        str(file_info.name),
        str(file_info.extension),
        str(file_info.path),
        str(file_info.old_path),
        str(file_info.folder),
        str(file_info.new_name)+'\n'
    ]
    data = ','.join(data_file)

    if file_info.folder == DIRECTORY["unknown_extensions"]:
        with open(FILE_UN_EXT, 'a', encoding='utf-8') as un_ext_file:
            un_ext_file.write(data)
    else:
        with open(FILE_KN_EXT, 'a', encoding='utf-8') as kn_ext_file:
            kn_ext_file.write(data)


def file_controller(file_info: InfoFile) -> None:
    """
    The function takes an InfoFile object and performs various operations 
    on it depending on its properties. It normalizes the file name, checks for any repetitions 
    of file names, creates a new InfoFile object with the normalized and checked file name, 
    and writes the file info to a file.

    If the file is in the archives folder, it moves the file to the appropriate folder and 
    extracts the files from the archive. Otherwise, it simply moves the file to the appropriate 
    folder.

    This function acts as a central control unit for the sorting and management of files 
    in the given path.
    """

    file_name_normal = normalize(file_info.name)
    file_name_new = check_for_repetition_of_names(file_info, file_name_normal)
    file_info_new = InfoFile(file_info.name,
                             file_info.extension,
                             file_info.path,
                             file_info.old_path,
                             file_info.folder,
                             file_name_new
                             )

    write_the_file_info_to_the_file(file_info_new)

    if DIRECTORY['archives'] == file_info.folder:
        move_the_file(file_info_new)
        extract_files_from_archive(file_info_new)
    else:
        move_the_file(file_info_new)


def check_extension(extension: str) -> str | bool:
    """
    Check if the given file extension is present in the list of extensions associated 
    with any folder in the FOLDERS_WITH_EXT dictionary.
    """
    for key, ext in FOLDERS_WITH_EXT.items():
        if extension.upper() in ext:
            return key
    return False


def sorting_files_into_folders(file_info: InfoFile) -> None:
    """
    The function takes an InfoFile object, determines the file's extension and 
    categorizes the file into a respective directory based on the extension. The 
    function also calls the file_controller function and passes the InfoFile object to it.
    """

    folder = check_extension(file_info.extension)

    if folder:
        file_info_new = InfoFile(
            file_info.name,
            file_info.extension,
            file_info.path,
            file_info.old_path,
            folder,
            None
        )
        file_controller(file_info_new)
    else:
        file_info_new = InfoFile(
            file_info.name,
            file_info.extension,
            file_info.path,
            file_info.old_path,
            DIRECTORY['unknown_extensions'],
            None
        )
        write_the_file_info_to_the_file(file_info_new)


def scan_files_and_folders(path: str, root_directory: str) -> None:
    """
    Scans the specified directory and all its subdirectories for files and folders and 
    passes the file data as a named tuple to the sorting_files_into_folders function.
    """

    try:
        objects = os.listdir(path)

        for unk_object in objects:
            object_path = os.path.join(path, unk_object)

            if os.path.isfile(object_path):
                name_file, extension = os.path.splitext(
                    os.path.basename(object_path))
                file_info = InfoFile(name_file,
                                     extension,
                                     root_directory,
                                     path, None, None)
                sorting_files_into_folders(file_info)

            else:
                if path == root_directory:
                    if unk_object.lower() not in DIRECTORY:
                        scan_files_and_folders(object_path, root_directory)
                else:
                    scan_files_and_folders(object_path, root_directory)
    except PermissionError as error:
        print(error)


def sort_files_for_print(files_info: Dict[int, InfoFile]) -> None:
    """
    Displays the names of files that have been sorted into folders.
    """
    images = []
    video = []
    documents = []
    audio = []
    archives = []

    for file_info in files_info.values():
        if file_info.folder == DIRECTORY['images']:
            images.append(file_info.new_name + file_info.extension)

        if file_info.folder == DIRECTORY['video']:
            video.append(file_info.new_name + file_info.extension)

        if file_info.folder == DIRECTORY['documents']:
            documents.append(file_info.new_name + file_info.extension)

        if file_info.folder == DIRECTORY['audio']:
            audio.append(file_info.new_name + file_info.extension)

        if file_info.folder == DIRECTORY['archives']:
            archives.append(file_info.new_name + file_info.extension)

    folders = [images, video, documents, audio, archives]

    return folders


def print_folders(folders: list):
    """Displays the names of files"""

    images, video, documents, audio, archives = folders

    print(f"--> {DIRECTORY['images']}: {images} \n")
    print(f"--> {DIRECTORY['video']}: {video} \n")
    print(f"--> {DIRECTORY['documents']}: {documents} \n")
    print(f"--> {DIRECTORY['audio']}: {audio} \n")
    print(f"--> {DIRECTORY['archives']}: {archives} \n")


def print_extensions(extensions_data: list) -> None:
    """Print extensions"""
    unknown_extensions, known_extensions = extensions_data

    print(f"-> known_extensions: {known_extensions} \n")

    print(f"-> unknown_extensions: {unknown_extensions} \n")


def deletes_empty_folders(path_folder, root_directory) -> None:
    """
    Recursively delete empty folders in the specified path_folder directory.
    """
    try:
        for path_object in os.listdir(path_folder):
            object_full_path = os.path.join(path_folder, path_object)
            if os.path.isdir(object_full_path):

                if path_folder == root_directory:
                    if path_object.lower() not in DIRECTORY:
                        if os.listdir(object_full_path):
                            deletes_empty_folders(
                                object_full_path, root_directory)
                        else:
                            os.rmdir(object_full_path)
                else:
                    if os.listdir(object_full_path):
                        deletes_empty_folders(object_full_path, root_directory)
                    else:
                        os.rmdir(object_full_path)

            elif os.path.isfile(object_full_path):
                continue

    except PermissionError as error:
        print(error)


def read_file_with_data() -> Tuple[List[str], Dict[int, InfoFile]]:
    """
    Reads data from two files, 'un_extension.txt' and 'kn_extension.txt'
    """

    with open(FILE_UN_EXT, 'r', encoding='utf-8') as un_ext_file:
        un_ext = []
        for line in un_ext_file:
            file_info = line.split(',')
            un_ext.append(file_info[1])
        un_ext = list(set(un_ext))

    with open(FILE_KN_EXT, 'r', encoding='utf-8') as kn_ext_file:
        files_info = {}
        kn_ext = []
        for i, line in enumerate(kn_ext_file):
            data = line.split(',')

            file_info = InfoFile(
                data[0], data[1], data[2], data[3], data[4], data[5].strip('\n'))
            files_info[i] = file_info
            kn_ext.append(data[1])
        kn_ext = list(set(kn_ext))

    data_extension = [un_ext, kn_ext]

    return data_extension, files_info


def check_folders(root_path: str):
    """
    Checks for the existence of specific folders in a given root path, and creates 
    any missing folders.
    """

    folders = list(DIRECTORY)[:-1]

    for folder in folders:
        path_folder = os.path.join(root_path, folder)
        if not os.path.exists(path_folder):

            try:
                os.mkdir(path_folder)
            except PermissionError as error:
                print(error)


def main(path_folder: str):
    """Main controller"""

    check_folders(path_folder)

    scan_files_and_folders(path_folder, path_folder)

    max_depth = get_max_depth(path_folder)
    while max_depth > 0:
        deletes_empty_folders(path_folder, path_folder)
        max_depth -= 1

    data_extension, files_info = read_file_with_data()

    print_extensions(data_extension)
    folders = sort_files_for_print(files_info)
    print_folders(folders)


if __name__ == '__main__':

    with open(FILE_UN_EXT, "w") as f:
        pass

    with open(FILE_KN_EXT, "w") as f:
        pass

    FOLDER_PATH = parse_path()

    if is_folder(FOLDER_PATH):
        main(FOLDER_PATH)
    else:
        print("Something wrong, try again")

# python modul_06_WH/sort.py /home/alex/Desktop/garbage
