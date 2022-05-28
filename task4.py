import os
import yara
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path',help='Add the path you want the exp to match')
parser.add_argument('-r',help='regex exp here.')
arg = parser.parse_args()
rules=yara.compile(filepath=arg.r)

def search(file):
    if(os.path.isdir(file)):
        if(os.listdir(file)):
            arr=os.listdir(file)
            for i in arr:
                check(file+'/'+entries)
    else:
        regex=re.compile(arg.r)
	if(regex.search(file)):
		print(file)



search(arg.path)
