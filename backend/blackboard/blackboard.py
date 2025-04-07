from agents import SummarizationAgent, BuyingAgent
class Blackboard:
    def __init__(self, image_path, post_details):
        self.image_data = image_path
        self.input_data = post_details
        self.agent_results = []
        self.buying_agent = BuyingAgent()
        self.summary_agent = SummarizationAgent()
        self.buying_data = []
        self.output_data = []


    def update_identification(self, identification):
        self.agent_results.append(identification)

    def return_identification(self):
        self.buying_data = self.buying_agent.analyze(self.agent_results)
        self.output_data = self.summary_agent.analyze(self.agent_results)

        return {"identification": self.output_data,
                "purchase_link": self.buying_data}
