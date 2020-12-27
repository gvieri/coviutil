#coviutil 

Stand for Corona Virus (COVID-19)` Utilities. I want to have some data in tables (I love tabular format). So I written some code. 

License: GPL v 2.0.


I have added some features. First one the help:
python covid19glodata.py --help 
or:
python covid19glodata.py -h . 

So now you can save the aggregate data, and/or you can add Death/Confirmed % ratio AND the recovered/Confirmed ratio % . 
Try:
python covid19glodata.py --ratio 
or
python covid19glodata.py --ratio --save 
and look for result in out.csv (it is a csv file so, you postprocess in excel or whatsoever you like). 

So:
python covid19glodata.py -h 
usage: covid19glodata.py [-h] [-r] [-n] [-s] [-c] [-d]

However now we have the notebook versions. 
Try to https://colab.research.google.com/github/gvieri/coviutil/blob/master/covid19glodata.ipynb. Remember: you needs a valid google account. 

fetch official COVID-19 data from github
(https://github.com/CSSEGISandData/COVID-19) and, make aggregate set

optional arguments:
  -h, --help       show this help message and exit
  -r, --ratio      add deaths/confirmed and recovered/confirmed ratio columns
  -n, --nicetable  it uses beautifultable lib to show the output in a
                   formatted table
  -s, --save       save results in a file (without header)
  -c, --chart      it create single chart of Confirmed, Deaths, Recovered
  -d, --debug      enables debug info



Stay tuned: I'm planning to add some other chart and basic trend analisys. Let me know if you like the idea. 
I've added semilog chart. 

TODO LIST:
* add an option to select a given country (-C ?) 
* add an option to select a given region 
* show some graph
* if the infection will continue, (I hope not) I will add some machine learning related functionnality. 
* your suggestion? 

If you like you can use colab: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/gvieri/coviutil/blob/master/covid19glodata.ipynb) . To use colab you must have a valid google account. 
Enjoy. 

