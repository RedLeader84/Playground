import shutil
from tkinter import Entry
import sys
import time
import logging

with os.scandir(source_dir) as entries:
    print(entry.name)
    
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "Users/user/Downloads"
dest_dir_sfx = "/Users/user/Sound"
dest_dir_video = "/Users/user/Desktop/Downloaded Video"
dest_dir_image = "/Users/user/Desktop/Downloaded Images"
dest_dir_music = "/Users/user/Sound/Muswak"

def makeUnique(path):
    
def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)
    
class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                dest = source_dir
                if name.endswith('.wav') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        dest = dest_dir_sfx
                    else:
                        dest = dest_dir_music
                    move(dest, entry, name)
                elif name.endswith(".mov") or name.endswith('mp4'):
                    dest = dest_dir_video
                    move(dest, entry, name)
                elif name.endswith('.jpg') or name.endswith('jpeg') or name.endswith('.png'):
                    dest = dest_dir_image
                    move(dest, entry, name)
                    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = Downloads
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()