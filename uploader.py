import os
import re
from tkinter import filedialog
import cloudinary.uploader
from config import *


def save_last_used_path(current_path):
    with open('config.py') as f:
        config = f.readlines()
    config[-1] = "initial_dir = '{}'".format(current_path)
    with open('config.py', "w") as f:
        f.writelines(config)


def get_path():
    title = "Please select a markdown file"
    file_types = (("markdown files", "*.md"),
                  ("all files", "*.*"))
    file_paths = filedialog.askopenfilenames(initialdir=initial_dir,
                                           title=title,
                                           filetypes=file_types
                                           )
    current_dir = os.path.dirname(file_paths[0])
    save_last_used_path(current_dir)

    return file_paths


def upload_img(path):
    upload_massage = cloudinary.uploader.upload(path)
    original_filename = upload_massage["original_filename"]
    url = upload_massage["url"]
    return "![{}]({})".format(original_filename, url)


PATTERN = "!\[[^\]]*\]\(([^\)]+)\)"

# use TK to get file paths
file_paths = get_path()

for file_path in file_paths:
    file_name = os.path.basename(file_path)
    current_dir = os.path.dirname(file_path)
    os.chdir(current_dir)

    # read md file
    with open(file_name) as f:
        md = f.readlines()

    # loop lines, upload images and replace the url
    new_md = []
    for line in md:
        imgs_local_path_list = re.findall(PATTERN, line)
        if imgs_local_path_list:
            for path in imgs_local_path_list:
                new_expression = upload_img(path)
                new_line = re.sub(PATTERN, new_expression, line)
                new_md.append(new_line)
                print(imgs_local_path_list[0], "uploaded")
        else:
            new_md.append(line)

    # save to a new md file
    new_file_name = "uploaded_" + file_name
    with open(new_file_name, "w") as f:
        f.writelines(new_md)

