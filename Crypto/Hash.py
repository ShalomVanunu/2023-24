
import hashlib

text = b"my name is Shalom"
hash_md5 = hashlib.md5(text) # make hash MD5 to  string

print(hash_md5.hexdigest())

text = b"m"
hash_md5 = hashlib.md5(text) # make hash MD5 to  string

print(hash_md5.hexdigest())