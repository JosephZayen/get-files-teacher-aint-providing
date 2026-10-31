# 项目名称
文件提取器

# 项目用途
在老师开机的时候把文件提取出来。如果老师不给PPT,PDF,DOCX等。

# 使用方法
WINDOWS设置程序计划管理器\
然后指向extract.py\
然后定时启动，不要多开实例，然后就会轮询了，完成之后就会关闭

配置在src/configs.py里面改\
TARGET_NAMES是目标目录\
file_suffixes是要从里面提取的文件后缀\
drive_prefixes是搜索的盘符\
DEST_DIR是保存的地方

# TODO
我还没测试过windows的文件共享机制，所以我不确定会不会出现文件锁的问题\
此外，我还需要加个复制文件数量的上限的配置，不然复制太多的话我也担心会出问题。