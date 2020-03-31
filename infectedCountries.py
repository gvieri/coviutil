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
from beautifultable import BeautifulTable
import time 

destdir="covid19"
searchdir=destdir+"/csse_covid_19_data/csse_covid_19_daily_reports"

countrynorm={('Iran', 'Iran (Islamic Republic of)'),
('Taiwan', 'Taiwan*'),
(' Azerbaijan', 'Azerbaijan'),
('Russia', 'Russian Federation'),
('Vietnam', 'Viet Nam'),
('UK', 'United Kingdom'),
('Mainland China','China'),
('Czech Republic','Czechia'),
('Hong Kong','Hong Kong SAR')
}


def normalizeCountry(country):
    for c,k in countrynorm:
        if c in country:
            country=k
    return(country)

def normalizeDate(datet):
    structdate=()
    if datet.find("T")>0 :
        structdate=time.strptime(datet,"%Y-%m-%dT%H:%M:%S")
    else:
        (datei,dummy)=datet.split()
        dateo=datei
        structdate=()
        if datei.find('/')>0:
            try:
                structdate=time.strptime(datei,"%m/%d/%Y")
            except Exception:
            ##    structdate=time.strptime(datei,"%m/%d/%y")
                structdate=datei.split('/')
                dep=structdate[2]
                if(len(dep)<4):
                    dep="20"+dep
                structdate[2]=structdate[0]
                structdate[0]=dep
        if datei.find('-')>0:
            structdate=time.strptime(datei,"%Y-%m-%d")
           
    dateo=str(structdate[0])+"-"+str(structdate[1])+"-"+str(structdate[2]) 
    return(dateo)

def getOptions(args=sys.argv[1:]):
    parser=argparse.ArgumentParser(description='fetch official COVID-19 data from github (https://github.com/CSSEGISandData/COVID-19) and, extract the complete list of countries hit by this disease')
    parser.add_argument('-d','--date', help='add start date column to output', action='store_true')
    parser.add_argument('-n','--nicetable', help='it uses beautifultable lib to show the output in a formatted table', action='store_true')
    parser.add_argument('-s','--save', help='save results in a file (without header)', action='store_true' ) 
    opt=parser.parse_args(args)
    return(opt) 


#########################################################
if __name__ == "__main__":
    opt=getOptions()
    dateopt   =opt.date
    save      =opt.save
    nicetable =opt.nicetable
 
    if os.path.isdir(destdir):
        shutil.rmtree(destdir)

    os.mkdir(destdir)

    Repo.clone_from("https://github.com/CSSEGISandData/COVID-19",destdir)

# now search all csv files in destdir/csse_covid_19_data/csse_covid_19_daily_reports

    ext='csv' 

    filenames=listdir(searchdir)
    filenames.sort()
    orig_stdout=sys.stdout

    if nicetable: 
        table=BeautifulTable()
        if dateopt:
            header=["Country","date"]
        else:
            header=["Country"]
        table.column_headers=header
    if save:
        fo=open('infectedcountries.csv','w')
        sys.stdout=fo

    content={}
    for filename in filenames:
       if filename.endswith(ext):
           completefile=searchdir+"/"+filename
           with open(completefile,'r') as fi:
               reader=csv.reader(fi)
               headers=next(reader)
               for row in reader:
#### need to normalize date  Italy 1/31/2020 23:59 to 2020-03-10T19:13:21
#### need to normalize country name as Iran ... 
                   if 'FIPS' in headers[0]:
                      # new layout
                      countryindex=3
                      dateindex   =4
                   else:
                      countryindex=1
                      dateindex   =2
                    
                   country=normalizeCountry(row[countryindex])
                   if country not in content:
                      content[country]=normalizeDate(row[dateindex])


    for c,d in content.items():
        tablerow=[]
        if nicetable: 
            if dateopt:
                tablerow=[c,d]
            else:
                tablerow=[c]
            table.append_row(tablerow)
        else: 
            if dateopt:
                print("{},{}".format(c,d))
            else:
                print("{}".format(c))
    if nicetable:
        print(table)
 
    if save:
        sys.stdout=orig_stdout
        fo.close()
                   




