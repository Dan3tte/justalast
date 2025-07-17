import os
import valorant
from dotenv import load_dotenv
load_dotenv()


KEY = os.environ["API_KEY"]

client = valorant.Client(KEY, locale=None)
skins = client.get_skins()
name = input("Search a Valorant Skin Collection: ")

results = skins.find_all(name=lambda x: name.lower() in x.lower())

print("\nResults: ")
for skin in results:
    print(f"\t{skin.name.ljust(21)} ({skin.localizedNames['ja-JP']})")