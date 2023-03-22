def scan_files_and_folders(path: str, root_directory: str = None) -> Dict[str, InfoFile]:
    """
    Scans the specified directory and all its subdirectories for files and folders, and returns a dictionary containing
    information about each file found.
    """
    files_info_data = {}
    scan_files(path, root_directory, files_info_data)
    return files_info_data


def scan_files(path: str, root_directory: str, files_info_data: Dict[str, InfoFile]) -> None:
    """
    Scans the specified directory and all its subdirectories for files, and adds information about each file to the
    specified dictionary.
    """
    objects = os.listdir(path)

    for object in objects:
        object_full = os.path.join(path, object)

        if os.path.isfile(object_full):
            add_file_to_data(object, path, files_info_data)
        else:
            if path == root_directory:
                if object.lower() not in ['images', 'video', 'documents', 'audio', 'archives']:
                    scan_files(object_full, root_directory, files_info_data)
            else:
                scan_files(object_full, root_directory, files_info_data)
                
                
def add_file_to_data(file_path: str, directory_path: str, files_info_data: Dict[str, InfoFile]) -> None:
    """
    Adds information about the specified file to the specified dictionary.
    If a file with the same name already exists in the dictionary, a copy number is appended to the file name to make it
    unique.
    """
    name_file, extension = os.path.splitext(os.path.basename(file_path))
    file_info = InfoFile(name_file, extension, os.path.dirname(file_path))

    if name_file in files_info_data:
        copy_number = 1
        while f"{name_file}_copy{copy_number}" in files_info_data:
            copy_number += 1
        name_file = f"{name_file}_copy{copy_number}"
    
    files_info_data[os.path.basename(file_path)] = file_info