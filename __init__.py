# coding=utf-8
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'winido'
logger = getLogger(__author__)


class WinidoTestSkill(MycroftSkill):
    def __init__(self):
        super(WinidoTestSkill, self).__init__(name="WinidoTestSkill")

    @intent_handler(IntentBuilder("StartIntent").require("PlayKeyWord"))
    def handle_start_intent(self, message):
        self.speak_dialog("response", None, expect_response=True)
        play = True
        while play:
            self.speak_dialog("question", None, expect_response=True)
            play = False

    @intent_handler(IntentBuilder('AnswerIntent').require("answer1KeyWord"))
    def handle_answer_intent(self, message):
        logger.error(self, message.data["answer1KeyWord"])
        if message.data["answer1KeyWord"] == "नरेंद्र मोदी":
            self.speak_dialog("CorrectAnswer")
        else:
            self.speak_dialog("WrongAnswer")

    @intent_handler(IntentBuilder('NoAnswerIntent'))
    def handle_no_answer_intent(self, message):
        logger.error(self, message)
        self.speak_dialog("WrongAnswer")


def create_skill():
    return WinidoTestSkill()
