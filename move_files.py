import os
import shutil
path = r"path"
extensions = {'.jpg', '.jpeg', '.mp4', '.png', '.mp3'}
destiny = r"A:\test"


for root, dirs, files in os.walk(path):
    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destiny, file)
            shutil.move(source_file, destination_file)
            print(f"Moved: {source_file} -> {destination_file}")
