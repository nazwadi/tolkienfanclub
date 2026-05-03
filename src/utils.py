import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)

def generate_public():
    # Delete all the contents of the destination directory `public` to ensure that the copy is clean
    if os.path.exists("./public/"):
        print("Public folder exists. Removing public folder tree.")
        shutil.rmtree("./public/")

    # Copy all files and subdirectories, nested files, etc. from a source directory to a destination directory
    # in our case, `static` to `public`
#    shutil.copytree("./static/", "./public/")
    recursive_copy("./static/", "./public/")

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

if __name__ == "__main__":
    generate_public()