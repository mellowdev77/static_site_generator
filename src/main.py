from generate_page import *
import os
import shutil
import sys

def main():
    basepath = "/"

    if len(sys.argv) > 1 and sys.argv[1] != None:
        basepath = sys.argv[1]

    gen_folder = "docs"
    if os.path.exists(gen_folder):
        shutil.rmtree(gen_folder)
    copy_static("static", gen_folder)
    generate_pages_recursive(basepath, "content", "template.html", gen_folder)

if __name__ == "__main__":
    main()
