import logging
from pathlib import Path
import time
import datetime
from .extract_from_dir import extractor
from .configs import TARGET_NAMES, drive_prefixes
import sys



def __cli():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename="ch_geo_extractor.log", level = logging.INFO, encoding="utf-8")

    # 初始化驱动盘符名称与路径
    drive_letters: list[str] = [prefix + TARGET_NAME for prefix in drive_prefixes for TARGET_NAME in TARGET_NAMES]
    # 转化成路径对象
    drive_paths: Path = [Path(drive_letter) for drive_letter in drive_letters]

    # 初始化搜索结果存储变量
    target_path = None

    # 在drive_paths中搜索，返回第一个存在的路径（文件夹）
    def search(drive_paths: list[Path]) -> Path:
        for drive_path in drive_paths:
            if(drive_path.exists() and drive_path.is_dir()):
                return drive_path

    # 轮询，搜索出存在文件夹后提取所有特定后缀文件
    while(target_path is None):
        log_date = datetime.datetime.now()
        log_time = str(log_date)
        target_path = search(drive_paths)
        if(target_path is not None):
            extractor(target_path)
            logger.info(f"成功完成搜索，LOG_TIME: {log_time}")
            sys.exit(0)
        time.sleep(60)


if __name__ == "__main__":
    __cli()