# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:24:47 2022

@author: microsoft
"""

#creating table

import sqlite3
con1=sqlite3.connect('logs.db')
con1.execute("create table logs(Date integer,Transaction_id  integer,Account_no integer,Balance float,Note string)")
con1.commit()
print("Table is created")