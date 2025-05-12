from generate_page import *
from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType
import unittest
import os
import shutil

def copy_static(path):
    if len(os.listdir(path)) == 0:
        print("found end")
        return
    if not os.path.exists("public"):
        os.mkdir("public")

    if os.path.exists(path):
        files_and_folders = os.listdir(path)
        for file in files_and_folders:
            updated_path = f"{path}/{file}"
            if os.path.isdir(updated_path):
                copy_static(updated_path)
            else:
                new_path = ""
                if len(path.split("static/", 1)) > 1:
                    new_path = path.split("static/", 1)[1]

                if not os.path.exists("public/" + new_path):
                    os.mkdir("public/" + new_path)

                shutil.copy(src=updated_path,dst="public/" + new_path)
    return

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_static("static")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
