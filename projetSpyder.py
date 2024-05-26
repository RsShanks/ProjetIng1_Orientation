#!/usr/bin/env python
# coding: utf-8

# In[186]:


import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
import random
import tkinter as tk
from tkinter import messagebox
import csv
import pymysql
import sys
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk



global autorisation
autorisation = False
global graphe
graphe = False


# In[187]:


nomBDD = 'projet'
mdpBDD = 'cytech0001'
speGI = {"IA":10,"CS":10,"IE":10,"VC":7}
speGMI = {"DS":10,"HPDA":10,"3D":10,"Fintech":9}
speGMF = {"IF":12,"MathF":12,"Act":14}
listeSpeGMI = [s[0] for s in list(speGMI.items())]#"data science","High Performance Data Analytics","Data du Developpement Durable","Finances et Technologies"
listeSpeGMF = [s[0] for s in list(speGMF.items())]#"Ingenierie Financiere","Mathematiques pour la Finance","Actuariat"
listeSpeGI = [s[0] for s in list(speGI.items())]#"IA","Cybersecurite","Informarique embarquee","Visual Computing"


# In[188]:


def dropBDD():
    requetes = [
        "DROP DATABASE IF EXISTS projet;",
        "CREATE DATABASE projet;",
        f"USE {nomBDD};",
        "DROP TABLE IF EXISTS eleves;",
        """
        CREATE TABLE IF NOT EXISTS eleves(
            mail VARCHAR(255),
            nom VARCHAR(255) NOT NULL,
            prenom VARCHAR(255) NOT NULL,
            filiere VARCHAR(255) NOT NULL,
            note FLOAT,
            affect BOOLEAN,
            specialite TEXT,
            id INT PRIMARY KEY,
            age INT,
            preferences VARCHAR(255)
        );
        """,
        """
        INSERT INTO eleves(nom,prenom,mail,id,age,filiere,note) VALUES 
('Lefort','Pierre','lefortpie@cy-tech.fr',5865,25,'GI',19),
('Vincent','Alice','vincentali@cy-tech.fr',8064,23,'GMI',18),
('Durand','Camille','durandcam@cy-tech.fr',2535,22,'GMF',15),
('Bertrand','Elodie','bertrandelo@cy-tech.fr',7894,24,'GMF',14),
('Laurent','Alexandre','laurentale@cy-tech.fr',970,23,'GI',14),
('Henry','Thomas','henrytho@cy-tech.fr',4702,24,'GMI',14),
('Garcia','Nicolas','garcianic@cy-tech.fr',8607,22,'GMI',14),
('Roux','Nicolas','rouxnic@cy-tech.fr',3487,22,'GMI',14),
('Dupont','Emma','dupontemm@cy-tech.fr',78,23,'GI',13),
('Lefort','Laura','lefortlau@cy-tech.fr',3511,20,'GMF',13),
('Henry','Jean','henryjea@cy-tech.fr',3143,20,'GMF',12),
('Lefevre','Maxime','lefevremax@cy-tech.fr',8170,21,'GI',12),
('Durand','Alice','durandali@cy-tech.fr',5088,25,'GMI',11),
('Moreau','Pierre','moreaupie@cy-tech.fr',2634,22,'GMF',10),
('Michel','Antoine','michelant@cy-tech.fr',5709,20,'GMF',8),
('Martin','Elodie','martinelo@cy-tech.fr',9778,18,'GMI',8),
('Simon','Marie','simonmar@cy-tech.fr',3802,20,'GMI',8),
('Dupont','Gabriel','dupontgab@cy-tech.fr',6038,19,'GMI',7),
('Henry','Alice','henryali@cy-tech.fr',4643,23,'GMF',5),
('Moreau','Laura','moreaulau@cy-tech.fr',7899,20,'GI',3),
('Lefevre','Hugo','lefevhug@cy-tech.fr',1234,21,'GI',16.5),
('Petit','Chloe','petitchl@cy-tech.fr',2345,22,'GMI',17.2),
('Robert','Lucas','roberluc@cy-tech.fr',3456,23,'GMF',14.8),
('Richard','Sophie','richasop@cy-tech.fr',4567,24,'GI',18.9),
('Dubois','Arthur','duboiart@cy-tech.fr',5678,25,'GMI',15.6),
('Fontaine','Manon','fontaman@cy-tech.fr',6789,26,'GMF',16.4),
('Blanc','Louis','blanclou@cy-tech.fr',7890,27,'GI',17.1),
('Guerin','Jules','guerijul@cy-tech.fr',8901,28,'GMI',13.7),
('Boyer','Lina','boyerlin@cy-tech.fr',9012,29,'GMF',19.3),
('Garnier','Tom','garntom@cy-tech.fr',1123,30,'GI',12.5),
('Chevalier','Zoe','chevzoe@cy-tech.fr',2234,18,'GMI',14.9),
('Clement','Leo','clemleo@cy-tech.fr',3345,19,'GMF',16.2),
('Lambert','Mila','lambmil@cy-tech.fr',4456,20,'GI',15.4),
('Bonnet','Adam','bonnadam@cy-tech.fr',5567,21,'GMI',18.2),
('Francois','Eva','franeva@cy-tech.fr',6678,22,'GMF',11.7),
('Martinez','Hugo','marthugo@cy-tech.fr',7789,23,'GI',13.9),
('Lefort','Chloe','lefortchl@cy-tech.fr',8890,24,'GMI',17.6),
('Vincent','Lucas','vincenluc@cy-tech.fr',9901,25,'GMF',12.8),
('Durand','Sophie','duransop@cy-tech.fr',1012,26,'GI',14.5),
('Bertrand','Arthur','bertarth@cy-tech.fr',2023,27,'GMI',18.3),
('Laurent','Manon','laurmano@cy-tech.fr',3034,28,'GMF',13.1),
('Henry','Louis','henrylou@cy-tech.fr',4045,29,'GI',16.8),
('Garcia','Jules','garcijul@cy-tech.fr',5056,30,'GMI',17.9),
('Roux','Lina','rouxlina@cy-tech.fr',6067,18,'GMF',14.3),
('Dupont','Tom','duponttom@cy-tech.fr',7078,19,'GI',15.2),
('Lefevre','Zoe','lefevzoe@cy-tech.fr',8089,20,'GMI',18.1),
('Moreau','Leo','morealeo@cy-tech.fr',9090,21,'GMF',12.6),
('Petit','Mila','petitmila@cy-tech.fr',1101,22,'GI',11.9),
('Robert','Eva','robertev@cy-tech.fr',1202,23,'GMI',13.5),
('Richard','Adam','richadam@cy-tech.fr',1303,24,'GMF',17.4),
('Dubois','Leo','duboileo@cy-tech.fr',1404,25,'GI',16.3),
('Fontaine','Zoe','fontazoe@cy-tech.fr',1505,26,'GMI',12.7),
('Blanc','Tom','blantom@cy-tech.fr',1606,27,'GMF',15.8),
('Guerin','Louis','guerilou@cy-tech.fr',1707,28,'GI',18.4),
('Boyer','Manon','boyerman@cy-tech.fr',1808,29,'GMI',17.1),
('Garnier','Lucas','garnluc@cy-tech.fr',1909,30,'GMF',14.6),
('Chevalier','Arthur','chevarth@cy-tech.fr',2010,18,'GI',13.9),
('Clement','Chloe','clemchl@cy-tech.fr',2111,19,'GMI',15.3),
('Lambert','Hugo','lamberthug@cy-tech.fr',2212,20,'GMF',16.7),
('Bonnet','Jules','bonnjul@cy-tech.fr',2313,21,'GI',14.2),
('Francois','Sophie','fransop@cy-tech.fr',2414,22,'GMI',19.0),
('Martinez','Lina','martlin@cy-tech.fr',2515,23,'GMF',13.4),
('Lefort','Leo','lefortleo@cy-tech.fr',2616,24,'GI',12.1),
('Vincent','Mila','vincenmila@cy-tech.fr',2717,25,'GMI',11.8),
('Durand','Eva','duranva@cy-tech.fr',2818,26,'GMF',16.5),
('Bertrand','Tom','bertom@cy-tech.fr',2919,27,'GI',18.2),
('Laurent','Louis','laurlou@cy-tech.fr',3020,28,'GMI',13.9),
('Henry','Manon','henryman@cy-tech.fr',3121,29,'GMF',14.8),
('Garcia','Adam','garciaadam@cy-tech.fr',3222,30,'GI',15.7),
('Roux','Lucas','rouxluc@cy-tech.fr',3323,18,'GMI',17.6),
('Dupont','Zoe','duponzoe@cy-tech.fr',3424,19,'GMF',15.6),
('Lefevre','Chloe','lefevchlo@cy-tech.fr',3525,20,'GI',16.3),
('Moreau','Leo','moreauleo@cy-tech.fr',3626,21,'GMI',17.2),
('Petit','Mila','petitmila@cy-tech.fr',3727,22,'GMF',18.9),
('Robert','Hugo','roberhug@cy-tech.fr',3828,23,'GI',14.7),
('Richard','Chloe','richachl@cy-tech.fr',3929,24,'GMI',15.4),
('Dubois','Lucas','duboluc@cy-tech.fr',4030,25,'GMF',16.5),
('Fontaine','Sophie','fontasop@cy-tech.fr',4131,26,'GI',17.8),
('Blanc','Arthur','blancthu@cy-tech.fr',4232,27,'GMI',13.6),
('Guerin','Manon','gueriman@cy-tech.fr',4333,28,'GMF',14.5),
('Boyer','Louis','boyerlou@cy-tech.fr',4434,29,'GI',18.2),
('Garnier','Jules','garnijul@cy-tech.fr',4535,30,'GMI',19.4),
('Chevalier','Lina','chevalin@cy-tech.fr',4636,18,'GMF',16.7),
('Clement','Tom','clemtom@cy-tech.fr',4737,19,'GI',15.8),
('Lambert','Zoe','lamberzoe@cy-tech.fr',4838,20,'GMI',14.9),
('Bonnet','Leo','bonneleo@cy-tech.fr',4939,21,'GMF',17.3),
('Francois','Mila','franmila@cy-tech.fr',5040,22,'GI',16.4),
('Martinez','Hugo','martihug@cy-tech.fr',5141,23,'GMI',12.7),
('Lefort','Chloe','leforchlo@cy-tech.fr',5242,24,'GMF',13.5),
('Vincent','Lucas','vincluc@cy-tech.fr',5343,25,'GI',14.8),
('Durand','Sophie','durasop@cy-tech.fr',5444,26,'GMI',18.7),
('Bertrand','Arthur','berthar@cy-tech.fr',5545,27,'GMF',19.2),
('Laurent','Manon','laurnan@cy-tech.fr',5646,28,'GI',16.1),
('Henry','Louis','henlou@cy-tech.fr',5747,29,'GMI',15.3),
('Garcia','Jules','garjul@cy-tech.fr',5848,30,'GMF',17.9),
('Roux','Lina','rouxlina@cy-tech.fr',5949,18,'GI',13.8),
('Dupont','Tom','duptom@cy-tech.fr',6050,19,'GMI',16.9),
('Lefevre','Zoe','lefevzoe@cy-tech.fr',6151,20,'GMF',17.1),
('Moreau','Leo','moreleo@cy-tech.fr',6252,21,'GI',14.2),
('Petit','Mila','petmila@cy-tech.fr',6353,22,'GMI',13.4),
('Robert','Eva','robeva@cy-tech.fr',6454,23,'GMF',15.6),
('Richard','Adam','richadam@cy-tech.fr',6555,24,'GI',17.2),
('Dubois','Leo','dubleo@cy-tech.fr',6656,25,'GMI',18.3),
('Fontaine','Zoe','fonzoe@cy-tech.fr',6757,26,'GMF',19.5),
('Blanc','Tom','blantom@cy-tech.fr',6858,27,'GI',14.9),
('Guerin','Louis','guerilou@cy-tech.fr',6959,28,'GMI',15.7),
('Boyer','Manon','boyemanon@cy-tech.fr',7060,29,'GMF',16.8),
('Garnier','Lucas','garnluc@cy-tech.fr',7161,30,'GI',17.9),
('Chevalier','Arthur','chevarthur@cy-tech.fr',7262,18,'GMI',18.4),
('Clement','Chloe','clechloe@cy-tech.fr',7363,19,'GMF',12.5),
('Lambert','Hugo','lamhugo@cy-tech.fr',7464,20,'GI',14.6),
('Bonnet','Jules','bonnjules@cy-tech.fr',7565,21,'GMI',13.7),
('Francois','Sophie','fransophie@cy-tech.fr',7666,22,'GMF',17.3),
('Martinez','Lina','martlina@cy-tech.fr',7767,23,'GI',18.2);
        """
    ]
    
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = mdpBDD,
        db = nomBDD,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        with conn.cursor() as cursor:
            for requete in requetes:
                cursor.execute(requete)
        conn.commit()  # Assurez-vous de valider les changements dans la base de données
    finally:
        conn.close()




# In[189]:


#dropBDD()


# In[190]:


def trouverEtudiantSQL(mail):
    requete = "SELECT * FROM eleves WHERE mail = '"+mail+"';" 
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = mdpBDD,
        db = nomBDD,
        cursorclass = pymysql.cursors.DictCursor
    )
    try : 
        with conn.cursor() as cursor :
            cursor.execute(requete)
            rows = cursor.fetchall()
    finally :
        conn.close()
    return rows[0]


# In[191]:


# gene id de connexkion

def initDonnesConnexion():
    listeCO = {}
    chemin_fichier = 'idConnexion.csv'

    # Lecture des données depuis le fichier CSV
    with open(chemin_fichier, mode='r', newline='') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        # Utilisation d'une boucle pour parcourir chaque ligne du fichier CSV
        for ligne in lecteur_csv:
            mail = ligne[0]
            password = ligne[1]
            type = ligne[2]
            info = ''
            y = {"password":password,"type":type,"info":info}
            listeCO[mail] = y
        
    return listeCO

listeCO = initDonnesConnexion()


# In[192]:


def ecrirePrefSQL(pref,id):
    
    prefSTR = ",".join(pref)
    requete = "UPDATE eleves SET preferences = '"+prefSTR+"' WHERE id="+str(id)+";"
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = mdpBDD,
        db = nomBDD,
        cursorclass = pymysql.cursors.DictCursor
    )
    try : 
        with conn.cursor() as cursor :
            cursor.execute(requete)
            rows = cursor.fetchall()
            conn.commit()

    finally :
        conn.close()

def ecrireAffSQL(eleves):
    #permet de regrouper toutes les affectations en une seule
    updates = [(nouvelle_specialite, nom) for nom, nouvelle_specialite in eleves.items()]

    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = mdpBDD,
        db = nomBDD,
        cursorclass = pymysql.cursors.DictCursor
    )

    try :
        with conn.cursor() as cursor :
            # Exécution de la requête de mise à jour
            cursor.executemany("UPDATE eleves SET specialite = %s ,affect = TRUE WHERE id = %s", updates)
            # Valider les modifications
            conn.commit()
    finally :
        conn.close()


# In[193]:


def initDonnesEtudiantsSQL():
    listeETU = []
    requete = "SELECT id,filiere FROM eleves WHERE isnull(preferences)=1 ORDER BY note DESC" 
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = mdpBDD,
        db = nomBDD,
        cursorclass = pymysql.cursors.DictCursor
    )
    try : 
        with conn.cursor() as cursor :
            cursor.execute(requete)
            rows = cursor.fetchall()
            
    finally :
        conn.close()
    return rows

def listeEtuCV(): #liste des etudiants qui ont validé leur choix
    requete = "SELECT nom, prenom, mail FROM eleves WHERE isnull(preferences)=0"
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = mdpBDD,
        db = nomBDD,
        cursorclass = pymysql.cursors.DictCursor
    )
    try : 
        with conn.cursor() as cursor :
            cursor.execute(requete)
            rows = cursor.fetchall()
    finally :
        conn.close()
    return rows

def listeEtuCNV(): #liste des etudiants qui n'ont pas validé leur choix
    requete = "SELECT nom, prenom, mail FROM eleves WHERE isnull(preferences)=1"
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'cytech0001',
        db = nomBDD,
        cursorclass = pymysql.cursors.DictCursor
    )
    try : 
        with conn.cursor() as cursor :
            cursor.execute(requete)
            rows = cursor.fetchall()
    finally :
        conn.close()
    return rows


def simulation_pref_tous_etu():
    liste_etu = initDonnesEtudiantsSQL()
    for e in liste_etu:
        if e['filiere']=='GI':
            pref = random.sample(listeSpeGI,len(listeSpeGI))
            ecrirePrefSQL(pref, e['id'])
        elif e['filiere']=='GMI':
            pref = random.sample(listeSpeGMI,len(listeSpeGMI))
            ecrirePrefSQL(pref, e['id'])
        elif e['filiere']=='GMF':
            pref = random.sample(listeSpeGMF,len(listeSpeGMF))
            ecrirePrefSQL(pref, e['id'])


# In[194]:


####  ICI SE TROUVE TOUTES LES FONCTIONS NECESSAIRES A L'AFFECTATION

def GMF(option,nb_finance,nb_actuariat,nb_manip,stat_gen,stat_GMF):
    i = 0
    while i < 3 :
        if option[i] == "IF" and nb_finance < speGMF["IF"] : 
            nb_finance+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GMF = np.append(stat_GMF,i+1)
            return "IF",nb_finance,nb_actuariat,nb_manip,stat_gen,stat_GMF
        elif option[i] == "Act" and nb_actuariat < speGMF["Act"] :
            nb_actuariat+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GMF = np.append(stat_GMF,i+1)
            return "Act",nb_finance,nb_actuariat,nb_manip,stat_gen,stat_GMF
        elif option[i] == "MathF" and nb_manip < speGMF["MathF"] :
            nb_manip+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GMF = np.append(stat_GMF,i+1)
            return "MathF",nb_finance,nb_actuariat,nb_manip,stat_gen,stat_GMF
        
        i=i+1

def GI(option,nb_cyber,nb_ia,nb_business,nb_dev,stat_gen,stat_GI):
    i = 0
    while i < 4 :
        if option[i] == "CS" and nb_cyber < speGI["CS"] : 
            nb_cyber+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GI = np.append(stat_GI,i+1)
            return "CS",nb_cyber,nb_ia,nb_business,nb_dev,stat_gen,stat_GI
        elif option[i] == "IA" and nb_ia < speGI["IA"] :
            nb_ia+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GI = np.append(stat_GI,i+1)
            return "IA",nb_cyber,nb_ia,nb_business,nb_dev,stat_gen,stat_GI
        elif option[i] == "IE" and nb_business < speGI["IE"] :
            nb_business+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GI = np.append(stat_GI,i+1)
            return "IE",nb_cyber,nb_ia,nb_business,nb_dev,stat_gen,stat_GI
        elif option[i] == "VC" and nb_dev < speGI["VC"] :
            nb_dev+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GI = np.append(stat_GI,i+1)
            return "VC",nb_cyber,nb_ia,nb_business,nb_dev,stat_gen,stat_GI
        
        i=i+1

def GMI(option,nb_data,nb_high,nb_3D,nb_tech,stat_gen,stat_GMI):
    i = 0
    while i < 4 :
        if option[i] == "DS" and nb_data < speGMI["DS"] :  
            nb_data+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GMI = np.append(stat_GMI,i+1)
            return "DS",nb_data,nb_high,nb_3D,nb_tech,stat_gen,stat_GMI
        elif option[i] == "HPDA" and nb_high < speGMI["HPDA"] :
            nb_high+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GMI = np.append(stat_GMI,i+1)
            return "HPDA",nb_data,nb_high,nb_3D,nb_tech,stat_gen,stat_GMI
        elif option[i] == "Fintech" and nb_tech < speGMI["Fintech"] :
            nb_tech+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GMI = np.append(stat_GMI,i+1)
            return "Fintech",nb_data,nb_high,nb_3D,nb_tech,stat_gen,stat_GMI
        elif option[i] == "3D" and nb_3D< speGMI["3D"]:
            nb_3D+=1
            stat_gen=np.append(stat_gen,i+1)
            stat_GMI = np.append(stat_GMI,i+1)
            return "3D",nb_data,nb_high,nb_3D,nb_tech,stat_gen,stat_GMI
        
        i=i+1

def voeux_pref(voeux) : 
    unique_values, counts = np.unique(voeux, return_counts=True)
    stats = np.concatenate((unique_values[:,np.newaxis],counts[:,np.newaxis]),axis=1)
    fg, ax = plt.subplots()
    ax.set_title("Choix le plus prisé")
    ax.hist(voeux,bins=np.arange(len(set(voeux))+1)-0.5,edgecolor='black', linewidth=2)

    #plt.yticks(np.arange(0, plt.gca().get_ylim()[1]+1, 1))
    return fg, ax
    


def voeux_obtenue(voeux):
    unique_values, counts = np.unique(voeux, return_counts=True)
    stats = np.concatenate((unique_values[:,np.newaxis],counts[:,np.newaxis]),axis=1)
    total = sum(counts)
    labels=[i for i in unique_values]
    labels[0] = "Choix 1"
    if 2 not in unique_values :
        labels.append("choix 2")
        counts= np.append(counts,0)
    else :
        for i,j in enumerate(unique_values) :
            if j == 2 :
                labels[i]="choix 2"


    if 3 not in unique_values :
        labels.append("choix 3")
        counts= np.append(counts,0)
    else :
        for i,j in enumerate(unique_values) :
            if j == 3 :
                labels[i]="choix 3"

    if 4 not in unique_values:
        labels.append("choix 4")
        counts= np.append(counts,0)
    else :
        for i,j in enumerate(unique_values) :
            if j == 4 :
                labels[i]="choix 4"

    explode = [0, 0, 0, 0]
    explode[np.argmax(counts)] = 0.1
    fig, ax = plt.subplots()
    ax.pie(counts, explode=explode, labels=labels,autopct='%1.1f%%',radius = 1.4, shadow=True, startangle=90)
    text=[]
    for i in range(len(unique_values)):
        text.append(str((counts[i]/total)*100) + "% des élèves ont eu leur " + labels[i] + "\n")
    return fig,ax,text





def initEleve():
    listeETU = []
    requete = "SELECT id,preferences FROM eleves ORDER BY note DESC" 
    conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = mdpBDD,
        db = nomBDD,
        cursorclass = pymysql.cursors.DictCursor
    )
    try : 
        with conn.cursor() as cursor :
            cursor.execute(requete)
            rows = cursor.fetchall()
    finally :
        conn.close()

   ## listeETU = {r['id']:r['preferences'].split(',') for r in rows}
    listeETU = {}
    voeux = np.array([])
    for eleve in rows :
        specialite = {}
        specialites = eleve['preferences'].split(",")
        voeux = np.append(voeux,specialites[0])
        for i,j in enumerate(specialites) :
            specialite[i]=j
        listeETU[eleve['id']] = specialite
    
    return listeETU,voeux

def affectation():
    
    nb_data = 0
    nb_high = 0
    nb_tech = 0
    nb_3D = 0
    nb_manip=0
    nb_actuariat = 0
    nb_finance = 0
    nb_dev=0
    nb_business=0
    nb_ia=0
    nb_cyber=0

    eleves,voeux = initEleve()
    stat_gen = np.array([])
    stat_GI = np.array([])
    stat_GMI = np.array([])
    stat_GMF = np.array([])
    for eleve in eleves :
        if eleves[eleve][0] in listeSpeGMI :
            eleves[eleve],nb_data,nb_high,nb_3D,nb_tech,stat_gen,stat_GMI = GMI(eleves[eleve],nb_data,nb_high,nb_3D,nb_tech,stat_gen,stat_GMI)
            
        elif eleves[eleve][0] in listeSpeGMF :
            eleves[eleve],nb_finance,nb_actuariat,nb_manip,stat_gen,stat_GMF = GMF(eleves[eleve],nb_finance,nb_actuariat,nb_manip,stat_gen,stat_GMF)
            
        elif eleves[eleve][0] in listeSpeGI :
            eleves[eleve],nb_cyber,nb_ia,nb_business,nb_dev,stat_gen,stat_GI = GI(eleves[eleve],nb_cyber,nb_ia,nb_business,nb_dev,stat_gen,stat_GI)
            
        else:
            eleves[eleve] = "Redoublement"
            
    ecrireAffSQL(eleves)
    fig1,ax1 = voeux_pref(voeux)
    fig2,ax2,text2 = voeux_obtenue(stat_gen)
    ax2.set_title("Stats Générales")
    ax2.title.set_position([0, 0.5])

    fig3,ax3,text3 = voeux_obtenue(stat_GI)
    ax3.set_title("Stats GI")
    ax3.title.set_position([0, 0.5])

    fig4,ax4,text4 = voeux_obtenue(stat_GMI)
    ax4.set_title("Stats GMI")
    ax4.title.set_position([0, 0.5])

    fig5,ax5,text5 = voeux_obtenue(stat_GMF)
    ax5.set_title("Stats GMF")
    ax5.title.set_position([0, 0.5])

    return fig1,fig2,fig3,fig4,fig5
    


# In[ ]:





# In[195]:


#simulation_pref_tous_etu()


# In[197]:


def interface():
    essai = []
    # global autorisation
    # autorisation = False
    # global graphe
    # graphe = False
    
    class CenteredFrame(tk.Frame):
        
        
        def __init__(self, master=None, **kwargs):
            super().__init__(master, **kwargs)
            self.configure(bg="#f0f0f0")  # Light grey background
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        
            
    class ConnexionPage(tk.Tk):
        
        def __init__(self):
            super().__init__()
            self.title("Page de Connexion")
            self.geometry('500x500')
            self.configure(bg="#f0f0f0")  # Light grey background
            self.protocol("WM_DELETE_WINDOW", on_closing)
            
            #setConstante()

            
            self.main_frame = CenteredFrame(self)
            self.main_frame.pack(fill=tk.BOTH, expand=True)
    
            self.email_label = tk.Label(self.main_frame, text="Adresse e-mail:", font=("Helvetica", 12), bg="#f0f0f0")
            self.email_entry = tk.Entry(self.main_frame, font=("Helvetica", 12))
            self.password_label = tk.Label(self.main_frame, text="Mot de passe:", font=("Helvetica", 12), bg="#f0f0f0")
            self.password_entry = tk.Entry(self.main_frame, show="*", font=("Helvetica", 12))
            self.login_button = tk.Button(self.main_frame, text="Se Connecter", command=self.login, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
    
            self.email_label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
            self.email_entry.grid(row=0, column=1, padx=10, pady=10)
            self.password_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)
            self.password_entry.grid(row=1, column=1, padx=10, pady=10)
            self.login_button.grid(row=2, columnspan=2, pady=10)
    
            # Utilisez vos données de connexion ici
            self.users = listeCO
            
            self.logged_in = False  # Initialiser la variable de connexion
            
        def login(self):
            if self.logged_in:
                messagebox.showinfo("Déjà Connecté", "Vous êtes déjà connecté!")
                return
    
            email = self.email_entry.get()
            password = self.password_entry.get()
    
            if email in self.users:
                if self.users[email]["password"] == password:
                    user_type = self.users[email]["type"]
                    if user_type == "Eleve":
                        self.gotoEspaceEleve(trouverEtudiantSQL(email))
                    elif user_type == "Admin":
                        self.gotoEspaceAdmin()
                    self.logged_in = True  # Définir à True après une connexion réussie
                else:
                    messagebox.showerror("Erreur de Connexion", "Mot de passe incorrect!")
            else:
                messagebox.showerror("Erreur de Connexion", "Adresse e-mail incorrecte!")
    
        def gotoEspaceEleve(self, user_info):
            self.withdraw()  # Masquer la fenêtre de connexion
            student_window = tk.Toplevel(self)
            student_window.title("Espace Étudiant")
            student_window.geometry('600x600')
            student_window.configure(bg="#f0f0f0")  # Light grey background
            student_window.protocol("WM_DELETE_WINDOW", on_closing)
            main_frame = CenteredFrame(student_window)
            main_frame.pack(fill=tk.BOTH, expand=True)
            
            def disconnect():
                student_window.destroy()  # Fermer la fenêtre de l'espace étudiant
                self.deiconify()  # Réafficher la fenêtre de connexion
                self.logged_in = False  # Réinitialiser la variable de connexion
    
            def validate_choices():
                choice1 = choix_specialite1.get()
                choice2 = choix_specialite2.get()
                choice3 = choix_specialite3.get()
                if choix_specialite4 != None :
                    choice4 = choix_specialite4.get()
                else :
                    choice4 = "None"

                choix=[choice1,choice2,choice3,choice4]

                if len(set(choix)) != len(choix):
                    messagebox.showerror("Erreur de Choix", "Les choix doivent être différents!")
                else:
                    # Récapituler les choix
                    if  choice4 == "None" :
                        choices_summary = f"Choix 1: {choice1}\nChoix 2: {choice2}\nChoix 3: {choice3}"
                    else :
                         choices_summary = f"Choix 1: {choice1}\nChoix 2: {choice2}\nChoix 3: {choice3}\nChoix 4 : {choice4}"
                    # Demander confirmation
                    confirmation = messagebox.askquestion("Confirmation", f"Voulez-vous valider les choix suivants ?\n\n{choices_summary}")
                    if confirmation == "yes":
                        essai = []
                        messagebox.showinfo("Choix Validés", "Les choix ont été validés !")
                        essai.append(choice1)
                        essai.append(choice2)
                        essai.append(choice3)
                        if choix_specialite4 != None:
                            essai.append(choice4)
                        ecrirePrefSQL(essai, user_info['id'])
                        
            tk.Label(main_frame, text="Informations de l'Élève", font=("Helvetica", 14, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=10)
    
            nom_prenom, adresse_mail, moyenne_generale, filiere, affect = user_info["nom"], user_info["mail"], user_info["note"], user_info["filiere"], user_info["affect"]

            # Cadre pour les informations de l'élève
            info_frame = tk.Frame(main_frame, bg="#f0f0f0")
            info_frame.grid(row=1, column=0, columnspan=2)
    
            tk.Label(info_frame, text="Nom:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=0, sticky="w", padx=10, pady=5)
            tk.Label(info_frame, text=nom_prenom, font=("Helvetica", 12), bg="#f0f0f0").grid(row=0, column=1, sticky="w", padx=10, pady=5)
    
            tk.Label(info_frame, text="Adresse e-mail:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=0, sticky="w", padx=10, pady=5)
            tk.Label(info_frame, text=adresse_mail, font=("Helvetica", 12), bg="#f0f0f0").grid(row=1, column=1, sticky="w", padx=10, pady=5)
    
            tk.Label(info_frame, text="Filière:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=0, sticky="w", padx=10, pady=5)
            tk.Label(info_frame, text=filiere, font=("Helvetica", 12), bg="#f0f0f0").grid(row=2, column=1, sticky="w", padx=10, pady=5)
    
            tk.Label(info_frame, text="Moyenne Générale:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=3, column=0, sticky="w", padx=10, pady=5)
            tk.Label(info_frame, text=moyenne_generale, font=("Helvetica", 12), bg="#f0f0f0").grid(row=3, column=1, sticky="w", padx=10, pady=5)
            global autorisation

            if autorisation == True:
                if affect == None:
                    
                    # Espace entre les informations de l'élève et les choix de spécialité
                    tk.Label(main_frame, text="", bg="#f0f0f0").grid(row=2, column=0, columnspan=2, pady=10)
    
                    tk.Label(main_frame, text="Choix de Spécialité", font=("Helvetica", 14, "bold"), bg="#f0f0f0").grid(row=3, column=0, columnspan=2, pady=10)
    
                    specialites = []
                    if filiere.strip() == "GMF":
                        specialites = list(speGMF.items())
                    elif filiere.strip() == "GI":
                        specialites = list(speGI.items())
                    elif filiere.strip() == "GMI":
                        specialites = list(speGMI.items())
                    choix_specialite1 = tk.StringVar(main_frame)
                    choix_specialite1.set(specialites[0][0])  # Sélectionner la première spécialité par défaut
                    tk.Label(main_frame, text="Choix 1:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=4, column=0, sticky="w", padx=10, pady=5)
                    tk.OptionMenu(main_frame, choix_specialite1, *[s[0] for s in list(specialites)]).grid(row=4, column=1, sticky="w", padx=10, pady=5)
    
                    choix_specialite2 = tk.StringVar(main_frame)
                    choix_specialite2.set(specialites[0][0])  # Sélectionner la première spécialité par défaut
                    tk.Label(main_frame, text="Choix 2:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=5, column=0, sticky="w", padx=10, pady=5)
                    tk.OptionMenu(main_frame, choix_specialite2, *[s[0] for s in specialites]).grid(row=5, column=1, sticky="w", padx=10, pady=5)
    
                    choix_specialite3 = tk.StringVar(main_frame)
                    choix_specialite3.set(specialites[0][0])  # Sélectionner la première spécialité par défaut
                    tk.Label(main_frame, text="Choix 3:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=6, column=0, sticky="w", padx=10, pady=5)
                    tk.OptionMenu(main_frame, choix_specialite3, *[s[0] for s in specialites]).grid(row=6, column=1, sticky="w", padx=10, pady=5)
                    choix_specialite4 = None
                    if len(specialites) == 4:
                        choix_specialite4 = tk.StringVar(main_frame)
                        choix_specialite4.set(specialites[0][0])  # Sélectionner la première spécialité par défaut
                        tk.Label(main_frame, text="Choix 4:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=7, column=0, sticky="w", padx=10, pady=5)
                        tk.OptionMenu(main_frame, choix_specialite4, *[s[0] for s in specialites]).grid(row=7, column=1, sticky="w", padx=10, pady=5)
    
                    # Bouton Valider en bas à droite de la fenêtre, de couleur verte
                    tk.Button(main_frame, text="Valider", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), command=validate_choices).grid(row=8, column=1, sticky="e", padx=10, pady=20)
                
                else:
                    tk.Label(info_frame, text="Spécialité affectée:", font=("Helvetica", 12), bg="#f0f0f0").grid(row=4, column=0, sticky="w", padx=10, pady=5)
                    tk.Label(info_frame, text=user_info["specialite"], font=("Helvetica", 12), bg="#f0f0f0").grid(row=4, column=1, sticky="w", padx=10, pady=5)
                
            # Bouton de déconnexion en haut à droite, en dehors de la grille
            disconnect_button = tk.Button(student_window, text="Déconnexion", bg="red", fg="white", font=("Helvetica", 12, "bold"), command=disconnect)
            disconnect_button.pack(anchor="ne", padx=10, pady=10)
    
        def gotoEspaceAdmin(self):
            self.withdraw()  # Masquer la fenêtre de connexion
            admin_window = tk.Toplevel(self)
            admin_window.title("Espace Administration")
            admin_window.geometry('1280x720')
            admin_window.configure(bg="#f0f0f0")  # Light grey background
            admin_window.protocol("WM_DELETE_WINDOW", on_closing)
            main_frame = CenteredFrame(admin_window)
            main_frame.pack(fill=tk.BOTH, expand=True)

            
            
            def actualiser():
                admin_window.destroy()
                self.gotoEspaceAdmin()


            def affectationClasse():
                global graphe
                graphe = True
                actualiser()

            def simulation():
                simulation_pref_tous_etu()
                actualiser()

            
            def autoriserChoix():
                global autorisation
                global graphe
                autorisation = True
                auto.pack_forget()
                cancel.pack(anchor="ne", padx=10, pady=10)
                lancerAffectatioBouton.pack(anchor="ne", padx=10, pady=10)
                actualiser()

            def RmChoix():
                global autorisation
                global graphe
                autorisation = False
                cancel.pack_forget()
                lancerAffectatioBouton.pack(anchor="ne", padx=10, pady=10)
                actualiser()

            
            global autorisation

            tk.Label(main_frame, text="Espace Administration", font=("Helvetica", 14, "bold"), bg="#f0f0f0").pack()

            def disconnect():
                admin_window.destroy()  # Fermer la fenêtre de l'espace admin
                self.deiconify()  # Réafficher la fenêtre de connexion
                self.logged_in = False  # Réinitialiser la variable de connexion
            # Bouton de déconnexion en haut à droite, en dehors de la grille
            disconnect_button = tk.Button(admin_window, text="Déconnexion", bg="red", fg="white", font=("Helvetica", 12, "bold"), command=disconnect)
            disconnect_button.pack(anchor="ne", padx=10, pady=10)
            
            ##Def des boutons
            lancerAffectatioBouton = tk.Button(main_frame, text="Lancer affectation", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), command=affectationClasse)
            auto = tk.Button(main_frame, text="Autoriser choix", bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), command=autoriserChoix)
            cancel = tk.Button(main_frame, text="Interdire choix", bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), command=RmChoix)
            simu = tk.Button(main_frame, text="Simulation", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), command=simulation)
            
            simu.pack(anchor="ne", padx=600, pady=10)
            
            
            
            if autorisation == True:

                cancel.pack(anchor="ne", padx=8, pady=8)
                
                lancerAffectatioBouton.pack(anchor="ne", padx=10, pady=10)

                global graphe
                
            
                if graphe == True:  # code pour afficher les stats une fois l'affectation terminée (graphe==true)
                    lancerAffectatioBouton.pack_forget()
                    cancel.pack_forget()
                    auto.pack_forget()
                    simu.pack_forget()

    
                    # Créer un canvas
                    canvas = tk.Canvas(main_frame)
                    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
                    
                    # Ajouter une scrollbar au canvas
                    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
                    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                    
                    # Configurer le canvas avec la scrollbar
                    canvas.configure(yscrollcommand=scrollbar.set)
                    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
                    
                    # Créer un autre frame à l'intérieur du canvas
                    second_frame = tk.Frame(canvas)
                    
                    # Ajouter ce nouveau frame dans une fenêtre du canvas
                    canvas.create_window((0,0), window=second_frame, anchor="nw")
                    
                    # Affectation des figures
                    fig1, fig2, fig3, fig4, fig5 = affectation()
                    
                    # Ajouter les graphiques au second_frame
                    for fig in [fig1, fig2, fig3, fig4, fig5]:
                        canvas_fig = FigureCanvasTkAgg(fig, master=second_frame)
                        canvas_fig.draw()
                        canvas_fig.get_tk_widget().pack()
                    
                else :

                    ##Liste des etudiants 
                    etuCV = listeEtuCV()  # fonction codée plus haut
                    etuCNV = listeEtuCNV()  # fonction codée plus haut
        
                    # Ajouter un cadre principal pour contenir les deux cadres des listes
                    lists_frame = tk.Frame(main_frame, bg="#f0f0f0")
                    lists_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
                    # Cadre pour les étudiants n'ayant pas validé leurs choix
                    left_frame = tk.Frame(lists_frame, bg="#f0f0f0")
                    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
                    tk.Label(left_frame, text="Elèves n'ayant pas validé leur choix:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
                    
                    left_canvas = tk.Canvas(left_frame, bg="#f0f0f0")
                    left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
                    left_scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=left_canvas.yview)
                    left_scrollbar.pack(side=tk.RIGHT, fill="y")
        
                    left_scrollable_frame = tk.Frame(left_canvas, bg="#f0f0f0")
                    left_scrollable_frame.bind(
                        "<Configure>",
                        lambda e: left_canvas.configure(
                            scrollregion=left_canvas.bbox("all")
                        )
                    )
                    
                    left_canvas.create_window((0, 0), window=left_scrollable_frame, anchor="nw")
                    left_canvas.configure(yscrollcommand=left_scrollbar.set)
        
                    for e in etuCNV:
                        tk.Label(left_scrollable_frame, text=f"      {e['prenom']} {e['nom']} - {e['mail']}", font=("Helvetica", 12), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
        
                    # Cadre pour les étudiants ayant validé leurs choix
                    right_frame = tk.Frame(lists_frame, bg="#f0f0f0")
                    right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
                    tk.Label(right_frame, text="Elèves ayant validé leur choix:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
        
                    right_canvas = tk.Canvas(right_frame, bg="#f0f0f0")
                    right_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
                    right_scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=right_canvas.yview)
                    right_scrollbar.pack(side=tk.RIGHT, fill="y")
        
                    right_scrollable_frame = tk.Frame(right_canvas, bg="#f0f0f0")
                    right_scrollable_frame.bind(
                        "<Configure>",
                        lambda e: right_canvas.configure(
                            scrollregion=right_canvas.bbox("all")
                        )
                    )
        
                    right_canvas.create_window((0, 0), window=right_scrollable_frame, anchor="nw")
                    right_canvas.configure(yscrollcommand=right_scrollbar.set)
        
                    for e in etuCV:
                        tk.Label(right_scrollable_frame, text=f"      {e['prenom']} {e['nom']} - {e['mail']}", font=("Helvetica", 12), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
                
            else:
                auto.pack(anchor="ne", padx=10, pady=10)
                simu.pack(anchor="ne", padx=600, pady=10)

                ##Liste des etudiants 
                etuCV = listeEtuCV()  # fonction codée plus haut
                etuCNV = listeEtuCNV()  # fonction codée plus haut
    
                # Ajouter un cadre principal pour contenir les deux cadres des listes
                lists_frame = tk.Frame(main_frame, bg="#f0f0f0")
                lists_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
                # Cadre pour les étudiants n'ayant pas validé leurs choix
                left_frame = tk.Frame(lists_frame, bg="#f0f0f0")
                left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    
                tk.Label(left_frame, text="Elèves n'ayant pas validé leur choix:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
                
                left_canvas = tk.Canvas(left_frame, bg="#f0f0f0")
                left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
                left_scrollbar = tk.Scrollbar(left_frame, orient="vertical", command=left_canvas.yview)
                left_scrollbar.pack(side=tk.RIGHT, fill="y")
    
                left_scrollable_frame = tk.Frame(left_canvas, bg="#f0f0f0")
                left_scrollable_frame.bind(
                    "<Configure>",
                    lambda e: left_canvas.configure(
                        scrollregion=left_canvas.bbox("all")
                    )
                )
                
                left_canvas.create_window((0, 0), window=left_scrollable_frame, anchor="nw")
                left_canvas.configure(yscrollcommand=left_scrollbar.set)
    
                for e in etuCNV:
                    tk.Label(left_scrollable_frame, text=f"      {e['prenom']} {e['nom']} - {e['mail']}", font=("Helvetica", 12), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
    
                # Cadre pour les étudiants ayant validé leurs choix
                right_frame = tk.Frame(lists_frame, bg="#f0f0f0")
                right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    
                tk.Label(right_frame, text="Elèves ayant validé leur choix:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
    
                right_canvas = tk.Canvas(right_frame, bg="#f0f0f0")
                right_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
                right_scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=right_canvas.yview)
                right_scrollbar.pack(side=tk.RIGHT, fill="y")
    
                right_scrollable_frame = tk.Frame(right_canvas, bg="#f0f0f0")
                right_scrollable_frame.bind(
                    "<Configure>",
                    lambda e: right_canvas.configure(
                        scrollregion=right_canvas.bbox("all")
                    )
                )
    
                right_canvas.create_window((0, 0), window=right_scrollable_frame, anchor="nw")
                right_canvas.configure(yscrollcommand=right_scrollbar.set)
    
                for e in etuCV:
                    tk.Label(right_scrollable_frame, text=f"      {e['prenom']} {e['nom']} - {e['mail']}", font=("Helvetica", 12), bg="#f0f0f0").pack(anchor="w", padx=5, pady=5)
    def on_closing():
        try:
            admin_window
            admin_window.destroy()
            # Si la variable est définie
        except NameError:
            # La variable n'est pas définie
            pass
        try:
            student_window
            student_window.destroy()
            # Si la variable est définie
        except NameError:
            # La variable n'est pas définie
            pass
        try:
            self
            self.destroy()
            # Si la variable est définie
        except NameError:
            # La variable n'est pas définie
            pass
        app.destroy()
    
    if __name__ == "__main__":
        app = ConnexionPage()
        app.protocol("WM_DELETE_WINDOW", on_closing)
        app.mainloop()

interface()

