'''
This is a program to auto unzip the tar file and update to HDFS
The command for run:

python deploy.py --package /path/you/put/tar.gz/file --install_root /path/you/want/to/put/on/hdfs

'''

import tarfile
import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--package", help = "specify the package path" , type = str)
parser.add_argument("--install_root", help = "specify the install root", type = str)
args = parser.parse_args()

package_path = args.package
install_root = args.install_root

if not install_root.endswith("/"):
	install_root = install_root + "/"


print "executing deploy script, the package path is {0}, the install_root is {1}".format(package_path, install_root)


tar = tarfile.open(package_path,"r:gz")

print "unzipping the package file to the current directory"

tar.extractall()

for tarinfo in tar:
	#This selects all the root folder
    print "copying folder {0}".format(tarinfo.name)
    os.system("hadoop fs -put {0} {1}".format(tarinfo.name, install_root))


print "deployment completed"

tar.close()
