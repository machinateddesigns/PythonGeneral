import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/ryjak/OneDrive/Pictures/Memes"

destination_dir = "E:/Photo/Memes/"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Copied to the destination directory")
    except FileExistsError:
        print(f"File already exists in : {dest}")

schedule.every().day.at("04:00").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(3600)