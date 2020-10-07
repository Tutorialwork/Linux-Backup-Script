import os
import time
from sys import platform

import config
from logger import Logger

date = time.strftime("%d-%m-%Y_%H-%M")
logger = Logger("backup.log")

def os_check():
    if platform == "linux" or platform == "linux2":
        return True
    else:
        return False


def mysql_backup():
    logger.log("INFO", "Starting backup for MySQL database...")
    tmpCheck = os.system("cd "+config.cloud_mount)
    if tmpCheck == 0:
        createBackup = os.system("cd " + config.cloud_mount + " && "
                                 "mysqldump -u " + config.mysql_user + " -p'" + config.mysql_password + "' --all-databases > mysqlbackup-" + date + ".sql")

        if createBackup == 0:
            logger.log("SUCCESS", "MySQL database backup successfully created")
        else:
            logger.log("ERROR", "MySQL database backup failed")
            os.system("cd " + config.cloud_mount + " && rm mysqlbackup-" + date + ".sql")
    else:
        logger.log("ERROR", "Mount not exits")


def backup():
    logger.log("INFO", "Starting backup for "+str(len(config.backup_dirs))+" directories...")
    if len(config.backup_dirs) == 0:
        logger.log("INFO", "No directories to backup")
    else:
        counter = 0
        for dir in config.backup_dirs:
            counter += 1
            logger.log("INFO", "Starting backup for "+dir+"...")
            status = os.system("cd " + config.cloud_mount + " && tar -czvf backup_" + str(counter) + "-" + date + ".tar.gz "+dir)
            if status == 0:
                logger.log("SUCCESS", "Backup for "+dir+" successfully")
            else:
                logger.log("ERROR", "Failed to backup "+dir)


def clearBackups():
    logger.log("INFO", "Cleaning backup dir...")
    for file in os.listdir(config.cloud_mount):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            os.rmdir(file)
        else:
            logger.log("ERROR", file + " can't be deleted!")
    logger.log("SUCCESS", "Successfully deleted old backup files")

if os_check():
    if os.path.exists(config.cloud_mount):
        if config.clear_backups:
            clearBackups()
        if config.mysql_backup:
            mysql_backup()
        backup()
    else:
        logger.log("ERROR", "Failed to create backup")
        logger.log("ERROR", config.cloud_mount + " not exists")
    logger.closeFile()
else:
    logger.log("ERROR", "Sorry but this script is only for Linux")
    logger.closeFile()
