from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPalette, QColor
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from MainWindow import Ui_MainWindow
import json
from pathlib import Path

import sys

loader = QUiLoader()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setupUi(self)
        
        client_id = ""#1007320805128024154

        saveDataFile = Path("./saveData.json")
        if (saveDataFile.is_file() == True):
            with open('saveData.json') as f:
                saveData = json.load(f)
                client_id = saveData.get("appid")
        else:
            print("No saveData file provided!")
        
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
                
        def getStringOrNone(config: dict, configPath: str):
            string = config.get(configPath)
            if (string == "" or string == " "): return None
            else: return string
        
        self.input_appid.setText(client_id)
        self.input_details.setText(getStringOrNone(config, "details"))
        self.input_state.setText(getStringOrNone(config, "state"))
        
        self.number_partyMax.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.number_partyMin.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.date_customtimestamp.setDisabled(True)
        
        self.button_save.clicked.connect(self.save)
        
    def save(self):
        print("Saved!: ", self.lb_appid.text())
        configFile = Path("./config.json")
        if (configFile.is_file() == True):
            newConfig = {
                "preset": "none",
                
                "details": self.input_details.text(),
                "state": self.input_state.text(),

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

            with open("config.json", "w") as fp:
                json.dump(newConfig, fp)

app = QApplication( sys.argv + ['-platform', 'windows:darkmode=2'] )

window = MainWindow()
window.show()

app.exec()