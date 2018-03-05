from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'winido'
logger = getLogger(__author__)


class WinidoTestSkill(MycroftSkill):
    def __init__(self):
        super(WinidoTestSkill, self).__init__(name="WinidoTestSkill")

    def initialize(self):
        start_intent = IntentBuilder("StartIntent").require("PlayKeyWord").adds_context('playing').build()
        self.register_intent(start_intent, self.handle_start_intent)

    def handle_start_intent(self, message):
        try:
            self.speak_dialog("response.dialog", None, true)
            self.count = 0
            self.play=true
            while play:
                self.speak_dialog("question", None, true)
                play = false
        except:
            self.speak_dialog("error")

    @intent_handler(IntentBuilder('CorrectAnswerIntent').require("answer1KeyWord").build())
    def answer_intent(self, message):
        self.speak_dialog("CorrectAnswer")

    @intent_handler(IntentBuilder('WrongAnswerIntent').build())
    def answer_intent(self, message):
        self.speak_dialog("WrongAnswer")

def create_skill():
    return WinidoTestSkill()