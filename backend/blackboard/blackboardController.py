from blackboard import Blackboard
from agents import *


class BlackboardController:
    def __init__(self, image_path, post_details):
        self.image_path = image_path
        self.blackboard = Blackboard(image_path, post_details)
        self.classification_agent = Classification()
        self.llm_agent = LlmIdentification()
        self.other_agent = OtherID()
        self.response = {}

    def identify(self):
        self.response['response1'] = self.classification_agent.analyze(self.image_path)
        self.response['response2'] = self.llm_agent.analyze(self.image_path)
        self.response['response3'] = self.other_agent.analyze(self.image_path)
        self.blackboard.update_identification(self.response)

    def getresponse(self):
        return self.blackboard.return_identification()
