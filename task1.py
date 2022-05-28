import time
import tarfile
import hashlib
import argparse
import os
import pickle
parser = argparse.ArgumentParser(description='backup a device into an image')
parser.add_argument('device', help='the device to use')
arg=parser.parse_args()
from py_essentials import hashing as hs
hash1 = hs.fileChecksum(arg.device, "sha256")
print("HASH GENERATED:" ,hash1)
skey=open("key.bin",'wb')
from cryptography.fernet import Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(hash1.encode())
print(key)
pickle.dump(key,skey)
skey.close()
hashfile=open("hash.bin",'wb')
pickle.dump(encoded_text,hashfile)
print("ENCRYPTED HASH GENERATED AND STORED: " ,encoded_text)
decoded_text = cipher_suite.decrypt(encoded_text)
print("ORIGINAL DECRYPTED HASH: " ,decoded_text)
