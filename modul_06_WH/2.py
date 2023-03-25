import os

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


print(get_max_depth('/home/alex/Desktop/garbage'))


# напиши функцію которая будет возвращать найбільшу глубину вложених папок
# навпаки найбільшу глубину вложених папок



def deletes_empty_folders(path_folder, root_directory):
    """Delete empty folders"""
    for object in os.listdir(path_folder):
        object_full_path = os.path.join(path_folder, object)
        if os.path.isdir(object_full_path):
            if os.listdir(object_full_path):
                # Recursively delete empty subfolders
                deletes_empty_folders(object_full_path, root_directory)
            else:
                # Delete empty folder
                if path_folder != root_directory or object.lower() not in ['images', 'video', 'documents', 'audio', 'archives']:
                    try:
                        os.rmdir(object_full_path)
                    except OSError:
                        # If rmdir fails, use shutil.rmtree to delete non-empty folders
                        shutil.rmtree(object_full_path)

        elif os.path.isfile(object_full_path):
            continue