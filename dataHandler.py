#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:52:07 2017

@author: garrettlee
"""

import pandas as pd
import numpy as np
import time

import kraken
import poloniex



def createTimeStamp(datestr, format="%Y-%m-%d %H:%M:%S"):
    return time.mktime(time.strptime(datestr, format))

kraken.getOrders()