from mycroft import MycroftSkill, intent_file_handler


class StiriSportive(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('sportive.stiri.intent')
    def handle_sportive_stiri(self, message):
        self.speak_dialog('sportive.stiri')


def create_skill():
    return StiriSportive()

