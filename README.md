# 将 Android 开发多语言表格生成 string.xml 的脚本
## 多语言 xls 生成  Android xml
## 1.使用前准备
安装 Python 3（最新版本是3.63）
安装 两个 Python Package ----pyexcelerator 和 xlrd （命令行：pip install XXX）
## 2.使用
cd 到 start.py 所在文件夹，并将多语言 xls 表格复制到同一文件夹下。
简单处理多语言表格，插入一列至表格的首列，并对对应的 string 命名 id。（相当于提前给字符指定 Android 中的 R.id....）
在本文件夹下运行 python start.py -f  xxx.xls -t XXX  （xxx.xls 为多语言表格名称加后缀，XXX 为 生成的 xml 所在文件夹
