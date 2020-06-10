# Linux Backup Script

My Python script helps you to backup your Linux Server to a Cloud Mount using rclone.

## Installation

- Install Python with ``apt install python3 python3-pip``
- Edit the ``config.py`` with a text editor like Notepad++
- Setup cronjob with ``crontab -e``. 
  - This cronjob backup your Linux server every day at 3 AM `0 3 * * * python3 /path/to/script/Linux-Backup-Script/backup.py`