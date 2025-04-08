from openai import OpenAI
import os
from dotenv import load_dotenv
import base64
from PIL import Image

class BlipIdentification:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")

    def analyze(self, image_path):
        base64_image = self.encode_image(image_path)

        prompt = """
         You are an expert in fashion and sneaker identification. Analyze the provided image of a shoe and return the following details:
                   Brand/Make (e.g., Nike, Adidas, New Balance)
                   Model Name (e.g., Air Jordan 1, Yeezy Boost 350)
                   Colorway or Edition (e.g., Bred, Triple White, Off-White x Nike)
                   Style or Category (e.g., running shoe, basketball sneaker, casual, skateboarding)
                   Distinguishing Features (e.g., materials, logos, design patterns, lacing system)
                   Estimated Release Year or Collection (if identifiable)
                   Be as specific and detailed as possible. If unsure, provide the closest match or a list of possible models."""

        response = self.client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=500,
    )


        return response.choices[0].message.content

