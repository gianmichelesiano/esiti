from __future__ import print_function
import glob
import os


#cartella per esiti
percorso = os.getcwd()
path= percorso+"/esiti_veri_tutti/"
os.chdir(path)



if os.path.exists(percorso+'/esiti_veri.txt'):
        print ("Si esiste")
        os.remove(percorso+'/esiti_veri.txt')
else:
        print ('Non ce')

filenames = []
for file in glob.glob("*.txt"):
    print(file)
    filenames.append(file)


with open(percorso+'/esiti_veri.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                cig = line.replace("\r"," ").replace(' ', '')
                outfile.write(cig)


import glob, os

filelist = glob.glob("*.txt")
for f in filelist:
    os.remove(f)

