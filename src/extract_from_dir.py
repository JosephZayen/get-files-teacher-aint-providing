import logging
from pathlib import Path
import shutil
from datetime import datetime
from configs import file_suffixes, DEST_DIR

logger = logging.getLogger(__name__)
targets: list[Path] = []



def extractor(p: Path) -> None:
    if(not p.is_dir()):
        raise TypeError("p is not a directory")

    #把所有目标文件倒到目标列表里面
    for suffix in file_suffixes:
        for target_file in p.rglob(f"**/*.{suffix}"):
            if(target_file.is_file()):
                targets.append(target_file)

    #这里面是目标文件，rlogb递归搜索出来的
    for target in targets:
        if(target.exists() and target.is_file()):
            dst: Path = DEST_DIR + target.name
            if(not dst.exists()):
                shutil.copy2(target, dst)
                log_time = str(datetime.now())
                logger.info(f"复制了一个文件， {log_time}")