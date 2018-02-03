# -*- coding: utf-8 -*-
"""############################################################################
###
### DataHandling
### This file is part of Snippets
### This file was created by Dr Daniel Parker on Sat Feb  3 17:54:10 2018 
###    Twitter: @DrDanParker     GitHub:https://github.com/DrDanParker 
###     
### Copyright (C) 2018 University of Salford - All Rights Reserved
### You may use, distribute and modify this code under the terms of MIT Licence
### See LICENSE or go to https://tldrlegal.com/license/mit-license for full licence details
###
### Based on the following:
###     
###     
###
############################################################################"""

import os
import numpy as np
import pandas as pd


File = 'C:\Syncplicity\UoS Work\Code\UdemyCourse\scriptsLecture\scriptsLecture\section4\Resp2.csv'

### Pandas Handling

class Panda_Files:
    def __init__(self):
        filename, file_extension = os.path.splitext(self)
        self.ftype = file_extension     ### file type from extension 
        
    def filetype(self):
                