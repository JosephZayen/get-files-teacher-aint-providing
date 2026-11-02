import logging
from pathlib import Path
import shutil
from datetime import datetime
from .configs import file_suffixes, DEST_DIR, NOT_IN_FILTER, IN_FILTER, COPY_LIMIT




def extractor(p: Path) -> None:
    logger = logging.getLogger(__name__)
    # 存储目标路径的列表
    targets: list[Path] = []

    if(not p.is_dir()):
        raise TypeError("p is not a directory")

    #把所有目标文件用rglob倒到目标列表里面
    for suffix in file_suffixes:
        for target_file in p.rglob(f"**/*.{suffix}"):
            if(target_file.is_file()):
                targets.append(target_file)

    #过滤目标文件
    filtered_targets: list[Path] = []
    for target in targets:
        str_target = str(target)
        # 必须同时通过两个过滤器
        # 如果说不存在过滤器，视为通过该过滤器
        if(
            ((IN_FILTER is None) or IN_FILTER in str_target)
            and
            ((NOT_IN_FILTER is None) or NOT_IN_FILTER not in str_target)
        ):
            filtered_targets.append(target)

    results: list[Path] = []
    if(COPY_LIMIT is not None):
        results = filtered_targets[ : COPY_LIMIT]

    #执行复制
    #这里面是目标文件，rlogb递归搜索出来的
    for target in results:
        if(target.exists() and target.is_file()):
            dst: Path = DEST_DIR / target.name
            if(not dst.exists()):
                shutil.copy2(target, dst)
                log_time = str(datetime.now())
                logger.info(f"已复制一个文件，LOG_TIME: {log_time}")