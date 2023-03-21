"""Sort garbage"""
import os
import sys
import shutil
from typing import NamedTuple
from string import punctuation
from prettytable import PrettyTable


class NameFolders(NamedTuple):
    """Type class for element"""
    images: str
    video: str
    documens: str
    audio: str
    archives: str
    unknown_extensions: str


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

    cyrillic_symbols = CYRILLIC_SYMBOLS + CYRILLIC_SYMBOLS.upper()
    cyrillic_symbols_all = [ord(symbol) for symbol in cyrillic_symbols]
    translation = TRANSLATION + [symbol.upper() for symbol in TRANSLATION]
    trans = dict(zip(cyrillic_symbols_all, translation))

    return name.translate(trans)


def main(folder):
    """Main controller"""
    print(folder)
    print(normalize('txt/$_пантелеймон.txt'))


if __name__ == '__main__':

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = (
        "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l",
        "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh",
        "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
    )

    IMAGES_EXTENSIONS = ['JPEG', 'PNG', 'JPG', 'SVG']
    VIDEO_EXTENSIONS = ['AVI', 'MP4', 'MOV', 'MKV']
    DOCUMENS_EXTENSIONS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
    AUDIO_EXTENSIONS = ['MP3', 'OGG', 'WAV', 'AMR']
    ARCHIVES_EXTENSIONS = ['ZIP', 'GZ', 'TAR']
    UNKNOWN_EXTENSIONS = []

    folder_path = parse_path()
    if is_folder(folder_path):
        main(folder_path)
    else:
        print("Something wrong, try again")

# python modul_06_WH/sort.py /home/alex/Desktop/garbage
