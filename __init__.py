from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
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
        self.speak_dialog("response", None, expect_response=True)
        play = True
        while play:
            self.speak_dialog("question", None, expect_response=True)
            play = False

    @intent_handler(IntentBuilder('CorrectAnswerIntent').require("answer1KeyWord"))
    def answer_intent(self, message):
        self.speak_dialog("CorrectAnswer")

    @intent_handler(IntentBuilder('WrongAnswerIntent'))
    def answer_intent(self, message):
        self.speak_dialog("WrongAnswer")


def create_skill():
    return WinidoTestSkill()
