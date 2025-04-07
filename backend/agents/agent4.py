from google import genai
import os
from dotenv import load_dotenv

class BuyingAgent:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        client = genai.Client(api_key=api_key)
        self.client = client

    def analyze(self, agent_results):


        prompt = f""" 
        For the given information regarding the type and model of shoe, 
        provide a location where the shoe can be bought on the internet.
        For example if the shoe is for sale on the nike website, provide a link to the website.
        If the shoe is no longer availible for purchase either say that or where it can be bought at resale.
        Do not specify an exact link to the shoe but only to the main webpage of the seller. 
        You response should be formatted in a markdown friendly manner as follows:
        
        You can often find <INSERT SHOE NAME> on the following websites:
        
        *   <WEBSITE NAME>: <LINK>
        *   <WEBSITE NAME>: <LINK>
        ...
        
        Context:
        {agent_results}"""

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt)

        return response.text