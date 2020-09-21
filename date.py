'''
                              Requriement Specifications
                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                              1. Should be able to add to a date year,month,week,day
                              2. Should be able to substract from a date year,month,week,day
                              3. The defaults will be all set as per the system date and time, if not provided.
                              4. Find the day of the week for a given date.
                              5. Architecture Overview
                                             .... 
                                             Choice of date(user/system)
                                             add/ substract
                                             years/months/weeks/day to add or sub
                                             
                                        
                              
'''
from datetime import *
from time import *
def ask():
    ch=input("\n\tPress 1 for entering your choice of date\n\tPress 2 for going with the system's date\n\n\t")
    specDate() if ch=='1' else useSystemUnits()

def select(lst):
    inp = [int(x) for x in input('\n\nEnter years,months,weeks,days seperated by a space to add/substract to/from specified date......\nPress 0 to skip a field,if any\n\n').split(' ')]
    ch=input("\n\nPress + to add - to substract??\n\n")
    addDays(lst,inp) if ch=='+' else subDays(lst,inp)
    
def useSystemUnits():
    x=localtime(time())
    l=[]
    l.append(x.tm_year)
    l.append(x.tm_mon)
    l.append(x.tm_mday)
    select(l)
    
def specDate():
    d = [int(x) for x in input('\tEnter your choice of date in the format dd/mm/yyyy format.\t\n\n').split('/')]
    l=[]
    l.append(d[2])
    l.append(d[1])
    l.append(d[0])
    select(l)

def disp(l):
    print('\n\tThe resultant date would be: \t\n',(l.strftime("%A, %d %B %Y")),sep='\t') 
    
def addDays(l,p):
    l[0]+=p[0]
    l[1]+=p[1]
    if l[1]>12:
        ty,tm=divmod(l[1],12)
        l[0]+=ty 
        # yr is the resultant year
        # tm is the resultant month
        # create DateTime obj with these values.
        de = datetime(l[0],tm,l[2])
        r = de + timedelta(weeks=p[2],days=p[3])
        disp(r)
    else:
        de = datetime(l[0],l[1],l[2])
        r = de + timedelta(weeks=p[2],days=p[3])
        disp(r)

    
def subDays(l,p):
    l[0]-=p[0]
    if p[1]==12:
        l[0]-=1
        de = datetime(l[0],l[1],l[2])
        r = de - timedelta(weeks=p[2],days=p[3])
        disp(r)
    elif p[1]>12:
        ty,tm=divmod(p[1],12)
        l[0]-=ty
        de = datetime(l[0],tm,l[2])
        r = de - timedelta(weeks=p[2],days=p[3])
        disp(r)
    else:
        # here again we have 3 conditions........
        if (l[1]-p[1])<0:
            l[0]-=1
            res_mon=(12-(p[1]-l[1]))
            de = datetime(l[0],res_mon,l[2])
            r = de - timedelta(weeks=p[2],days=p[3])
            disp(r)
        elif (l[1]-p[1])==0:
            l[0]-=1
            de = datetime(l[0],12,l[2])
            r = de - timedelta(weeks=p[2],days=p[3])
            disp(r)
        else:
            l[1]-=p[1]
            de = datetime(l[0],l[1],l[2])
            r = de - timedelta(weeks=p[2],days=p[3])
            disp(r)
            
ask()
        

