# Credentials to connect to the MySQL database and backup all databases to a .sql file.
mysql_user = "root"
mysql_password = "securePassword"

# Location where the backup files will be stored
backup_location = "/media/cloud"
# Locations to backup
backup_dirs = ["/var/www", "/etc"]

# Should the script do a MySQL Database backup?
mysql_backup = True
# Should the script delete old backups?
clear_backups = False

# Format for the date in the filename
date_format = "%Y_%m_%d-%H_%M"
# Backup filename
backup_name_format = "%date%-%backupName%"