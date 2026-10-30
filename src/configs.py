from pathlib import Path

TARGET_NAMES = ["中国地理/中国地理"]

file_suffixes: str = ["pptx", "ppt", "pdf", "doc", "docx"]

DEST_DIR = Path(r"D:/backup_files")
DEST_DIR.mkdir(parents=True, exist_ok=True)