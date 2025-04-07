from blackboard import Blackboard
from agents import BlipIdentification, LlmIdentification, Classification


class BlackboardController:
    def __init__(self, image_path, post_details):
        self.image_path = image_path
        self.blackboard = Blackboard(image_path, post_details)
        self.classification_agent = Classification()
        self.llm_agent = LlmIdentification()
        self.other_agent = BlipIdentification()
        self.response = {}

    def identify(self):
        try:
            self.response['response1'] = self.classification_agent.analyze(self.image_path)
            self.response['response2'] = self.llm_agent.analyze(self.image_path)
            self.response['response3'] = self.other_agent.analyze(self.image_path)
        except Exception as e:
            print("Unable to identify error:" + e)
        finally:
            self.blackboard.update_identification(self.response)

    def getresponse(self):
        return self.blackboard.return_identification()
