
import hashlib

cat_file = open("cat.jpg","rb")
cat_picture = cat_file.read()

hash_md5 = hashlib.md5(cat_picture) # make hash MD5 to  string

#
print(hash_md5.hexdigest())

cat_file = open("cat1.jpg","rb")
cat_picture = cat_file.read()

hash_md5 = hashlib.md5(cat_picture) # make hash MD5 to  string

#
print(hash_md5.hexdigest())