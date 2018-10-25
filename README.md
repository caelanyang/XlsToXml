# 将 APP 开发多语言表格生成 Android string.xml ，以及 iOS Localizable.strings 的脚本
### 多语言 xls 生成  Android xml /iOS Localizable.strings
### 2018.10.25 新增支持将新增多语言直接写入 iOS 或 Android 项目的多语言文件


## 1.使用前准备

- 安装 Python 3（最新版本是3.65）
- 安装 两个 Python Package ----pyexcelerator 和 xlrd （命令行：pip install XXX）
- 简单处理多语言表格：插入一列至表格的首列，并对对应的 string 命名 id。（相当于提前给字符指定 Android 中的 R.id.... 或者 iOS当中的 key）

## 2.常规使用
cd 到 start.py 所在文件夹，并将多语言 xls 表格复制到同一文件夹下。
在本文件夹下运行  `python start.py -f  xxx.xls -t XXX`  （xxx.xls 为多语言表格名称加后缀，XXX 为 生成的 strings.xml以及 Localizable.strings 所在文件夹（`python start.py -f  xxx.xls -t .`）生成到当前脚本文件夹

## 3.直接写入 Android 多语言 strings.xml 或 iOS 的 Localizable.strings

请先完成 **使用前准备**

然后检查表格第一行的国家代码，如果 写入 Android 项目的话，表格中国家代码要分别与 res 文件夹下 values-xx 中的 xx 一致，如果是英文，则直接写 en ，对应 res 文件夹下的英文文件夹 values。如果是 iOS 项目，则表格中国家代码要分别与 Localization 下的 xx.lproj 中的 xx 保持一致。

确认代码无误后

Android 在脚本所在文件夹下运行 `python start.py -f xxx/xxx.xls -t xxx/xxx/res -w 1`，其中 xxx/xxx.xls 为多语言表格路径，xxx/xxx/res 为 Android res 文件夹的路径。

iOS 在脚本所在文件夹下运行 `python start.py -f xxx/xxx.xls -t xxx/xxx/Localization -w 0`，其中 xxx/xxx.xls 为多语言表格路径，xxx/xxx/Localization 为 iOS Localization 文件夹的路径。

脚本运行完毕，写入即完成

同时，脚本会在脚本所在的文件夹也会生成 **常规使用** 中的 strings.xml 或 iOS 的 Localizable.strings，可以按需取用。

