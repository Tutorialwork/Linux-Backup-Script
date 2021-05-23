# Linux Backup Script

My Python script helps you to backup your Linux Server.
You can use it without any programming knowledge just by editing the config.py file.
The script backups directories and the entire MySQL Database and save it to a folder that you can set in the config.py file.

## Installation

- Install Python with ``apt install python3 python3-pip``
- Edit the ``config.py`` with a text editor like Notepad++
- Setup cronjob with ``crontab -e``. 
  - This cronjob backup your Linux server every day at 3 AM `0 3 * * * python3 /path/to/script/Linux-Backup-Script/backup.py`

## Automatic cloud upload

I recommend using this script with rclone.
Rclone is used to mount a Cloud Storage like Google Drive, OneDrive etc.
You can set this path as backup target and rclone will upload it automatically to the cloud.

### YouTube Tutorial (German)

[![YouTube Tutorial](https://img.youtube.com/vi/Zotvv52k7lE/0.jpg)](https://www.youtube.com/watch?v=Zotvv52k7lE)