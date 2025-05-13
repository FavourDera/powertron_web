@echo off
setlocal enabledelayedexpansion

:: Create backup directory if it doesn't exist
if not exist "backups" mkdir backups

:: Generate timestamp
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set timestamp=%datetime:~0,8%_%datetime:~8,6%

:: Create backup filename
set backup_filename=powertron_backup_%timestamp%.zip
set backup_path=backups\%backup_filename%

:: Create zip file
powershell Compress-Archive -Path * -DestinationPath "%backup_path%" -Force

:: Git backup
git add .
git commit -m "Automated backup: %timestamp%"
git push

echo Backup completed successfully: %backup_filename%
pause 