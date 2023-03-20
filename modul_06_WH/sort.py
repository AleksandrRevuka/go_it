"""Sort garbage"""
import os
import sys
from typing import NamedTuple
from string import digits, ascii_letters, punctuation
from prettytable import PrettyTable


class NameFolders(NamedTuple):
    """Type class for element"""
    images: str
    video: str
    documens: str
    audio: str
    archives: str
    unknown_extensions: str


def chack_path(test_path: str) -> bool:
    """Checking the path for correctness"""
    try:
        if os.path.isfile(test_path):
            return True
    except OSError as error:
        print(f"{error}, 'My error'")
    return False


def parse_path() -> str:
    """Get path from input data"""
    return " ".join(sys.argv[1])


def main():
    """Main controller"""
    print("main")


if __name__ == '__main__':
    IMAGES_EXTENSIONS = ['JPEG', 'PNG', 'JPG', 'SVG']
    VIDEO_EXTENSIONS = ['AVI', 'MP4', 'MOV', 'MKV']
    DOCUMENS_EXTENSIONS = ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX']
    AUDIO_EXTENSIONS = ['MP3', 'OGG', 'WAV', 'AMR']
    ARCHIVES_EXTENSIONS = ['ZIP', 'GZ', 'TAR']
    UNKNOWN_EXTENSIONS = []

    path_folder = parse_path
    if chack_path(path_folder):
        main()
    else:
        print("Something wrong, try again")
