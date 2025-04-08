## Usage (WSL)

Make virtual environment:
```angular2html
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
- Must create a .env file add API_KEY=\<google genai key\> from the following link: https://aistudio.google.com/app/apikey

- Must create a .env file add OPENAI_API_KEY=\<your OpenAI key here\>. This uses GPT-4o (vision) from OpenAI. 


Running backend:
```angular2html
python3 app.py
```
