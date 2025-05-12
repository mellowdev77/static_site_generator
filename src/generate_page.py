from utils import *
import os
import shutil

def extract_title(markdown):
    header = markdown.split("#")
    if len(header) > 1:
        return str(str(markdown.strip("#")).strip()).split("\n")[0]

    raise Exception()

def generate_page(basepath, from_path, template_path, dest_path):
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
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')
    template = template.replace("href='/", f"href='{basepath}")
    template = template.replace("src='/", f"src='{basepath}")
    file_name = str(from_path.split("/")[-1])
    new_path = dest_path + "/" + file_name.replace(".md", ".html")
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    to_file = open(new_path, "w")
    to_file.write(template)

def generate_pages_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content):
        files_and_folders = os.listdir(dir_path_content)
        for file in files_and_folders:
            updated_path = dir_path_content + "/" + file
            updated_dest = dest_dir_path + "/" + file
            if os.path.isdir(updated_path):
                print(f"recursive dir: {updated_path}, dest: {updated_dest}")
                generate_pages_recursive(basepath, updated_path, template_path, updated_dest)
            else:
                print(f"non recursive dir: {updated_path}, dest: {dest_dir_path}")
                generate_page(basepath, updated_path, template_path, dest_dir_path)

    return

def copy_static(path, gen_folder):
    if len(os.listdir(path)) == 0:
        print("found end")
        return
    if not os.path.exists(gen_folder):
        os.mkdir(gen_folder)

    if os.path.exists(path):
        files_and_folders = os.listdir(path)
        for file in files_and_folders:
            updated_path = f"{path}/{file}"
            if os.path.isdir(updated_path):
                copy_static(updated_path, gen_folder)
            else:
                new_path = ""
                if len(path.split("static/", 1)) > 1:
                    new_path = path.split("static/", 1)[1]

                if not os.path.exists(gen_folder + "/" + new_path):
                    os.mkdir(gen_folder + "/" + new_path)

                shutil.copy(src=updated_path,dst=gen_folder + "/" + new_path)
    return
