#Import des modules et chargement des données
import json
import matplotlib.pyplot as plt
import pandas as pd

import datetime
from collections import defaultdict
import numpy as np

d = open('data_rhobs.json', encoding = 'utf-8')
clients = json.load(d, )

    #--------------------------------------------------------------
    #Nombre de clients écoutant chaque style de musique
    #Fonctionne mais prend beaucoup de temps à s'exécuter

def nb_clients_genre() :

    records_musique = []
    for key, value in clients.items() : 
        for elt in value['music'] :
            records_musique.append(elt)
            
    musique = {elt : records_musique.count(elt) for elt in records_musique}

    print("Le nombre de clients écoutant chaque style de musique : ", '\n\n', musique)

    #Plot des résultats
    names = list(musique.keys())
    values = list(musique.values())

    plt.barh(range(len(musique)), sorted(values), tick_label=names)
    plt.show()
    
    
    #--------------------------------------------------------------
    #Âge moyen des clients pour chaque style de musique
    
def age_moyen() :

    #Création d'une nouvelle variable indiquant l'âge du client
    for key, value in clients.items() :
        birthdate = pd.to_datetime(value['birthdate']).year
        now = datetime.datetime.now().year
        value['age'] = now - birthdate

    #On effectue un groupby sur les musiques, en sélectionnant les différents âges
    res = defaultdict(list)
    for key, value in sorted(clients.items()):
        for elt in value['music'] :
            res[elt].append(value['age'])
    dico = dict(res)

    #On donne pour valeur la moyenne arrondie des âges
    for key, value in dico.items() :
        dico[key] = round(np.mean(value), 1)

    print("L'âge moyen des clients pour chaque style de musique : ", '\n\n', dico)
    
    
    #Plot des résultats
    names = list(dico.keys())
    values = list(dico.values())

    plt.barh(range(len(dico)), sorted(values), tick_label=names)
    plt.show()
    
    
    #--------------------------------------------------------------    
    #Fonction de la pyramide des âges
    
def pyramide_age(city, slice_size) :
    res = defaultdict(list)

    #Création d'une nouvelle variable indiquant la tranche d'âge du client. 
    #La taille de la tranche est indiquée par l'argument slice_size
    for key, value in clients.items():
        value['tranche_age'] = pd.cut([value['age']],  bins = np.arange(0, 100, slice_size))

    #On effectue un groupby sur les tranches d'âge, en sélectionnant les différentes personnes        
    for key, value in clients.items():
        for elt in value['tranche_age'] :
            if value['city'] == city :
                res[elt].append(key)
                dico = dict(res)

    return dico


