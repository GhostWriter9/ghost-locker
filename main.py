import os
import getpass

def lock_folder():
    if os.path.exists("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"):
        unlock_folder()
    elif not os.path.exists("Locker"):
        create_locker()
    else:
        confirm = input("Are you sure you want to lock the folder? (Y/N): ")
        if confirm.lower() == 'y':
            lock()

def lock():
    os.rename("Locker", "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}")
    os.system("attrib +h +s \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\"")
    print("Folder locked")

def unlock_folder():
    password = getpass.getpass("Enter password to unlock folder: ")
    if password == "123qwerty":
        os.system("attrib -h -s \"Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}\"")
        os.rename("Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}", "Locker")
        print("Folder unlocked successfully")
    else:
        print("Invalid password")

def create_locker():
    os.mkdir("Locker")
    print("Locker created successfully")

if __name__ == "__main__":
    lock_folder()
