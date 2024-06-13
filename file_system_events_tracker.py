import os
import shutil
import random 
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/marcu/OneDrive/Desktop/Projects/pro103/New folder'

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f'Hello',{event.src_path}, 'has been create')
    def on_deleted(self,event):
        print("Somebody deleted,",{event.src_path},'has been deleted')
    def on_modified(self,event):
        print("Somebody modified,",{event.src_path}, 'has been modified')
    def on_moved(self,event):
        print("Somebody moved,", {event.src_path}, 'has been moved')




event_handler=FileMovementHandler()
observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()



try:
    while True:
        time.sleep(2)
        print("running")
except  KeyboardInterrupt:
    
    print("Stopped")
    observer.stop()
        
            
