import logging
import os
import errno
import shutil
from markdown_blocks import markdown_to_html_node

logging.basicConfig(level=logging.INFO)

def generate_public(src_dir, dest_dir):
    # Delete all the contents of the destination directory `public` to ensure that the copy is clean
    if os.path.exists(dest_dir):
        print("Public folder exists. Removing public folder tree.")
        shutil.rmtree(dest_dir)

    # Copy all files and subdirectories, nested files, etc. from a source directory to a destination directory
    # in our case, `static` to `public`
#    shutil.copytree("./static/", "./public/")
    recursive_copy(src_dir, dest_dir)

def recursive_copy(source_dir: str, destination_dir: str):
    if not os.path.exists(destination_dir):
        logging.log(logging.INFO, f"Creating directory '{destination_dir}'")
        os.mkdir(destination_dir)
    source_full_path = os.path.abspath(source_dir)
    destination_full_path = os.path.abspath(destination_dir)
    logging.log(logging.INFO, f"Copying source path: {source_full_path} to destination path: {destination_full_path}")
    entries = os.listdir(source_full_path)
    for entry in entries:
        source_filename = os.path.abspath(os.path.join(source_full_path, entry))
        destination_filename = os.path.abspath(os.path.join(destination_full_path, entry))
        logging.log(logging.INFO, f"* Entry is: '{source_filename}'")
        if os.path.isfile(source_filename):
            logging.log(logging.INFO, f"* Determined that '{source_filename}' is a file.")
            shutil.copy(source_filename, destination_filename)
            logging.log(logging.INFO, f"* Copying {source_filename} to {destination_filename}")
        elif os.path.isdir(os.path.join(source_full_path, entry)):
            logging.log(logging.INFO, f"* Determined that '{source_filename}' is a directory. Creating it at {destination_filename}.")
            os.mkdir(destination_filename)
            logging.log(logging.INFO, f"* Recursively calling recursive_copy(source_dir={source_filename}, destination_dir={destination_filename})")
            recursive_copy(source_filename, destination_filename)
    logging.log(logging.INFO, f"No more files in this directory.  Exiting.")

def extract_title(markdown: str):
    lines = markdown.split("\n\n")
    for line in lines:
        if line.startswith("#"):
            return line[1:].strip()
    raise Exception("No title found in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating a page from {from_path} to {dest_path} using {template_path}.")
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    node = markdown_to_html_node(markdown)
    html_string = node.to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
    try:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(dest_path):
            pass
        else: raise
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

if __name__ == "__main__":
    generate_public("./static/", "./public/")