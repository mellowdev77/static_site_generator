from generate_page import *
import os
import shutil
import sys

def main():
    basepath = sys.argv[1]
    if basepath == None:
        basepath = "/"

    gen_folder = "docs"
    if os.path.exists(gen_folder):
        shutil.rmtree(gen_folder)
    copy_static("static", gen_folder)
    generate_pages_recursive(basepath, "content", "template.html", gen_folder)

if __name__ == "__main__":
    main()
