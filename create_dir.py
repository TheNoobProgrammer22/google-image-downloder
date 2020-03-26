from os import chdir
from os import makedirs
from os import removedirs
from os import rename
from os.path import exists
from os.path import pardir
from shutil import copytree
from shutil import move

# Creates A Directory

def create_directory(name):
    if exists(pardir + "\\" + name):
        print("Folder already exists... Cannot Overwrite This")
    else:
        makedirs(pardir + "\\" + name)


# Deletes A Directory

def delete_directory(name):
    removedirs(name)

# Rename A Directory


def rename_directory(direct, name):
    rename(direct, name)

# Sets The Working Directory

def set_working_directory():
    chdir(pardir)

# Backup The Folder Tree
 
def backup_files(name_dir, folder):
    copytree(pardir, name_dir + ':\\' + folder)

# Move Folder To Specific Location 
# Overwrites The File If It Already Exists

def move_folder(filename, name_dir, folder):
    if not exists(name_dir + ":\\" + folder):
        makedirs(name_dir + ':\\' + folder)
    move(filename, name_dir + ":\\" + folder + ':\\')

