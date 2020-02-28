# author Giovambattista Vieri
# (c) 2020 all rights reserverd
# license: GPL V 2.0 
# 

from git import Repo
from os import listdir 
import csv
import os
import sys
import shutil
import argparse 
import numpy as np

destdir="covid19"
searchdir=destdir+"/csse_covid_19_data/csse_covid_19_daily_reports"

def getOptions(args=sys.argv[1:]):
    parser=argparse.ArgumentParser(description='fetch official COVID-19 data from github and, make aggregate set')
    parser.add_argument('-r','--ratio', help='add deaths/confirmed and recovered/confirmed ratio columns', action='store_true')
    parser.add_argument('-s','--save', help='save results in a file (without header)', action='store_true' ) 
    parser.add_argument('-d','--debug',help='enables debug info', action='store_true' )
    opt=parser.parse_args(args)
    return(opt) 


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

##########################################
if __name__ == "__main__":
    opt=getOptions()
    ratio=opt.ratio
    save =opt.save
    if os.path.isdir(destdir):
        shutil.rmtree(destdir)

    os.mkdir(destdir)

    Repo.clone_from("https://github.com/CSSEGISandData/COVID-19",destdir)

# now search all csv files in destdir/csse_covid_19_data/csse_covid_19_daily_reports

    ext='csv' 

    filenames=listdir(searchdir)
    filenames.sort()
    orig_stdout=sys.stdout

    if save:
        fo=open('out.csv','w')
        sys.stdout=fo
        
    for filename in filenames:
       if filename.endswith(ext):
           r=list(processafile(filename) )
           if r[1] >0:
                r.append(float(r[1]/r[0]))
           else:
                r.append('NaN')
           if r[2] >0:
                r.append(float(r[2]/r[0]))
           else:
                r.append('NaN')
           
           if ratio:
                print("{},{},{},{},{:.3f},{:.3f}".format(filename[:-4],r[0],r[1],r[2],r[3],r[4]) )
           else: 
                print("{},{},{},{}".format(filename[:-4],r[0],r[1],r[2]) )
    if save:
        sys.stdout=orig_stdout
        fo.close()
