# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re, cgi
from random import randint
from datetime import datetime
import pymysql
import time
from time import sleep
import os


#Database config
conn = pymysql.connect(
    db='scraper',
    user='root',
    passwd='',
    host='localhost',
charset='utf8')
c = conn.cursor()
c.execute('SET NAMES utf8;')
c.execute('SET CHARACTER SET utf8;')
c.execute('SET character_set_connection=utf8;')
c.execute("DELETE  FROM today_matches")

tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')

linki_tekme = set() #List of links sites
seznam_oglasov = set()
trenuten_datum=datetime.now().strftime('%d-%m-%Y %H:%M:%S')
trenuten_datum_xml=datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
time_of_start = time.time() #Log start time so i can use it to get execution time




def get_all_links():
      zz = 0
      with urllib.request.urlopen("http://www.zulubet.com") as url:
       r = url.read()
      soup = BeautifulSoup(r, "html.parser")
      for link in soup.find_all('a'):
        zz+=1
        aa = link.get('href')
        if 'match' in str(aa):
         linki_tekme.add(aa)



def print_links(linki_tekme):
    z=0
    for link in linki_tekme:
        print ("Link: "+str(link)) #Debug data
        z+=1
    print ("Tekem: "+str(z)) #Debug data

def loop_over_links():
    z=0
    for link in linki_tekme:
        get_data_from_link(link)
        z+=1



def get_data_from_link(tekma_link):
    with urllib.request.urlopen(tekma_link) as url:
        r = url.read()
    soup = BeautifulSoup(r, "html.parser")

    #Imena ekip
    tekma=soup.find_all("h3")
    stx=0
    for ekipa in tekma:
        stx+=1
        if(stx==1):
         ekipa1=ekipa.text;
         print("EKIPA1: "+ekipa.text)
        if (stx == 2):
         ekipa2 = ekipa.text;
         print("EKIPA2: " + ekipa.text)
    tekma_final=ekipa1+" - "+ekipa2
    #datum
    dd = soup.find_all("td", {"width": "75"})
    for aa in dd:
        dt=aa.text;
        datum_tekme=dt.split(';')[1].replace(",", "-")
        print(datum_tekme)


    table = soup.find_all("td", {"align": "center"})
    stevec=0;


    #VARS
    #PRVA TABELA DATA
    prva_1_out_prediction="-" #25
    prva_x_out_prediction="-" #26
    prva_2_out_prediction ="-" #27
    prva_tips_out_prediction="-" #28

    prva_odds_1="-" #31
    prva_odds_x = "-" #32
    prva_odds_2 = "-" #33
    prva_odds_u2_5 = "-"  # 34
    prva_odds_o2_5 = "-"  # 35

    #Druga tabela

    druga_matches = '-'  # 40
    druga_goals = '-'  # 41
    druga_avg_goals='-' #42

    druga_0_1_goals='-' #46
    druga_2_3_goals = '-'  # 47
    druga_4_goals = '-'  # 48

    druga_under_over_1_5m = '-'  # 57
    druga_under_over_1_5p = '-'  # 58
    druga_under_over_2_5m = '-'  # 59
    druga_under_over_2_5p = '-'  # 60
    druga_under_over_3_5m = '-'  # 61
    druga_under_over_3_5p = '-'  # 62
    druga_under_over_4_5m = '-'  # 63
    druga_under_over_4_5p = '-'  # 64

    druga_total_goals_0 ='' #73
    druga_total_goals_1p = ''  # 74
    druga_total_goals_2p = ''  # 75
    druga_total_goals_3p = ''  # 76
    druga_total_goals_4p = ''  # 77
    druga_total_goals_5p = ''  # 78
    druga_total_goals_6p = ''  # 79
    druga_total_goals_7p = ''  # 80

    #Tretja tabela

    tretja_matches = '-'  # 84
    tretja_goals = '-'  # 85
    tretja_avg_goals = '-'  # 86

    tretja_0_1_goals = '-'  # 90
    tretja_2_3_goals = '-'  # 91
    tretja_4_goals = '-'  # 92

    tretja_under_over_1_5m = '-'  # 101
    tretja_under_over_1_5p = '-'  # 102
    tretja_under_over_2_5m = '-'  # 103
    tretja_under_over_2_5p = '-'  # 104
    tretja_under_over_3_5m = '-'  # 105
    tretja_under_over_3_5p = '-'  # 106
    tretja_under_over_4_5m = '-'  # 107
    tretja_under_over_4_5p = '-'  # 108

    tretja_total_goals_0 = ''  # 117
    tretja_total_goals_1p = ''  # 118
    tretja_total_goals_2p = ''  # 119
    tretja_total_goals_3p = ''  # 120
    tretja_total_goals_4p = ''  # 121
    tretja_total_goals_5p = ''  # 122
    tretja_total_goals_6p = ''  # 123
    tretja_total_goals_7p = ''  # 124


    no=0
    for td in table:
        stevec += 1
        #---------TABELA 1--------------------
        if(stevec==25):
            prva_1_out_prediction = td.text.replace("%", "").replace("%", "") # 25
            #print("prva_1_out_prediction: "+prva_1_out_prediction)
        if (stevec == 26):
            prva_x_out_prediction = td.text.replace("%", "")  # 26
            #print("prva_x_out_prediction: " + prva_x_out_prediction)
        if (stevec == 27):
            prva_2_out_prediction = td.text.replace("%", "")  # 27
            #print("prva_2_out_prediction: " + prva_2_out_prediction)
        if (stevec == 28):
            prva_tips_out_prediction = td.text.replace("%", "")  # 28
           # print("prva_tips_out_prediction: " + prva_tips_out_prediction)
        if (stevec == 31):
            prva_odds_1 = td.text.replace("%", "")  # 31
            #print("prva_odds_1: " + prva_odds_1)
        if (stevec == 32):
            prva_odds_x = td.text.replace("%", "")  # 32
           # print("prva_odds_x: " + prva_odds_x)
        if (stevec == 33):
            prva_odds_2 = td.text.replace("%", "")  # 33
            #print("prva_odds_2: " + prva_odds_2)
        if (stevec == 34):
            prva_odds_u2_5 = td.text.replace("%", "")  # 34
           # print("prva_odds_u2_5: " + prva_odds_u2_5)
        if (stevec == 35):
            prva_odds_o2_5 = td.text.replace("%", "")  # 35
           # print("prva_odds_o2_5: " + prva_odds_o2_5)
        #------TABELA 2--------------------------
            # Druga tabela
        if (stevec == 40):
            druga_matches = td.text.replace("%", "")  # 40
        if (stevec == 41):
            druga_goals = td.text.replace("%", "")  # 41
        if (stevec == 42):
            druga_avg_goals = td.text.replace("%", "")  # 42
        if (stevec == 46):
            druga_0_1_goals = td.text.replace("%", "")  # 46
        if (stevec == 47):
            druga_2_3_goals = td.text.replace("%", "")  # 47
        if (stevec == 48):
            druga_4_goals = td.text.replace("%", "")  # 48
        if (stevec == 57):
            druga_under_over_1_5m = td.text.replace("%", "")  # 57
        if (stevec == 58):
            druga_under_over_1_5p = td.text.replace("%", "")  # 58
        if (stevec == 59):
            druga_under_over_2_5m = td.text.replace("%", "")  # 59
        if (stevec == 60):
            druga_under_over_2_5p = td.text.replace("%", "")  # 60
        if (stevec == 61):
            druga_under_over_3_5m = td.text.replace("%", "")  # 61
        if (stevec == 62):
            druga_under_over_3_5p = td.text.replace("%", "")  # 62
        if (stevec == 63):
            druga_under_over_4_5m = td.text.replace("%", "")  # 63
        if (stevec == 64):
            druga_under_over_4_5p = td.text.replace("%", "")  # 64
        if (stevec == 73):
            druga_total_goals_0 = td.text.replace("%", "")  # 73
        if (stevec == 74):
            druga_total_goals_1p = td.text.replace("%", "")  # 74
        if (stevec == 75):
            druga_total_goals_2p = td.text.replace("%", "")  # 75
        if (stevec == 76):
            druga_total_goals_3p = td.text.replace("%", "")  # 76
        if (stevec == 77):
            druga_total_goals_4p = td.text.replace("%", "")  # 77
        if (stevec == 78):
            druga_total_goals_5p = td.text.replace("%", "")  # 78
        if (stevec == 79):
            druga_total_goals_6p = td.text.replace("%", "")  # 79
        if (stevec == 80):
            druga_total_goals_7p = td.text.replace("%", "")  # 80

            # Tretja tabela
        if (stevec == 84):
            tretja_matches = td.text.replace("%", "")  # 84
        if (stevec == 85):
            tretja_goals = td.text.replace("%", "")  # 85
        if (stevec == 86):
            tretja_avg_goals = td.text.replace("%", "")  # 86
        if (stevec == 90):
            tretja_0_1_goals = td.text.replace("%", "")  # 90
        if (stevec == 91):
            tretja_2_3_goals = td.text.replace("%", "")  # 91
        if (stevec == 92):
            tretja_4_goals = td.text.replace("%", "")  # 92
        if (stevec == 101):
            tretja_under_over_1_5m = td.text.replace("%", "")  # 101
        if (stevec == 102):
            tretja_under_over_1_5p = td.text.replace("%", "")  # 102
        if (stevec == 103):
            tretja_under_over_2_5m = td.text.replace("%", "")  # 103
        if (stevec == 104):
            tretja_under_over_2_5p = td.text.replace("%", "")  # 104
        if (stevec == 105):
            tretja_under_over_3_5m = td.text.replace("%", "")  # 105
        if (stevec == 106):
            tretja_under_over_3_5p = td.text.replace("%", "")  # 106
        if (stevec == 107):
            tretja_under_over_4_5m = td.text.replace("%", "")  # 107
        if (stevec == 108):
            tretja_under_over_4_5p = td.text.replace("%", "")  # 108
        if (stevec == 117):
            tretja_total_goals_0 = td.text.replace("%", "")  # 117
        if (stevec == 118):
            tretja_total_goals_1p = td.text.replace("%", "")  # 118
        if (stevec == 119):
            tretja_total_goals_2p = td.text.replace("%", "")  # 119
        if (stevec == 120):
            tretja_total_goals_3p = td.text.replace("%", "")  # 120
        if (stevec == 121):
            tretja_total_goals_4p = td.text.replace("%", "")  # 121
        if (stevec == 122):
            tretja_total_goals_5p = td.text.replace("%", "")  # 122
        if (stevec == 123):
            tretja_total_goals_6p = td.text.replace("%", "")  # 123
        if (stevec == 124):
            tretja_total_goals_7p = td.text.replace("%", "")  # 124
        if "games" in prva_odds_2:
            no=1

        #print("(" + str(stevec) + ")")
        #print(td.text.replace("%", ""))


    date = trenuten_datum

    loggit = """
                     INSERT INTO today_matches (
                      date,
                      match_date,
                      teams,
                      prva_1_out_prediction,
                      prva_x_out_prediction,
                      prva_2_out_prediction,
                      prva_tips_out_prediction,
                      prva_odds_1,
                      prva_odds_x,
                      prva_odds_2,
                      prva_odds_u2_5,
                      prva_odds_o2_5,
                      druga_matches,
                      druga_goals,
                      druga_avg_goals,
                      druga_0_1_goals,
                      druga_2_3_goals,
                      druga_4_goals,
                      druga_under_over_1_5m,
                      druga_under_over_1_5p,
                      druga_under_over_2_5m,
                      druga_under_over_2_5p,
                      druga_under_over_3_5m,
                      druga_under_over_3_5p,
                      druga_under_over_4_5m,
                      druga_under_over_4_5p,
                      druga_total_goals_0,
                      druga_total_goals_1p,
                      druga_total_goals_2p,
                      druga_total_goals_3p,
                      druga_total_goals_4p,
                      druga_total_goals_5p,
                      druga_total_goals_6p,
                      druga_total_goals_7p,
                      tretja_matches,
                      tretja_goals,
                      tretja_avg_goals,
                      tretja_0_1_goals,
                      tretja_2_3_goals,
                      tretja_4_goals,
                      tretja_under_over_1_5m,
                      tretja_under_over_1_5p,
                      tretja_under_over_2_5p,
                      tretja_under_over_2_5m,
                      tretja_under_over_3_5m,
                      tretja_under_over_3_5p,
                      tretja_under_over_4_5m,
                      tretja_under_over_4_5p,
                      tretja_total_goals_0,
                      tretja_total_goals_1p,
                      tretja_total_goals_2p,
                      tretja_total_goals_3p,
                      tretja_total_goals_4p,
                      tretja_total_goals_5p,
                      tretja_total_goals_6p,
                      tretja_total_goals_7p)
                     VALUES
                         (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                 """
    if no!=1:
     no=0
     c.execute(loggit, (
        date,
        datum_tekme,
        tekma_final,
        prva_1_out_prediction,
        prva_x_out_prediction,
        prva_2_out_prediction,
        prva_tips_out_prediction,
        prva_odds_1,
        prva_odds_x,
        prva_odds_2,
        prva_odds_u2_5,
        prva_odds_o2_5,
        druga_matches,
        druga_goals,
        druga_avg_goals,
        druga_0_1_goals,
        druga_2_3_goals,
        druga_4_goals,
        druga_under_over_1_5m,
        druga_under_over_1_5p,
        druga_under_over_2_5m,
        druga_under_over_2_5p,
        druga_under_over_3_5m,
        druga_under_over_3_5p,
        druga_under_over_4_5m,
        druga_under_over_4_5p,
        druga_total_goals_0,
        druga_total_goals_1p,
        druga_total_goals_2p,
        druga_total_goals_3p,
        druga_total_goals_4p,
        druga_total_goals_5p,
        druga_total_goals_6p,
        druga_total_goals_7p,
        tretja_matches,
        tretja_goals,
        tretja_avg_goals,
        tretja_0_1_goals,
        tretja_2_3_goals,
        tretja_4_goals,
        tretja_under_over_1_5m,
        tretja_under_over_1_5p,
        tretja_under_over_2_5p,
        tretja_under_over_2_5m,
        tretja_under_over_3_5m,
        tretja_under_over_3_5p,
        tretja_under_over_4_5m,
        tretja_under_over_4_5p,
        tretja_total_goals_0,
        tretja_total_goals_1p,
        tretja_total_goals_2p,
        tretja_total_goals_3p,
        tretja_total_goals_4p,
        tretja_total_goals_5p,
        tretja_total_goals_6p,
        tretja_total_goals_7p))
     conn.commit()
     print("*****Loged****")


get_all_links()
print_links(linki_tekme)
loop_over_links()




