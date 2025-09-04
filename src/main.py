import psutil #recherche pid linux / windows
import os
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta, time
import urllib3
import re
from APIvalo import ingameValo

#lancer le schedular dans un autre thread pour permettre de faire tourner la boucle de l'ui
import threading

#boucler
from apscheduler.schedulers.background import BackgroundScheduler

#desactive le warning SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#ui
if __name__ =="__main__":
    from ui import lancer_ui
    lancer_ui()

def trouvepid(jeu):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == jeu:
            return proc.info['pid']
    return None


def heure_depassee(heure: time):
    mtn = datetime.now()
    limite = datetime.combine(mtn.date(), heure)
    if heure < mtn.time() and heure < time(6,0):
        print('mode nuit')
        limite += timedelta(days=1)
    return mtn >= limite



def quitte(jeu):
    pid = trouvepid(jeu)
    if pid == None:
        return
    proc = psutil.Process(pid)
    proc.kill()
    print("jeu quitté")
    return



def est_en_game_valo():
    if trouvepid("VALORANT.exe") != None:
        if ingameValo()=="INGAME":
            print("est en game valo")
            return True
        else:
            return False
    else:
        print("Valorant non trouvé")

def est_en_game_lol():
    jeu = "League of Legends.exe"
    if trouvepid(jeu) != None: 
        return True
    else:
        return False
    elseprint ("Lol non trouvé")

def est_en_game():
    return est_en_game_lol() or est_en_game_valo()


def Sleepnow (limite):
    if not heure_depassee(limite):
        print("limite non atteinte !")
        return()
    if est_en_game():
        return()
    else:
        quitte("LeagueClient.exe")
        quitte("VALORANT-Win64-Shipping.exe")
        quitte("RiotClientServices.exe")
        return ()


scheduler = None 

def start_scheduler(limite):
    global scheduler
    stop_scheduler()
    scheduler = BackgroundScheduler()
    scheduler.add_job(Sleepnow, 'interval', seconds=5, args=[limite,])
    scheduler.start()

def stop_scheduler():
    global scheduler
    if scheduler is not None:
        scheduler.shutdown()
        scheduler=None
        print("Scheduler arrêté")


#lance schedular dans un thread séparé : 
def start_threading(limite):
    thread = threading.Thread(target = start_scheduler,args=(limite,), daemon=True)
    thread.start()

