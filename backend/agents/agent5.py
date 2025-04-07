from google import genai
import os
from dotenv import load_dotenv


class SummarizationAgent:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        client = genai.Client(api_key=api_key)
        self.client = client

    def analyze(self, agent_results):
        prompt = f""" 
        Provide a markdown formatted response that summarizes the shoe identification based on the context. 
        You answer should provide the following:
        Brand: <BRAND>
        ShoeModel: <Model>
        Colorway: <COLORWAY>

        Context:
        {agent_results}"""

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt)

        return response.text
