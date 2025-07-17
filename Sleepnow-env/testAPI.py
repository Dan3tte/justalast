import os
from valorant import LocalClient
import json
import base64
from dotenv import load_dotenv

load_dotenv()

client = LocalClient()


presence = client.get_presences(user=True)

private = presence.get('private')

missing_padding = len(private) % 4
if missing_padding:
    private += '=' *(4 - missing_padding)

decoded =base64.urlsafe_b64decode(private).decode('utf-8')
private_data =json.loads(decoded)

print(private_data.get("sessionLoopState"))
