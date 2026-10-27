from pathlib import Path
import shutil

DRY_RUN = False   # first run: True. When the preview looks right: False

folder = Path.home() / "Downloads"

CATEGORIES = {
    ".jpg": "Images", ".jpeg": "Images", ".png": "Images",
    ".svg": "Images", ".gif": "Images", ".webp": "Images",
    ".pdf": "Docs", ".docx": "Docs", ".doc": "Docs",
    ".txt": "Docs", ".pptx": "Docs",
    ".xlsx": "Data", ".csv": "Data", ".pbix": "Data",
    ".mp4": "Videos", ".mov": "Videos",
    ".zip": "Archives",
    ".exe": "Installers",
}

SKIP_NAMES = {"desktop.ini"}
SKIP_EXTENSIONS = {".crdownload", ".part", ".tmp"}

for file in folder.iterdir():
    if not file.is_file():
        continue
    if file.name.startswith("~$") or file.name.lower() in SKIP_NAMES:
        continue

    ext = file.suffix.lower()
    if ext in SKIP_EXTENSIONS:
        continue

    category = CATEGORIES.get(ext, "Others")
    dest_folder = folder / category
    dest = dest_folder / file.name

    counter = 1
    while dest.exists():
        dest = dest_folder / f"{file.stem} ({counter}){file.suffix}"
        counter += 1

    if DRY_RUN:
        print(f"[PREVIEW] {file.name} -> {category}/")
    else:
        dest_folder.mkdir(exist_ok=True)
        shutil.move(str(file), str(dest))
        print(f"Moved {file.name} -> {category}/")