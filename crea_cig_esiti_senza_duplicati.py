# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import MySQLdb
import urllib
import urllib2
import re
import string
from bs4 import BeautifulSoup
from datetime import datetime
import datetime as dt
import calendar
import time
import os
import json as m_json
import duckduckgo
import requests
import urllib2

import DBconnection
conn= DBconnection.connection()


def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))


def getgoogleurl(search,siteurl=False):
    if siteurl==False:
        return 'http://www.google.com/search?q='+urllib2.quote(search)
    else:
        return 'http://www.google.com/search?q=site:'+urllib2.quote(siteurl)+'%20'+urllib2.quote(search)



def trova_sito (ente):
    try:
        link = duckduckgo.get_zci(ente)
    except:
        link = ''
    return link



def trova_cat_da_cpv (CPV):

    cursore = conn.cursor()
    cursore.execute("SELECT * FROM gare.cpv_to_cat where CPV = '"+CPV+"'")
    CPV_trovati = cursore.fetchall()

    n_OG1= 0
    n_OG2 = 0
    n_OG3 = 0
    n_OG4 = 0
    n_OG5=0
    n_OG6=0
    n_OG7=0
    n_OG8=0
    n_OG9=0
    n_OG10=0
    n_OG11=0
    n_OG12=0
    n_OG13=0
    n_OS1=0
    n_OS2A=0
    n_OS2B=0
    n_OS3=0
    n_OS4=0
    n_OS5=0
    n_OS6=0
    n_OS7=0
    n_OS8=0
    n_OS9=0
    n_OS10=0
    n_OS11=0
    n_OS12A=0
    n_OS12B=0
    n_OS13=0
    n_OS14=0
    n_OS15=0
    n_OS16=0
    n_OS17=0
    n_OS18A=0
    n_OS18B=0
    n_OS19=0
    n_OS20A=0
    n_OS20B=0
    n_OS21=0
    n_OS22=0
    n_OS23=0
    n_OS24=0
    n_OS25=0
    n_OS26=0
    n_OS27=0
    n_OS28=0
    n_OS29=0
    n_OS30=0
    n_OS31=0
    n_OS32=0
    n_OS33=0
    n_OS34=0
    n_OS35=0

    for y in CPV_trovati:
            categoria = y[1]
            if categoria=='OG1': n_OG1 = n_OG1+1
            elif categoria =='OG1': n_OG1= n_OG1+1
            elif categoria =='OG2': n_OG2= n_OG2+1
            elif categoria =='OG3': n_OG3= n_OG3+1
            elif categoria =='OG4': n_OG4= n_OG4+1
            elif categoria =='OG5': n_OG5= n_OG5+1
            elif categoria =='OG6': n_OG6= n_OG6+1
            elif categoria =='OG7': n_OG7= n_OG7+1
            elif categoria =='OG8': n_OG8= n_OG8+1
            elif categoria =='OG9': n_OG9= n_OG9+1
            elif categoria =='OG10': n_OG10= n_OG10+1
            elif categoria =='OG11': n_OG11= n_OG11+1
            elif categoria =='OG12': n_OG12= n_OG12+1
            elif categoria =='OG13': n_OG13= n_OG13+1
            elif categoria =='OS1': n_OS1= n_OS1+1
            elif categoria =='OS2-A': n_OS2A= n_OS2A+1
            elif categoria =='OS2-B': n_OS2B= n_OS2B+1
            elif categoria =='OS3': n_OS3= n_OS3+1
            elif categoria =='OS4': n_OS4= n_OS4+1
            elif categoria =='OS5': n_OS5= n_OS5+1
            elif categoria =='OS6': n_OS6= n_OS6+1
            elif categoria =='OS7': n_OS7= n_OS7+1
            elif categoria =='OS8': n_OS8= n_OS8+1
            elif categoria =='OS9': n_OS9= n_OS9+1
            elif categoria =='OS10': n_OS10= n_OS10+1
            elif categoria =='OS11': n_OS11= n_OS11+1
            elif categoria =='OS12-A': n_OS12A= n_OS12A+1
            elif categoria =='OS12-B': n_OS12B= n_OS12B+1
            elif categoria =='OS13': n_OS13= n_OS13+1
            elif categoria =='OS14': n_OS14= n_OS14+1
            elif categoria =='OS15': n_OS15= n_OS15+1
            elif categoria =='OS16': n_OS16= n_OS16+1
            elif categoria =='OS17': n_OS17= n_OS17+1
            elif categoria =='OS18-A': n_OS18A= n_OS18A+1
            elif categoria =='OS18-B': n_OS18B= n_OS18B+1
            elif categoria =='OS19': n_OS19= n_OS19+1
            elif categoria =='OS20-A': n_OS20A= n_OS20A+1
            elif categoria =='OS20-B': n_OS20B= n_OS20B+1
            elif categoria =='OS21': n_OS21= n_OS21+1
            elif categoria =='OS22': n_OS22= n_OS22+1
            elif categoria =='OS23': n_OS23= n_OS23+1
            elif categoria =='OS24': n_OS24= n_OS24+1
            elif categoria =='OS25': n_OS25= n_OS25+1
            elif categoria =='OS26': n_OS26= n_OS26+1
            elif categoria =='OS27': n_OS27= n_OS27+1
            elif categoria =='OS28': n_OS28= n_OS28+1
            elif categoria =='OS29': n_OS29= n_OS29+1
            elif categoria =='OS30': n_OS30= n_OS30+1
            elif categoria =='OS31': n_OS31= n_OS31+1
            elif categoria =='OS32': n_OS32= n_OS32+1
            elif categoria =='OS33': n_OS33= n_OS33+1
            elif categoria =='OS34': n_OS34= n_OS34+1
            elif categoria =='OS35': n_OS35= n_OS35+1

    lista = []
    lista.append(('OG1',n_OG1))
    lista.append(('OG2',n_OG2))
    lista.append(('OG3',n_OG3))
    lista.append(('OG4',n_OG4))
    lista.append(('OG5',n_OG5))
    lista.append(('OG6',n_OG6))
    lista.append(('OG7',n_OG7))
    lista.append(('OG8',n_OG8))
    lista.append(('OG9',n_OG9))
    lista.append(('OG10',n_OG10))
    lista.append(('OG11',n_OG11))
    lista.append(('OG12',n_OG12))
    lista.append(('OG13',n_OG13))
    lista.append(('OS1',n_OS1))
    lista.append(('OS2A',n_OS2A))
    lista.append(('OS2B',n_OS2B))
    lista.append(('OS3',n_OS3))
    lista.append(('OS4',n_OS4))
    lista.append(('OS5',n_OS5))
    lista.append(('OS6',n_OS6))
    lista.append(('OS7',n_OS7))
    lista.append(('OS8',n_OS8))
    lista.append(('OS9',n_OS9))
    lista.append(('OS10',n_OS10))
    lista.append(('OS11',n_OS11))
    lista.append(('OS12A',n_OS12A))
    lista.append(('OS12B',n_OS12B))
    lista.append(('OS13',n_OS13))
    lista.append(('OS14',n_OS14))
    lista.append(('OS15',n_OS15))
    lista.append(('OS16',n_OS16))
    lista.append(('OS17',n_OS17))
    lista.append(('OS18A',n_OS18A))
    lista.append(('OS18B',n_OS18B))
    lista.append(('OS19',n_OS19))
    lista.append(('OS20A',n_OS20A))
    lista.append(('OS20B',n_OS20B))
    lista.append(('OS21',n_OS21))
    lista.append(('OS22',n_OS22))
    lista.append(('OS23',n_OS23))
    lista.append(('OS24',n_OS24))
    lista.append(('OS25',n_OS25))
    lista.append(('OS26',n_OS26))
    lista.append(('OS27',n_OS27))
    lista.append(('OS28',n_OS28))
    lista.append(('OS29',n_OS29))
    lista.append(('OS30',n_OS30))
    lista.append(('OS31',n_OS31))
    lista.append(('OS32',n_OS32))
    lista.append(('OS33',n_OS33))
    lista.append(('OS34',n_OS34))
    lista.append(('OS35',n_OS35))

    ordinata  = sorted (lista , key=lambda lista  : lista[1],reverse=True)

    return   ordinata


def converti_data (data_py):
        data_ita = data_py.strftime('%d-%m-%Y')
        sitrng = str(data_ita)
        return data_ita

def get_session_info():
	
			uid = "web";
			access_type= "no";
			info = "uid="+uid+"&pwd="+access_type;			
			return info;
account = get_session_info()

def function_config():
			 name_server = "10*.119*.128*.95";
			 name_project = "SISk*_Extranet";
			 directory = "Extranet";
			 url_din = ""+name_server+"."+name_project+".0_&shared=*-1.*-1.0.0.0&ftb=0.422541B24E28B69DC5DF858B20E67091.*0.8.0.0-8.18_268453447.*-1.1.*0&fb=0.422541B24E28B69DC5DF858B20E67091."+directory+".8.0.0-8.768.769.774.770.773.772.775.55.256.10.257.776.777_268453447.*-1.1.*0";
			 return url_din;
part_url = function_config()
def get_server():
			server_ip = "portaletrasparenza.avcp.it";
			return server_ip;

ip = get_server()

def data_per_db(data):
    data=data.replace(u'\xa0', '')
    if data:               
        d = datetime.strptime(data, '%d/%m/%Y')
        day_string = d.strftime('%Y-%m-%d')
        
    else:
        day_string = "1900-01-01"
    return day_string
        


        

def prendi_provincia_regione2(comun):
    try:
        sql_com = 'SELECT * FROM gare.comuni where nome = "'+comun+'"'
        cursore1 = conn.cursor()
        cursore1.execute(sql_com)
        id_prov  = cursore1.fetchall()[0][2]   
        sql_prov   = 'SELECT * FROM gare.province where id = '+ str(id_prov)
        cursore1.execute(sql_prov)
        prov =  cursore1.fetchall()

        provincia = prov[0][1]
        sql_sigle = 'SELECT * FROM gare.province_sigle where nomeprovincia = "'+provincia+'"'
        cursore1.execute(sql_sigle)
        
        try:
            sigla_prov   =  cursore1.fetchall()[0][3].replace('\xe9','')
        except:
            sigla_prov =  provincia.replace('\xe9','')
        
        id_regione = prov[0][2]
        sql_reg   = 'SELECT * FROM gare.regioni where id = '+ str(id_regione)
        cursore1.execute(sql_reg)
        regione  =  cursore1.fetchall()[0][1].replace('\xe9','')
        
    except:
        sigla_prov = ''
        regione = ''
    return (removeNonAscii(sigla_prov),removeNonAscii(regione))


def get_lista_cig_esistenti():
    lista_esistenti = []
    sql_select_cig_esistenti = 'SELECT CIG FROM gare.esiti_veri;'
    cursore1 = conn.cursor()
    cursore1.execute(sql_select_cig_esistenti)
    cig_esistenti = cursore1.fetchall()
    for cig_singolo in cig_esistenti:
        lista_esistenti.append(cig_singolo[0])
    return lista_esistenti


def prendi_import(imp):
    #imp = '€ 40.810.000'
    impo= imp[1:]
    impor = impo.replace('.','').replace(' ','')
    return impor

def estrai_OG(cat):
    grafo_cat = {
    'Edifici civili e industriali':'OG1',
    'Restauro e manutenzione dei beni immobili sottoposti a tutela':'OG2',
    'Strade, autostrade, ponti, viadotti, ferrovie, metropolitane':'OG3',
    'Opere d’arte nel sottosuolo':'OG4',
    'Dighe':'OG5',
    'Acquedotti, gasdotti , oleodotti, opere di irrigazione e di evacuazione':'OG6',
    'Acquedotti, gasdotti, oleodotti, opere di irrigazione e di evacuazione':'OG6',
    'Opere marittime e lavori di dragaggio':'OG7',
    'Opere fluviali, di difesa, di sistemazione idraulica e di bonifica':'OG8',
    'Impianti per la produzione di energia elettrica':'OG9',
    'Impianti per la trasformazione alta/media tensione e e per la distribuzione di energia elettrica in corrente alternata e continua ed impianti di pubblica illuminazione':'OG10',
    'Impianti tecnologici':'OG11',
    'Opere ed impianti di bonifica e protezione ambientale':'OG12',
    'Opere di ingegneria naturalistica':'OG13',
    'Lavori in terra':'OS1',
    'Superfici decorate di beni immobili del patrimonio culturale e beni culturali mobili di interesse storico, artistico, archeologico ed etnoantropologico':'OS2-A',
    'Beni culturali mobili di interesse archivistico e librario':'OS2-B',
    'Impianti idrico-sanitario, cucine, lavanderie':'OS3',
    'Impianti elettromeccanici trasportatori':'OS4',
    'Impianti pneumatici e antintrusione':'OS5',
    'Finiture di opere generali in materiali lignei, plastici, metallici e vetrosi':'OS6',
    'Finiture di opere generali di natura edile':'OS7',
    'Opere di impermeabilizzazione':'OS8',
    'Impianti per la segnaletica luminosa e la sicurezza del traffico':'OS9',
    'Segnaletica stradale non luminosa':'OS10',
    'Apparecchiature strutturali speciali':'OS11',
    'Barriere stradali di sicurezza':'OS12-A',
    'Barriere paramassi, fermaneve e simili':'OS12-B',
    'Strutture prefabbricate in cemento armato':'OS13',
    'Impianti di smaltimento e recupero dei rifiuti':'OS14',
    'Pulizie di acque marine, lacustri, fluviali':'OS15',
    'Impianti per centrali di produzione energia elettrica':'OS16',
    'Linee telefoniche ed impianti di telefonia':'OS17',
    'Componenti strutturali in acciaio':'OS18-A',
    'Componenti per facciate continue':'OS18-B',
    'Impianti di reti di telecomunicazione e di trasmissione dati':'OS19',
    'Rilevamenti topografici':'OS20-A',
    'Indagini geognostiche':'OS20-B',
    'Opere strutturali speciali':'OS21',
    'Impianti di potabilizzazione e depurazione':'OS22',
    'Demolizione di opere':'OS23',
    'Verde e arredo urbano':'OS24',
    'Scavi archeologici':'OS25',
    'Pavimentazioni e sovrastrutture speciali':'OS26',
    'Impianti per la trazione elettrica':'OS27',
    'Impianti termici e di condizionamento':'OS28',
    'Armamento ferroviario':'OS29',
    'Impianti interni elettrici, telefonici, radiotelefonici e televisivi':'OS30',
    'Impianti per la mobilità sospesa':'OS31',
    'Strutture in legno':'OS32',
    'Coperture speciali':'OS33',
    'Sistemi antirumore per infrastrutture di mobilità':'OS34',
    'Interventi a basso impatto ambientale':'OS35',

    }


    cat = cat.rstrip().lstrip()
    if cat.capitalize() in grafo_cat.keys():

        return grafo_cat.get(cat.capitalize())
    else:
        return ""

                
def insert_esiti(cig,oggetto,tipologia,procedura,ente,citta,provincia,regione,importo,data_pubblicazione,data_scadenza,cat_prev,cat_scor1,cat_scor2,cat_scor3,cat_scor4,cat_scor5,cpv,bando_url,bando_pdf,ribasso,criterio_agg,data_agg,importo_agg,nr_offerte,aggiudicatario,scaduto,data_inserimento, linkAVCP):
                        cursore = conn.cursor()
                        sql = 'INSERT INTO gare.esiti_veri (cig,oggetto,tipologia,procedura,ente,citta,provincia,regione,importo,data_pubblicazione,data_scadenza,cat_prev,cat_scor1,cat_scor2,cat_scor3,cat_scor4,cat_scor5,cpv,bando_url,bando_pdf,ribasso,criterio_agg,data_agg,importo_agg,nr_offerte,aggiudicatario,scaduto,data_inserimento, linkAVCP)   VALUES ("%s","%s", "%s","%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s", "%s","%s","%s","%s","%s","%s","%s","%s")'% (cig,                                                
                                                                                              oggetto,
                                                                                              tipologia,
                                                                                              procedura,                                                                                                                                           
                                                                                              ente,
                                                                                              citta,
                                                                                              provincia,
                                                                                              regione,
                                                                                              importo,
                                                                                              data_pubblicazione,
                                                                                              data_scadenza,
                                                                                              cat_prev,
                                                                                              cat_scor1,
                                                                                              cat_scor2,
                                                                                              cat_scor3,
                                                                                              cat_scor4,
                                                                                              cat_scor5,
                                                                                              cpv,
                                                                                              bando_url,
                                                                                              bando_pdf,
                                                                                              ribasso,
                                                                                              criterio_agg,
                                                                                              data_agg,
                                                                                              importo_agg,
                                                                                              nr_offerte,
                                                                                              aggiudicatario,  
                                                                                              scaduto,
                                                                                              data_inserimento,
                                                                                              linkAVCP                                                                                                                                                                                                                                                                                                                                                                                                                            
                                                                                              )
                        print sql
                                                                                           
                        cursore.execute(sql)
                        conn.commit()



#ecco
def prendi_indice():
    sql_ultimo = 'SELECT * FROM (SELECT T1.*, @rownum := @rownum + 1 AS rn FROM gare.esiti1 T1, (SELECT @rownum := 0) T2) T3 ORDER BY rn DESC LIMIT 1'
    cursore1 = conn.cursor()
    cursore1.execute(sql_ultimo)
    bandi = cursore1.fetchall()
    ultimo_record =  bandi[0][0]
    print ultimo_record
    try:
        indice = int(cigs.index(ultimo_record+'\n'))
    except:
        indice = 0
    return indice

headers = {
    'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.13) Gecko/2009073022 Firefox/3.0.13',
    'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml; q=0.9,*/*; q=0.8',
    'Content-Type': 'application/x-www-form-urlencoded'
}


formFields = (
)


def get_lista_cig_esistenti():
    lista_esistenti = []
    sql_select_cig_esistenti = 'SELECT CIG FROM gare.esiti_veri;'
    cursore1 = conn.cursor()
    cursore1.execute(sql_select_cig_esistenti)
    cig_esistenti = cursore1.fetchall()
    for cig_singolo in cig_esistenti:
        lista_esistenti.append(cig_singolo[0])
    return lista_esistenti

percorso = os.getcwd() 
path= percorso
#path= "C:/Users/Gianmichele/Google Drive/miglior_bandi/date/"
fil = "/esiti_veri.txt"


f = open(path+fil,"r")
cigs = f.readlines()
cigs = [item.replace("\n"," ").replace("\r"," ").replace(' ', '') for item in cigs]
cigs = list(set(cigs))
f.close()



lista_cigs_esistenti = get_lista_cig_esistenti()

print len(cigs)
print len(lista_cigs_esistenti)

lista_senza_duplicati = [item for item in cigs if item not in lista_cigs_esistenti]
print len(lista_senza_duplicati)






