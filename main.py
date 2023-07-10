from pypresence import Presence
import time
import json
from pathlib import Path

client_id = "1035313051454406736"
RPC = Presence(client_id)

RPC.connect()

config = {
    "state": "test"
}

configFile = Path("./config.json")
if (configFile.is_file() == True):
    with open('config.json') as f:
        newConfig = json.load(f)
        config = newConfig
else:
    print("No config provided!")

print(config)

update = RPC.update(state=config.get("state"), details=config.get("details"), large_image="communitydiscord",  buttons=[{"label": "My Website", "url": "https://qtqt.cf"}, {"label": "My Website", "url": "https://strassburger.org"}])

while True:
    time.sleep(30)
    update = RPC.update(state="State", large_image="communitydiscord",  details="Details", buttons=[{"label": "My Website", "url": "https://qtqt.cf"}, {"label": "My Website", "url": "https://strassburger.org"}])
    print(update)