#!/usr/bin/env python
# -*- coding: utf-8 -*

import os
import shutil

path = "/Users/user/Desktop/"
os.chdir(path)
files = os.listdir()

def change_file_name_png(x):
    str_files = x.replace(" ", "")
    str_files = str_files.replace(".", "")
    str_files = str_files.replace("-", '')
    str_files = str_files.replace("png", "")

    if "スクリーンショット" in str_files:
        str_files = str_files.replace("スクリーンショット", "Pict")
    if "20" in str_files:
        cnt = str_files.index("20")
        file_date = str(str_files[4:10])
        str_files = str_files.replace(file_date, "")
    else:
        file_date = "PNG"

    if not os.path.exists(path + "Screenshots/" + file_date + "/"):
        os.makedirs(path + "Screenshots/" + file_date + "/")
        os.chmod(path + "Screenshots/" + file_date + "/", 0o744)
    shutil.move(path + x, path + "Screenshots/" + file_date + "/" + str_files + ".png")

for i in files:
    if ".png" in i:
        change_file_name_png(i)

print('finish')