import logging
from pathlib import Path
import time
import datetime
from extract_from_dir import extractor
from configs import TARGET_NAME
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(filename="ch_geo_extractor.log", level = logging.INFO)

# 初始化驱动盘符名称与路径
drive_letters = [rf"C:/{TARGET_NAME}", rf"F:/中国地理{TARGET_NAME}", rf"E:/{TARGET_NAME}", rf"D:/{TARGET_NAME}"]
#搜索类似于F:/中国地理的文件
drive_paths = [Path(drive_letter) for drive_letter in drive_letters]

# 初始化搜索结果存储变量
target_path = None


def search():
    for drive_path in drive_paths:
        if(drive_path.exists() and drive_path.is_dir()):
            return drive_path

while(target_path is None):
    target_path = search()
    if(target_path is not None):
        extractor(target_path)
        logger.info(f"完成了， {log_time}")
        sys.exit(0)
    log_date = datetime.datetime.now()
    log_time = str(log_date)
    logger.info(f"搜索完成一轮，{log_time}")
    time.sleep(60)