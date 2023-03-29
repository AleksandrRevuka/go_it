import pathlib


def walk(path):
    for entry in pathlib.Path(path).iterdir():
        if entry.is_file():
            yield path, [], [entry.name]
        elif entry.is_dir():
            yield entry.absolute(), [
                subdir.name for subdir in entry.iterdir() if subdir.is_dir()
            ], [file.name for file in entry.glob("*") if file.is_file()]
            yield from walk(entry)


# Пример использования
for root, dirs, files in walk("/path"):
    print(f"root: {root}")
    print(f"dirs: {dirs}")
    print(f"files: {files}")