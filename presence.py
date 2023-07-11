from pypresence import Presence
import time
import json
from pathlib import Path

startTime = int(time.time())

client_id = "000000"#1007320805128024154

saveDataFile = Path("./saveData.json")
if (saveDataFile.is_file() == True):
    with open('saveData.json') as f:
        saveData = json.load(f)
        client_id = saveData.get("appid")
else:
    print("No saveData file provided!")

RPC = Presence(client_id =client_id)

config = {
    "preset": "none",
    
    "details": "My very nice details!",
    "state": "A very nice custom State!",

    "large_image": "",
    "large_text": "",

    "small_image": "",
    "small_text": "",

    "party_players": 2,
    "party_maxplayers": -1,

    "start_time": "timesincestart",
    "customtimestamp": 0,

    "buttons": [
        {
            "label": "Button 1",
            "url": "https://strassburger.org/"
        },
        {
            "label": "Button 2",
            "url": "https://strassburger.org/"
        }
    ]
}


configFile = Path("./config.json")
if (configFile.is_file() == True):
    with open('config.json') as f:
        newConfig = json.load(f)
        config = newConfig
else:
    print("No config provided!")
    
    
def getStringOrNone(config: dict, configPath: str):
    string = config.get(configPath)
    if (string == "" or string == " "): return None
    else: return string
    

def getPartyList(config: dict, playersPath: str, maxPlayersPath: str):
    players = config.get(playersPath)
    if players < 0: return None
    maxPlayers = config.get(maxPlayersPath)
    if maxPlayers < 0:return None
    return [players, maxPlayers]


def getTime(config: dict):
    if (config.get("start_time") == "timesincestart"):
        return startTime
    elif (config.get("start_time") == "localtime"):
        currentTime = int(time.time())
        localtime = time.localtime()
        hour = localtime.tm_hour
        minute = localtime.tm_min
        second = localtime.tm_sec
        
        return currentTime - (hour * 60 * 60) - (minute * 60) - second
    elif (config.get("start_time") == "customtimestamp"):
        if (config.get("customtimestamp") < 10): return 10
        return config.get("customtimestamp")
    else:
        return None
    
def updatePresence():
    newConfig = {
        "preset": "none",
        "details": "My very nice details!",
        "state": "A very nice custom State!",
        "large_image": "",
        "large_text": "",
        "small_image": "",
        "small_text": "",
        "party_players": 2,
        "party_maxplayers": -1,
        "start_time": "timesincestart",
        "customtimestamp": 0,
        "buttons": [
            {
                "label": "Button 1",
                "url": "https://strassburger.org/"
            },
            {
                "label": "Button 2",
                "url": "https://strassburger.org/"
            }
        ]
    }
    
    configFile = Path("./config.json")
    if (configFile.is_file() == True):
        with open('config.json') as f:
            newConfig = json.load(f)
    else:
        print("No config provided!")
    
    update = RPC.update(
        details = getStringOrNone(config=newConfig, configPath="details"),
        state = getStringOrNone(config=newConfig, configPath="state"),
        large_image = getStringOrNone(config=newConfig, configPath="large_image"),
        large_text = getStringOrNone(config=newConfig, configPath="large_text"),
        small_image = getStringOrNone(config=newConfig, configPath="small_image"),
        small_text = getStringOrNone(config=newConfig, configPath="small_text"),
        party_size = getPartyList(config=newConfig, playersPath="party_players", maxPlayersPath="party_maxplayers"),
        start=getTime(config=newConfig),
        buttons = newConfig.get("buttons")
    )
    print(update)


def start():
    connectsuccess = True
    
    try:
        RPC.connect()
    except Exception as e:
        connectsuccess = False
        print(e)
    
    if (connectsuccess == False):
        print("No connection")
        return
    
    update = RPC.update(
        details=getStringOrNone(config=config, configPath="details"),
        state=getStringOrNone(config=config, configPath="state"),
        large_image=getStringOrNone(config=config, configPath="large_image"),
        large_text=getStringOrNone(config=config, configPath="large_text"),
        small_image=getStringOrNone(config=config, configPath="small_image"),
        small_text=getStringOrNone(config=config, configPath="small_text"),
        party_size=getPartyList(config=config, playersPath="party_players", maxPlayersPath="party_maxplayers"),
        start=getTime(config=config),
        buttons=config.get("buttons"),
    )
    print("Discord-RP started!")

    while True:
        def stop():
            RPC.close()
            print("Closed connection")
            
        def restart():
            RPC.connect()
            updatePresence()
            print("Restarted connection")
            
        # time.sleep(10)
        # stop()

        # time.sleep(10)
        # restart()
        
        time.sleep(30)
        updatePresence()

start()