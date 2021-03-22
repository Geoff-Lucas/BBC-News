# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 2021

@author: Geoff
"""

import re

month_num_sub = {
    '1': "jan",
    '2': "feb",
    '3': "mar",
    '4': "apr",
    '5': 'may',
    '6': 'jun',
    '7': 'jul',
    '8': 'aug',
    '9': 'sep',
    '10': 'oct',
    '11': 'nov',
    '12': 'dec',
    '01': 'jan',
    '02': 'feb',
    '03': 'mar',
    '04': 'apr',
    '05': 'may',
    '06': 'jun',
    '07': 'jul',
    '08': 'aug',
    '09': 'sep'}
    
def date_norm_mmddyy(date):
     # date = '5-2-1982'
     
    valid_date = True
    date_parts = re.split("\.|-|/", date)
     
    month = ''
    day = ''
    year = ''
     
    try:    
         month = month_num_sub[date_parts[0]]
    except:
         valid_date = False     
     
    day = date_parts[1]
    if len(date_parts[1]) < 2:
         day = "0" + day
         
    try:
        temp = int(day)
        if temp > 31 or temp == 0:
            valid_date = False
    except:
        valid_date = False
        
    year = date_parts[2]
        
    if len(year) != 4:
        
        temp = 0
        try:
            temp = int(year)
        except:
            valid_date = False
        
        if valid_date:
            if temp < 30:
                temp += 2000
            elif temp >= 30 and temp < 100:
                temp += 1900
            else:
                valid_date = False
                
        year = str(temp)
        
    if valid_date:
        return " " + month + "-" + day + "-" + year + " "
    else:
        return 'invalid_date'
         
long_month = {
    'january': 'jan',
    'february': 'feb',
    'march': 'mar',
    'april': 'apr',
    'may': 'may',
    'june': 'jun',
    'july': 'jul',
    'august': 'aug',
    'september': 'sep',
    'october': 'oct',
    'november': 'nov',
    'december': 'dec',
    'jan': 'jan',
    'feb': 'feb',
    'mar': 'mar',
    'apr': 'apr',
    'jun': 'jun',
    'jul': 'jul',
    'aug': 'aug',
    'sep': 'sep',
    'oct': 'oct',
    'nov': 'nov',
    'dec': 'dec'}
 
def date_norm_month(date):
    # date = 'march 4, 1993'
    
    valid_date = True
    date_parts = re.split("\.|, |-|/| |,", date)
    year = date_parts[-1]
    mon = ''
    day = ''
    
    # i.e. May 1982 just, use 1 for day
    if len(date_parts) == 2:
        try:
            mon = long_month[date_parts[0]]
        except:
            valid_date = False
            
        day = 1
        
    elif len(date_parts) == 3:
        try:
            day = int(date_parts[1])
            mon = date_parts[0]
        except: 
            try:
                day = int(date_parts[0])
                mon = date_parts[1]
            except:
                valid_date = False
                
        if valid_date:
            try:
                mon = long_month[mon]
            except:
                valid_date = False
    else:
        valid_date = False
        
    if valid_date:
        
        if day > 31 or day == 0:
            valid_date = False
        else:
            day = str(day)
            if len(day) == 1:
                day = '0' + day
                
        if len(year) != 4:
           
           temp = 0
           try:
               temp = int(year)
           except:
               valid_date = False
           
           if valid_date:
               if temp < 30:
                   year = str(temp + 2000)
               elif temp >= 30 and temp < 100:
                   year = str(temp + 1900)
               else:
                   valid_date = False
             
    if valid_date:
        return " " + mon + "-" + day + "-" + year + " "
        
    else:
        return "invalid_date"
    