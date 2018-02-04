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

### Pandas Handling

class Panda_Files:
    def __init__(self):
        filename, file_extension = os.path.splitext(self)
        self.ftype = file_extension     ### file type from extension 
        
    def file_delim(self):
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(csv.read(self))
        return(dialect.delimiter)
        
    def load_file(self):
        if self.ftype == '.csv' or '.txt' or '.asc':
            delim = self.file_delim()
            outfile = pd.read_csv(self,sep=delim)
        elif self.ftype == '.xls' or '.xlsx':
            outfile = pd.ExcelFile(self)
        elif self.type == '.json':
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
        

      