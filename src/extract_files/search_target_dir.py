from pathlib import Path

# 在drive_paths中搜索，返回第一个存在的路径（文件夹）
def search(drive_paths: list[Path]) -> Path:
    for drive_path in drive_paths:
        if(drive_path.exists() and drive_path.is_dir()):
            return drive_path