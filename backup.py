import os
import time
from sys import platform

import config

date = time.strftime("%d-%m-%Y_%H-%M")


def os_check():
    if platform == "linux" or platform == "linux2":
        return True
    else:
        return False


def mysql_backup():
    print("")
    print("Starting backup for MySQL database...")
    print("")
    tmpCheck = os.system("cd "+config.cloud_mount)
    if tmpCheck == 0:
        createBackup = os.system("cd " + config.cloud_mount + " && "
                                 "mysqldump -u " + config.mysql_user + " -p'" + config.mysql_password + "' --all-databases > mysqlbackup-" + date + ".sql")

        if createBackup == 0:
            print("")
            print("MySQL database backup successfully created")
            print("")
        else:
            print("")
            print("MySQL database backup failed")
            print("")
            os.system("cd " + config.cloud_mount + " && rm mysqlbackup-" + date + ".sql")
    else:
        print("")
        print("Mount not exits")
        print("")


def backup():
    print("")
    print("Starting backup for "+str(len(config.backup_dirs))+" directories...")
    print("")
    if len(config.backup_dirs) == 0:
        print("")
        print("No directories to backup")
        print("")
    else:
        counter = 0
        for dir in config.backup_dirs:
            counter += 1
            print("")
            print("Starting backup for "+dir+"...")
            print("")
            status = os.system("cd " + config.cloud_mount + " && tar -czvf backup_" + str(counter) + "-" + date + ".tar.gz "+dir)
            if status == 0:
                print("")
                print("Backup for "+dir+" successfully")
                print("")
            else:
                print("")
                print("Failed to backup "+dir)
                print("")


def clearBackups():
    print("")
    print("Cleaning backup dir...")
    print("")
    for file in os.listdir(config.cloud_mount):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            os.rmdir(file)
        else:
            print(file + " can't be deleted!")
    print("")
    print("Successfully deleted old backup files")
    print("")

if os_check():
    if os.path.exists(config.cloud_mount):
        if config.clear_backups:
            clearBackups()
        if config.mysql_backup:
            mysql_backup()
        backup()
    else:
        print("Failed to create backup")
        print(config.cloud_mount + " not exists")
else:
    print("Sorry but this script is only for Linux")
