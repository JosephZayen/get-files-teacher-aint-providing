from pathlib import Path

                                                                    

# 搜索路径                                                  # 去掉盘符的完整目标路径后缀
TARGET_NAMES = ["中国地理/中国地理"]                        # 会拼接盘符进行路径猜测，匹配后复制文件，只复制单个文件夹

# 搜索后缀
file_suffixes: str = ["pptx", "ppt", "pdf", "doc", "docx"]

# 搜索盘符
drive_prefixes: list[str] = [r"C:/", r"F:/", r"E:/", r"D:/"]

DEST_DIR = Path(r"D:/backup_files")
DEST_DIR.mkdir(parents=True, exist_ok=True)