import os
import argparse
import sys

def ls(directory='.', show_hidden=False, human_readable=False):
    file_list = os.listdir(directory)
    file_list.sort()

    if not show_hidden:
        file_list = [f for f in file_list if not f.startswith('.')]

    if human_readable:
        file_list = [(f, get_human_readable_size(os.path.join(directory, f))) for f in file_list]
        for file, size in file_list:
            print(f"{file}\t{size}")
    else:
        for file in file_list:
            print(file)

def get_human_readable_size(file_path):
    size = os.path.getsize(file_path)
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(units) - 1:
        size /= 1024
        index += 1
    return f"{size:.2f} {units[index]}"

def main():
    parser = argparse.ArgumentParser(description='List files in a directory.')
    parser.add_argument('-a', '--all', action='store_true', help='Include hidden files')
    parser.add_argument('-w', '--human-readable', action='store_true', help='Display file sizes in human-readable format')
    args = parser.parse_args()

    ls(directory='.', show_hidden=args.all, human_readable=args.human_readable)

if __name__ == '__main__':
    main()