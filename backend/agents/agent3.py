from google import genai
import os
from dotenv import load_dotenv
import PIL.Image

class LlmIdentification:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("API_KEY")
        client = genai.Client(api_key=api_key)
        self.client = client

    def analyze(self, image_path):


        prompt = """ You are an expert in fashion and sneaker identification. Analyze the provided image of a shoe and return the following details:
                   Brand/Make (e.g., Nike, Adidas, New Balance)
                   Model Name (e.g., Air Jordan 1, Yeezy Boost 350)
                   Colorway or Edition (e.g., Bred, Triple White, Off-White x Nike)
                   Style or Category (e.g., running shoe, basketball sneaker, casual, skateboarding)
                   Distinguishing Features (e.g., materials, logos, design patterns, lacing system)
                   Estimated Release Year or Collection (if identifiable)
                   Be as specific and detailed as possible. If unsure, provide the closest match or a list of possible models."""

        image = PIL.Image.open(image_path)

        response = self.client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[image, prompt])

        return response.text
