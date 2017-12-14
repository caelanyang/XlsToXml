from optparse import OptionParser
from importlib import reload
import sys
import xlrd
import os


def add_parser():
    parser = OptionParser()

    parser.add_option("-f", "--file_path",
                      help="original.xls File Path.",
                      metavar="file_path")

    parser.add_option("-t", "--target_path",
                      help="Target Folder Path.",
                      metavar="target_path")

    (options, args) = parser.parse_args()
    print("options: %s, args: %s" % (options, args))

    return options


def start_convert(options):
    file_path = options.file_path
    target_path = options.target_path

    if file_path is not None:
        if target_path is None:
            print("targetPath is None！use -h for help.")
            return

        print("read xls file from: " + file_path)
        xls_file = XlsUtil(file_path)

        table = xls_file.get_table_by_index(0)
        convert_android_file(table, target_path)

        print("Finished, see: " + target_path)

    else:
        print().error("file path is None！use -h for help.")


def convert_android_file(table, target_path):
    first_row = table.row_values(0)

    keys = table.col_values(0)
    del keys[0]

    for index in range(len(first_row)):
        if index > 0:
            language_name = first_row[index]
            values = table.col_values(index)
            del values[0]
            write_to_file(keys, values, target_path, language_name)


class XlsUtil:
    def __init__(self, file_path):
        self.filePath = file_path
        reload(sys)
        self.data = xlrd.open_workbook(file_path)

    def get_table_by_index(self, index):
        if 0 <= index < len(self.data.sheets()):
            return self.data.sheets()[index]
        else:
            print("XlsUtil error -- getTable:index")


def write_to_file(keys, values, target_path, language_name):
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    print("reading language for: " + language_name + " to " + target_path + "/strings.xml")

    fo = open(target_path + "/strings.xml", "a", encoding="utf8")

    if language_name is not None:
        fo.write(language_name + "\n")

    for x in range(len(keys)):
        if values[x] is None or values[x] == '':
            print("Key:" + keys[x] + "\'s value is None. Index:" + str(x + 1))
            continue

        key = keys[x]
        value = values[x]
        content = "<string name=\"" + key + "\">" + value + "</string>\n"
        fo.write(content)

    fo.write("\n")
    fo.close()


def main():
    options = add_parser()
    start_convert(options)


main()