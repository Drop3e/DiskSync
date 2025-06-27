import sync
import time
import psutil
import folder as fol

def find_procs_by_name():
    for p in psutil.process_iter(['name']):
        if p.info['name'] == 'Obsidian.exe':
            return True
    return False

while True:
    time.sleep(20)
    if find_procs_by_name() == False:
        try:
            sync.sync_folder(fol.source_folder, fol.target_folder)
        finally:    
            break
    else:
        continue
