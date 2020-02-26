# author Giovambattista Vieri
# (c) 2020 all rights reserverd
# license: GPL V 2.0 
# 

from git import Repo
from os import listdir 
import csv
import os
import shutil

destdir="covid19"
searchdir=destdir+"/csse_covid_19_data/csse_covid_19_daily_reports"

def processafile(filename):
    completefile=searchdir+"/"+filename
    confirmed=deaths=recovered=0
    with open(completefile,'r') as fi:
        reader=csv.reader(fi)
        next(reader)
        for row in reader:
            if len(row[3])<1: row[3]=0
            if len(row[4])<1: row[4]=0
            if len(row[5])<1: row[5]=0
            confirmed +=int(row[3])
            deaths    +=int(row[4])
            recovered +=int(row[5])
    return(confirmed,deaths,recovered)


if os.path.isdir(destdir):
    shutil.rmtree(destdir)

os.mkdir(destdir)

Repo.clone_from("https://github.com/CSSEGISandData/COVID-19",destdir)

# now search all csv files in destdir/csse_covid_19_data/csse_covid_19_daily_reports

ext='csv' 

filenames=listdir(searchdir)
filenames.sort()

for filename in filenames:
   if filename.endswith(ext):
       r=processafile(filename) 
       print("{},{},{},{}".format(filename[:-4],r[0],r[1],r[2]) )


