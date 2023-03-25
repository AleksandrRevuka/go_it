import os
import shutil


def main(path):

    os.rename('/home/alex/Desktop/garbage (copy)', '/home/alex/Desktop/garbage')
    shutil.move('/home/alex/Desktop/garbage', '/home/alex/Desktop/garbage (copy)')


if __name__ == '__main__':
    main('/home/alex/Desktop')
