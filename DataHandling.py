# -*- coding: utf-8 -*-
"""############################################################################
###
### DataHandling
### This file is part of Data-Processing
### This file was created by Dr Daniel Parker on Sat Feb  3 17:54:10 2018 
###    Twitter: @DrDanParker     GitHub:https://github.com/DrDanParker 
###     
### Copyright (C) 2018 University of Salford - All Rights Reserved
### You may use, distribute and modify this code under the terms of MIT Licence
### See LICENSE or go to https://tldrlegal.com/license/mit-license for full licence details
###
### Based on the following:
###     general panda docs and online tutorials
###     
###
############################################################################"""

import os, csv, html5lib
import numpy as np
import pandas as pd

### File List Managers

def grp_by_prefix(filelist,seperator='_'):
    ### Groups a list of files based on common prefix
    # find unique prefixes
    pref = []
    used = set()
    for file in filelist:
        pref.append(os.path.basename(file).split(seperator)[0])
    unique = [x for x in pref if x not in used and (used.add(x) or True)]
    # group files based on prefix
    groups = []    
    for i in range(0,len(unique)):
        grp = []
        for j in range(0,len(pref)):
            if pref[j] == unique[i]:
                grp.append(filelist[j])
        groups.append(grp)
    return(groups)



### Pandas Handling

class Panda_Files:
    def __init__(self,fname):
        filename, file_extension = os.path.splitext(fname)
        self.ftype = file_extension     ### file type from extension 
        
    def file_delim(self,fname):
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(csv.read(fname))
        return(dialect.delimiter)
        
    def load_file(self):
        filename, file_extension = os.path.splitext(self)
        if file_extension == '.csv' or '.txt' or '.asc':
            delim = Panda_Files.file_delim(self)
            outfile = pd.read_csv(self,sep=delim)
        elif file_extension == '.xls' or '.xlsx':
            outfile = pd.ExcelFile(self)
        elif file_extension == '.json':
            outfile = pd.read_json(self) 
        else:
            print('not recognised file type')
        return(outfile)    

### Panda Scrape

class Web_Scrape:
    def __init__(self):
        pass
    
    def load_page(self):
        outfile = pd.read_html(self)
        return(outfile)

    def load_json(self):
        outfile = pd.read_json(self)
        return(outfile)
        

      
