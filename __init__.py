from mycroft import MycroftSkill, intent_file_handler
import subprocess
import os.path
#import os

ALERT = 'mb19_e'
ZONE = 'mb-24_e'

class EvcanAlerts(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    def initialize(self):
        self._setup()
        self.settings.set_changed_callback(self.on_websettings_changed)

    def on_websettings_changed(self):
        # Only attempt to load if the host is set
        self.log.debug("websettings changed")
        self._setup()

    def _setup(self):
        self.zone_id = self.settings.get('zone_id','')
        self.alert_id = self.settings.get('alert_id','')
        self.mqtt_ip = self.settings.get('mqtt_ip','')
        self.mqtt_opt = self.settings.get('mqtt_opt','')
        MQTT = self.mqtt_ip + " " + self.mqtt_opt
        
        SETTINGS = self.alert_id + " " + MQTT
        os.system("skills/Evcan-alerts-skill/./WAlert " + SETTINGS + " >nul 2>&1 | echo started") 

    @intent_file_handler('alerts.evcan.intent')
    def handle_alerts_evcan(self, message):
        self.log.debug("handle_alerts for zone_id {}".format(self.zone_id))
        if not self.zone_id:
            self.speak_dialog('error')
            return
        ##alerts = os.popen("ls").read()
        alerts = os.popen("skills/Evcan-alerts-skill/./alert.sh " + self.alert_id).read()
        zone = os.popen("skills/Evcan-alerts-skill/./zone.sh "+ self.zone_id).read()
        print(alerts)
        self.speak(alerts)  
        self.speak(' Currently ')
        self.speak(zone)

def create_skill():
    return EvcanAlerts()

