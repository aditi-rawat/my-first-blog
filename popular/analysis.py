import pandas as pd, numpy as np, matplotlib.pyplot as plt
#import networkx.algorithms
#from math import sin, cos, sqrt, atan2, radians
#from sklearn.cluster import DBSCAN
#from geopy.distance import great_circle
#import matplotlib.pyplot as plt
#import networkx as nx
#from networkx.algorithms import tree
#from shapely.geometry import MultiPoint
#df = pd.read_csv('summer-travel-gps-full.csv')
#coords = df.as_matrix(columns=['lat', 'lon'])
#import gmplot
import unicodedata
#import pymysql
import sqlite3

y_year=[0,0,0,0,0,0,0,0,0,0,0,0]
x_year=[1,2,3,4,5,6,7,8,9,10,11,12]

y_month=[0,0,0,0,0,0,0]
x_month=[1,2,3,4,5,6,7]

months=['January','February','March','April','May','June','July','August','September','October','November','December']
years=[2011,2012,2013,2014,2015,2016,2017,2018]

conn = sqlite3.connect('db1.sqlite3')

# query=1 for showing the months
# query=2 for showing the years
# stat=0 for showing only total count
# stat=1 for showing only national count
# stat=2 for showing only international count
# stat=3 for showing both

def graphical_analysis(query,stat,ans):
    if query==1:
        y=[0,0,0,0,0,0,0]
        y1=[0,0,0,0,0,0,0]
        #x=[1,4,7,10,13,16,19]
        x=np.arange(7)
        if stat==0:
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2017 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[6]+=c[0][2]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][2]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2016 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[5]+=c[0][2]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][2]

            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2015 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[4]+=c[0][2]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][2]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2014 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[3]+=c[0][2]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][2]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2013 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[2]+=c[0][2]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][2]



            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2012 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[1]+=c[0][2]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][2]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2011 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[0]+=c[0][2]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][2]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][2]
            plt.xlabel('years')
            plt.ylabel('Number of Tourists')
            plt.bar(x+2011,y, color="red")
            plt.show()
            
        elif stat==1:
            
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2017 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[6]+=c[0][0]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][0]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2016 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[5]+=c[0][0]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][0]

            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2015 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[4]+=c[0][0]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][0]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2014 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[3]+=c[0][0]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][0]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2013 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[2]+=c[0][0]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][0]



            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2012 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[1]+=c[0][0]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][0]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2011 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[0]+=c[0][0]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][0]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][0]
            plt.bar(x+2011,y, color="red")
            plt.xlabel('years')
            plt.ylabel('Number of National Tourists')
            plt.show()
            
        elif stat==2:
            
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2017 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[6]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y[6]+=c[0][1]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2016 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[5]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y[5]+=c[0][1]

            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2015 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[4]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y[4]+=c[0][1]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2014 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[3]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y[3]+=c[0][1]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2013 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[2]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y[2]+=c[0][1]



            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2012 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[1]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y[1]+=c[0][1]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2011 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y[0]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y[0]+=c[0][1]

            plt.bar(x+2011,y, color="red")
            plt.xlabel('years')
            plt.ylabel('Number of International Tourists')
            plt.show()
            
        else :
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2011 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y1[0]+=c[0][0]
            y[0]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y1[0]+=c[0][0]
            y[0]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y1[0]+=c[0][0]
            y[0]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y1[0]+=c[0][0]
            y[0]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2011 where month=?",[ans])
            c=cursor.fetchall()
            y1[0]+=c[0][0]
            y[0]+=c[0][1]

            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2012 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y1[1]+=c[0][0]
            y[1]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y1[1]+=c[0][0]
            y[1]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y1[1]+=c[0][0]
            y[1]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y1[1]+=c[0][0]
            y[1]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2012 where month=?",[ans])
            c=cursor.fetchall()
            y1[1]+=c[0][0]
            y[1]+=c[0][1]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2013 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y1[2]+=c[0][0]
            y[2]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y1[2]+=c[0][0]
            y[2]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y1[2]+=c[0][0]
            y[2]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall() 
            y1[2]+=c[0][0]
            y[2]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2013 where month=?",[ans])
            c=cursor.fetchall()
            y1[2]+=c[0][0]
            y[2]+=c[0][1]

            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2014 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y1[3]+=c[0][0]
            y[3]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y1[3]+=c[0][0]
            y[3]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y1[3]+=c[0][0]
            y[3]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y1[3]+=c[0][0]
            y[3]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2014 where month=?",[ans])
            c=cursor.fetchall()
            y1[3]+=c[0][0]
            y[3]+=c[0][1]

            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2015 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y1[4]+=c[0][0]
            y[4]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y1[4]+=c[0][0]
            y[4]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y1[4]+=c[0][0]
            y[4]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y1[4]+=c[0][0]
            y[4]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2015 where month=?",[ans])
            c=cursor.fetchall()
            y1[4]+=c[0][0]
            y[4]+=c[0][1]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2016 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y1[5]+=c[0][0]
            y[5]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y1[5]+=c[0][0]
            y[5]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y1[5]+=c[0][0]
            y[5]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y1[5]+=c[0][0]
            y[5]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2016 where month=?",[ans])
            c=cursor.fetchall()
            y1[5]+=c[0][0]
            y[5]+=c[0][1]


            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2017 where month=?;",[ans])
            c=cursor.fetchall()
            #print c
            y1[6]+=c[0][0]
            y[6]+=c[0][1]
            #print y[i]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y1[6]+=c[0][0]
            y[6]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y1[6]+=c[0][0]
            y[6]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y1[6]+=c[0][0]
            y[6]+=c[0][1]
            cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2017 where month=?",[ans])
            c=cursor.fetchall()
            y1[6]+=c[0][0]
            y[6]+=c[0][1]
            plt.bar(x+2011,y, color="red",width=0.25)
            plt.bar(x+0.25+2011,y1, color="blue",width=0.25)
            plt.xlabel('years')
            plt.ylabel('Number of Tourists')
            plt.show()
    else:
        y=[0,0,0,0,0,0,0,0,0,0,0,0]
        y1=[0,0,0,0,0,0,0,0,0,0,0,0]
        y2=[0,0,0,0,0,0,0,0,0,0,0,0]
        #x=[1,4,7,10,13,16,19]
        x=np.arange(12)
        if ans==2017:
            for i in range(0,12):
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2017 where month=?;",[months[i]])
                c=cursor.fetchall()
                #print c
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                #print y[i]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2017 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2017 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2017 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2017 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                
                
        elif ans==2016:
            for i in range(0,12):
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2016 where month=?;",[months[i]])
                c=cursor.fetchall()
                print c
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                #print y[i]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2016 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2016 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2016 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2016 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                
        elif ans==2015:
            for i in range(0,12):
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2015 where month=?;",[months[i]])
                c=cursor.fetchall()
                #print c
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                #print y[i]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2015 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2015 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2015 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2015 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
        elif ans==2014:
            for i in range(0,12):
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2014 where month=?;",[months[i]])
                c=cursor.fetchall()
                print i
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                #print y[i]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2014 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2014 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2014 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2014 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
        elif ans==2013:
            for i in range(0,12):
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2013 where month=?;",[months[i]])
                c=cursor.fetchall()
                #print c
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                #print y[i]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2013 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2013 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2013 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2013 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
        elif ans==2012:
            for i in range(0,12):
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2012 where month=?;",[months[i]])
                c=cursor.fetchall()
                #print c
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                #print y[i]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2012 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2012 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2012 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2012 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
        elif ans==2011:
            for i in range(0,12):
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2011 where month=?;",[months[i]])
                c=cursor.fetchall()
                #print c
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                #print y[i]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2011 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2011 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2011 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
                cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2011 where month=?",[months[i]])
                c=cursor.fetchall()
                y[i]+=c[0][2]
                y1[i]+=c[0][0]
                y2[i]+=c[0][1]
        if stat==0:
            plt.bar(x+1,y, color="red")
            plt.xlabel('Months of Year=%i'%ans)
            plt.ylabel('Number of Tourists')
            plt.show()
        elif stat==1:
            plt.bar(x+1,y1, color="red")
            plt.xlabel('Months of Year=%i'%ans)
            plt.ylabel('Number of Tourists')
            plt.show()
        elif stat==2:
            plt.bar(x+1,y2, color="red")
            plt.xlabel('Months of Year=%i'%ans)
            plt.ylabel('Number of Tourists')
            plt.show()
        else:
            plt.bar(x+1,y1, color="red",width=0.25)
            plt.bar(x+0.25+1,y2, color="blue",width=0.25)
            plt.xlabel('Months of Year=%i'%ans)
            plt.ylabel('Number of Tourists')
            plt.savefig('pic.png')
            plt.show()
                        


# 2017 stats highlight the reference 
'''for i in range(0,12):
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2017 where month=?;",[months[i]])
    c=cursor.fetchall()
    print c
    y[i]+=c[0][2]
    #print y[i]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2017 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2017 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2017 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2017 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]'''

# 2016 stats

'''for i in range(0,12):
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel1_annualreport_2016 where month=?;",[months[i]])
    c=cursor.fetchall()
    print c
    y[i]+=c[0][2]
    #print y[i]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel2_annualreport_2016 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel3_annualreport_2016 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel4_annualreport_2016 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]
    cursor=conn.execute("select national_count,international_count,total_count from popular_hotel5_annualreport_2016 where month=?",[months[i]])
    c=cursor.fetchall()
    y[i]+=c[0][2]'''

graphical_analysis(2,3,2016)
conn.close()

#y = [123,200,345,322,300,200,340,230,322,400,300,255]
#x = [1,2,3,4,5,6,7,8,9,10,11,12]
#width =1/1.5
#plt.bar(x,y, color="red")
#plt.show()
