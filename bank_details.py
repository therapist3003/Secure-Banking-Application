# -*- coding: utf-8 -*-
"""
Created on Tue May 31 12:59:23 2022

@author: microsoft
"""

#creating table

import sqlite3
con=sqlite3.connect('bank_details.db')
con.execute("create table bank_details(Username string,Password string,Full_name string,Email_id string,Contact_no integer,City string,Gender string,Date integer,Month integer,Year integer,town string,vacation string,school string,Account_no integer,Balance float,Debit_card_no integer,cvv_no integer,status string,card_limit integer,security_pin integer)")
con.commit()
print("Table is created")