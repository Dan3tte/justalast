import psutil
import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta, time
import urllib3
import re

#desactive le warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def trouvepid(jeu):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == jeu:
            return proc.info['pid']
    print("jeu non trouvé")
    return None


def heure_depassee(heure: time):
    mtn = datetime.now()
    limite = datetime.combine(mtn.date(), heure)
    if heure < mtn.time() and heure < time(6,0):
        print('mode nuit')
        limite += timedelta(days=1)
    return mtn >= limite



def quitte(jeu):
    proc = psutil.Process(trouvepid(jeu))
    proc.kill()
    print("jeu quitté")
    return()



def est_en_game(jeu):
    # VALO

    # Trouver Lockfile -> Extraire le port + token -> Appeler URL avec les infos 
    #-> Comparer les infos ("Ingame, Menus, Pregame...") 

    # LOL
    if jeu == "League of Legends (TM) Client":  
        print("est en game de lol")
        return True
    else:
        return False




def Sleepnow (limite,jeu):
    if (not est_en_game(jeu) and heure_depassee(limite)):
        quitte(jeu)
    else:
        if heure_depassee(limite):
            print("limite d'heure non dépassée")
        return()


chemin_lockfile = os.path.join(
    os.environ["LOCALAPPDATA"],"Riot Games","Riot Client","Config","lockfile"
)


def lirefile():
    with open(chemin_lockfile, "r", encoding="utf-8") as fichier:
        lockfile = fichier.read()
    parties = lockfile.split(":")
    return parties
    

parties = lirefile()
print(parties)

PID= parties[1]
port = parties[2]
token = parties [3]
protocole = parties [4]

#endpoint 
endpoints = "/entitlements/v1/token"

#demande du bon port permettant de faire des endpoints sur le gamestate
url_sessions = f"{protocole}://127.0.0.1:{port}{endpoints}"

#requete pour recup le bon port
reponse = requests.get(url_sessions, auth=HTTPBasicAuth("riot", token),verify = False)

print ("Status :", reponse.status_code)
print ("Réponse :", reponse.text)


limite = time(12,0)

jeu = "snap-store"


Sleepnow(limite,jeu)
