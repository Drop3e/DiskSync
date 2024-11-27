import os
import shutil

def sync_folder(source_folder, target_folder):
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder) #Create a relative path to the folder, in order to then use it to create an absolute path to any media, such as a flash drive
        target_path = os.path.join(target_folder, relative_path) #create an absolute path to the flash drive

        if not os.path.exists(target_path):# checking the folder on the flash drive, if any of the folders are missing, creates
            os.makedirs(target_path)

        for file in files:
            source_file = os.path.join(root, file)# Create a path to a file on your hard drive
            target_file = os.path.join(target_path, file)# create the path to the file on the flash drive
            if os.path.exists(target_file): # if the file exists, check for changes
                if os.path.getmtime(source_file) > os.path.getmtime(target_file):# Check the file, if the time of the main file is later, delete the file
                    os.remove(target_file)
            shutil.copy2(source_file, target_file) # And in any case we make a copy
                    
# ***
# This cycle will check the files of the second specified media, be it a flash drive or a second disk partition.
# If the second media in the specified directory contains files or folders that do not exist in the main directory, they will be deleted
# ***
    for root, dirs, files in os.walk(target_folder):
        relative_path = os.path.relpath(root, target_folder) # All relative paths from the second media
        target_path = os.path.join(source_folder, relative_path) # Using a relative path, we create an absolute path to the main disk
        if not os.path.exists(target_path): # check if this path exists
            shutil.rmtree(os.path.join(target_folder, relative_path)) # delete files from the flash drive if the specified path is not there

        for file in files: # create a loop that will iterate through files
            flash_file = os.path.join(root, file) 
            hard_file = os.path.join(target_path, file)
            if not os.path.exists(hard_file): # if the file is not on the hard drive, delete it from another medium, in our case from a flash drive
                os.remove(flash_file)

