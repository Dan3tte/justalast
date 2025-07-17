import os
from valorant import LocalClient
from dotenv import load_dotenv
load_dotenv()


client = LocalClient()

status = client.get_session()


# Exemple d’accès possible à l'état (à adapter selon le nom de la propriété)
print("Phase:", session.phase)
# ou
print("InGame:", session.in_game)
#skins = client.get_skins()

#name = input("Search a Valorant Skin Collection: ")

#results = skins.find_all(name=lambda x: name.lower() in x.lower())

#print("\nResults: ")
#for skin in results:
 #   print(f"\t{skin.name.ljust(21)} ({skin.localizedNames['ja-JP']})")