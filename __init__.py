from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'winido'
logger = getLogger(__author__)


class WinidoTestSkill(MycroftSkill):
    def __init__(self):
        super(WinidoTestSkill, self).__init__(name="WinidoTestSkill")

    def initialize(self):
        start_intent = IntentBuilder("StartIntent").require("PlayKeyWord").build()
        self.register_intent(start_intent, self.handle_start_intent)

    def handle_start_intent(self, message):
        try:
            self.speak_dialog("response", None, true)
        except:
            self.speak_dialog("error")

def create_skill():
    return WinidoTestSkill()