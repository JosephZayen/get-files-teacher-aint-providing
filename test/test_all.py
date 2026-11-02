# 从项目根目录启动, python script.py方式运行，让脚本目录添加到那里

#import sys
#print(sys.path)

import sys
sys.path.insert(0, r"C:\Users\7\Desktop\VSCProjects\extract_files_teacher_doesnot_provide\src")

from extract_files.extract import __cli
from extract_files.configs import TARGET_NAMES, DEST_DIR
from pathlib import Path

#根据第一个目标目录创建D盘顶部测试目录
TEST_DIR = Path(f"D:/{TARGET_NAMES[0]}")
TEST_DIR.mkdir(parents=True, exist_ok=True)

"""
#清空测试目录
for ofile in TEST_DIR.iterdir():
    if(ofile.is_file()):
        ofile.unlink()
"""
# 清空目标目录
for ofile in DEST_DIR.iterdir():
    if(ofile.is_file()):
        ofile.unlink()

# 创建测试文件
# 硬编码使用PPTX/ ppt测试（默认包含在文件复制目标格式中）
TEST_FILE_PATHS = [TEST_DIR / (str(i) + ".pptx") for i in range(10)]
TEST_FILE_PATHS = TEST_FILE_PATHS + [TEST_DIR / (str(i) + ".ppt") for i in range(10)]

for TEST_FILE_PATH in TEST_FILE_PATHS:
    TEST_FILE_PATH.touch(exist_ok=True)

# PATH __hash__是字符串哈希
original = set()
for path_object in DEST_DIR.glob("*.pptx"):
    original.add(path_object)

__cli()

#找到新增的，目标目录新加了就认为通过测试（不在original内）
found = []
for path_object in DEST_DIR.glob("*.pptx"):
    if path_object not in original:
        found.append(path_object)

assert len(found) > 0

print("test passed")
print("file saved in destination folder, as seen in src/configs.py")

