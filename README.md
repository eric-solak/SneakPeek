# SneakPeek

## 📝 Product Description
This project is a mobile sneaker identification and social forum app that uses AI to recognize shoe models from user-uploaded images.
Users post pictures of sneakers, recieve AI-powered responses for the exact shoe type, and can interact with posts through ratings and comments.

This project uses a custom, PyTorch based deep-learning model, trained by [Eric Solak](https://github.com/eric-solak). The link to the model can be found on HuggingFace: https://huggingface.co/eric-solak/ShoeClassificationAI
## ✨ Features
- **Sneaker Identification**
  
  - Upload a picture of a shoe (or shoes), and SneakPeek identifies the brand, style, make, and model of the shoe using three AI agents.
  - Once identified, SneakPeek links users to where they can purchase the sneakers online.

- **Multi-Agent AI System**

  - Google Gemini 2.0 Flash  
  - OpenAI GPT-4o  
  - Custom [AI-model](https://huggingface.co/eric-solak/ShoeClassificationAI), trained with a DenseNet201 architecture on [this dataset](https://www.kaggle.com/datasets/noobyogi0100/shoe-dataset/data) 
  - Agents iterate and compare predictions to finalize the best match.

- **Social Forum**
  
  - Users can create accounts, upload sneaker photos, comment, and rate posts.
  - See others’ shoes, opinions, and AI guesses.

## ⚙️ How It Works

1. User uploads an image via the app.
2. Image + optional description are sent via `POST` request to the backend.
3. AI agents (Gemini, GPT-4o, Custom Model) analyze the input.
4. Second initialization of Gemini selects the best result from agent responses.
5. App displays predicted shoe model with a purchase link

## 🛠️ Development

This is a **prototype**, intended for testing and demonstration purposes.

### Backend
The backend follows a Blackboard Architecture, where multiple AI agents (e.g., Gemini, GPT-4o, Custom Model) submit their predictions to a shared space. A central controller (Gemini) evaluates all suggestions and selects the most accurate result.
```angular2html
python3 backend/app.py
```

### Frontend
```angular2html
npx expo start
```

### Requirements
```angular2html
pip install -r requirements.txt
```
