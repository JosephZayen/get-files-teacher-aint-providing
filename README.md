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
DEST_DIR是保存的地方\
两个FILTER在整个路径进行搜索\
NOT_IN_FILTER进行过滤，防止某些不需要的文件\
IN_FILTER是强制把某些内容加入\
COPY_LIMIT是复制数量的上限，防止复制太多卡了\

# TEST
本地电脑测试了文件共享机制，防止出现文件锁问题,WPS打开的情况下依然能复制，不会锁住\

U盘进行了测试，多个小文件，一个10MB的PPT正常复制（搜索PPT与PPTX，使用任务调度器，WPS打开依然能正常复制）

# TEST TODO
还未测试DOCX， PDF等，但是想必是一样的
还未测试大批量的U盘复制

