import os
from valorant import LocalClient
import json
from dotenv import load_dotenv

load_dotenv()


client = LocalClient()

status = client.get_session()
precence = client.get_presences(user=True)

private_data_raw = precence['private']
private_data = json.loads(private_data_raw)

print(private_data['sessionLoopState'])

#skins = client.get_skins()

#name = input("Search a Valorant Skin Collection: ")

#results = skins.find_all(name=lambda x: name.lower() in x.lower())

#print("\nResults: ")
#for skin in results:
 #   print(f"\t{skin.name.ljust(21)} ({skin.localizedNames['ja-JP']})")