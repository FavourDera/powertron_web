import os
import shutil
from datetime import datetime
import zipfile

def create_backup():
    # Create backup directory if it doesn't exist
    backup_dir = "backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Generate timestamp for backup filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"powertron_backup_{timestamp}.zip"
    backup_path = os.path.join(backup_dir, backup_filename)

    # Create zip file
    with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the project directory
        for root, dirs, files in os.walk('.'):
            # Skip the backups directory and git directory
            if 'backups' in dirs:
                dirs.remove('backups')
            if '.git' in dirs:
                dirs.remove('.git')
            
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, '.')
                zipf.write(file_path, arcname)

    print(f"Backup created successfully: {backup_filename}")

if __name__ == "__main__":
    create_backup() 