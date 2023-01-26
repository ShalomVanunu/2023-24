
import os
import shutil

files_in_dir = os.listdir()
src_path = "shalom.txt"
dst_path = r"shalom\\"
shutil.copy(src_path, dst_path)
os.remove("shalom.txt")