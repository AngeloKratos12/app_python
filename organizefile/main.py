import os
import glob
import shutil

extensions = {
    "jpg": "images",
    "png": "images",
    "PNG": "images",
    "ico": "images",
    "gif": "images",
    "webp":"images",
    "svg": "images",
    "jpeg": "image",
    "sql": "sql",
    "exe": "programs",
    "msi": "programs",
    "deb":"programs",
    "pdf": "pdf",
    "xlsx": "excel",
    "csv": "excel",
    "rar": "archive",
    "zip": "archive",
    "gz": "archive",
    "tar": "archive",
    "docx": "word",
    "odt": "documents",
    "torrent": "torrent",
    "txt": "text",
    "ipynb": "python",
    "py": "python",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "video",
    "3gp" : "video",
    "avi": "video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
    "sqlite3": "sqlite3",
    "iso": "iso"
}

path = '/home/n_kratos/Téléchargements'

verbose = 0
for extension, folder_name in extensions.items():
        # get all the files matching the extension
    files = glob.glob(os.path.join(path, f"*.{extension}"))
    print(f"[*] Found {len(files)} files with {extension} extension")
    if not os.path.isdir(os.path.join(path, folder_name)) and files:
            # create the folder if it does not exist before
        print(f"[+] Making {folder_name} folder")
        os.mkdir(os.path.join(path, folder_name))
    for file in files:
            # for each file in that extension, move it to the correponding folder
        basename = os.path.basename(file)
        dst = os.path.join(path, folder_name, basename)
        if verbose:
            print(f"[*] Moving {file} to {dst}")
        shutil.move(file, dst)