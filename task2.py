import checksumdir
path1='home/yahya/uni/1'
path2='home/yahya/uni/2'
hash1=checksumdir.dirhash(path1)
hash2=checksumdir.dirhash(path2)
if hash1==hash2:
	print("DIRECTORIES ARE SAME!")
else:
	print("DIRECTORIES ARE NOT SAME!")

