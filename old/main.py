from discordrp import Presence
import time

client_id = "1128041207071772856"  # Replace this with your own client id

with Presence(client_id) as presence:
    presence.set(
        {
            "state": "In Game",
            "details": "Summoner's Rift",
            "timestamps": {"start": int(time.time())},
        }
    )

    while True:
        time.sleep(15)