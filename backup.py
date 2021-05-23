import os
import time
from sys import platform

import config
from logger import Logger

date = time.strftime(config.date_format)
logger = Logger("backup.log")

# This function check if the script is running on a unix based operating system.
def os_check():
    if platform.startswith('linux') or platform == 'darwin':
        return True
    else:
        return False


def mysql_backup():
    logger.log("INFO", "Starting backup for MySQL database...")
    tmpCheck = os.system("cd "+config.backup_location)
    if tmpCheck == 0:
        mysqlBackupFileName = getFileName('mysqlBackup') + '.sql'
        createBackup = os.system("cd " + config.backup_location + " && "
                                 "mysqldump -u " + config.mysql_user + " -p'" + config.mysql_password + "' --all-databases > " + mysqlBackupFileName)

        if createBackup == 0:
            logger.log("SUCCESS", "MySQL database backup successfully created")
        else:
            logger.log("ERROR", "MySQL database backup failed")
            os.system("cd " + config.backup_location + " && rm mysqlbackup-" + date + ".sql")
    else:
        logger.log("ERROR", "Mount not exits")


def backup():
    logger.log("INFO", "Starting backup for "+str(len(config.backup_dirs))+" directories...")
    if len(config.backup_dirs) == 0:
        logger.log("INFO", "No directories to backup")
    else:
        counter = 0
        for dir in config.backup_dirs:
            backupFileName = getFileName('backup_' + str(counter + 1)) + '.tar.gz'
            counter += 1
            logger.log("INFO", "Starting backup for "+dir+"...")
            status = os.system("cd " + config.backup_location + " && tar -czvf " + backupFileName + " " + dir)
            if status == 0:
                logger.log("SUCCESS", "Backup for "+dir+" successfully")
            else:
                logger.log("ERROR", "Failed to backup "+dir)


def clearBackups():
    logger.log("INFO", "Cleaning backup dir...")
    for file in os.listdir(config.backup_location):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            os.rmdir(file)
        else:
            logger.log("ERROR", file + " can't be deleted!")
    logger.log("SUCCESS", "Successfully deleted old backup files")

def getFileName(name):
    fileName = config.backup_name_format

    fileName = fileName.replace('%date%', date)
    fileName = fileName.replace('%backupName%', name)

    print(fileName)

    return fileName

if os_check():
    if os.path.exists(config.backup_location):
        if config.clear_backups:
            clearBackups()
        if config.mysql_backup:
            mysql_backup()
        backup()
    else:
        logger.log("ERROR", "Failed to create backup")
        logger.log("ERROR", config.backup_location + " not exists")
    logger.closeFile()
else:
    logger.log("ERROR", "Sorry but this script is only for Linux or macOS")
    logger.closeFile()
