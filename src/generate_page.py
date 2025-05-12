from utils import *
import os
import shutil

def extract_title(markdown):
    header = markdown.split("#")
    if len(header) > 1:
        return str(str(markdown.strip("#")).strip()).split("\n")[0]

    raise Exception()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    with open(from_path, 'r') as f:
        markdown = f.read()
    with open(template_path, 'r') as f:
        template = f.read()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Content }}", html)
    template = template.replace("{{ Title }}", title)
    file_name = str(from_path.split("/")[-1])
    new_path = dest_path + "/" + file_name.replace(".md", ".html")
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    to_file = open(new_path, "w")
    to_file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dir_path_content):
        return
    if not os.path.isdir(dir_path_content):
        return

    if os.path.exists(dir_path_content):
        files_and_folders = os.listdir(dir_path_content)
        for file in files_and_folders:
            updated_path = dir_path_content + "/" + file
            updated_dest = dest_dir_path + "/" + file
            if os.path.isdir(updated_path):
                print(f"recursive dir: {updated_path}, dest: {updated_dest}")
                generate_pages_recursive(updated_path, template_path, updated_dest)
            else:
                print(f"non recursive dir: {updated_path}, dest: {dest_dir_path}")
                generate_page(updated_path, template_path, dest_dir_path)

    return
