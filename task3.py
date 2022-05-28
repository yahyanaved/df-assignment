import os
import yara
import argparse
parser=argparse.ArgumentParser(description='match any YARA signatures against a file')
parser.add_argument('path',help='the file to run signatures against')
parser.add_argument('-r',help='a single yara rule to match for')
arg=parser.parse_args()
rules=yara.compile(filepath=arg.r)
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

