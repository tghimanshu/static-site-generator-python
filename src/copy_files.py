import shutil
import os


def copy_files_recursively(source_dir, target_dir):
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)

        if os.path.isdir(source_item):
            if not os.path.exists(target_item):
                os.makedirs(target_item)
            copy_files_recursively(source_item, target_item)
        else:
            print("Copying file:", source_item, " -> ", target_item, sep=" ")
            shutil.copy2(source_item, target_item)
            print("Done")


def copy_files(source_dir="static", target_dir="public"):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    else:
        shutil.rmtree(target_dir)
        os.makedirs(target_dir)

    copy_files_recursively(source_dir, target_dir)
