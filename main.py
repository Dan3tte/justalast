import psutil
from datetime import datetime, timedelta, time


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
    heure_actuelle= 10
    if (not est_en_game(jeu) and heure_depassee(limite)):
        quitte(jeu)
    else:
        if heure_actuelle(limite):
            print("limite d'heure non dépassée")
        return()



limite =time(18,4)

jeu = "snap-store"


Sleepnow(limite,jeu)

#caca