import os


def list_items(directory):
    items = os.listdir(directory)

    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print(f"{item} is a directory")
        else:
            print(f"{item} is a file")

list_items('../')