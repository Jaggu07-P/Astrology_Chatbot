# 🔮 Astrology Chatbot with Gemini 1.5 Flash & Aztro API

A chat-based astrology assistant that allows users to input their date, time, and place of birth, then ask personalized horoscope questions. Uses Aztro API for horoscope data and Gemini 1.5 Flash for natural language interpretation.

---

## ✨ Features

- User-friendly web interface (HTML/CSS + Flask backend)
- Fetches real-time horoscope data using Aztro API
- Interprets results using Gemini 1.5 Flash (Google Generative AI)
- Fallback to LLM if API fails or is unreachable
- Input validation for date, time, and location
- Option to ask specific questions (e.g., *"What will my day be like?"*)

---

## 🔧 Tech Stack

- Python (Flask)
- HTML/CSS
- Aztro API (Free horoscope data)
- Google Gemini 1.5 Flash (via `google-generativeai`)
- Hosted on Heroku (optional)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/astrology-chatbot.git
cd astrology-chatbot
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your API Keys

Edit `utils/llm_interpreter.py` and replace:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

(You don’t need an API key for Aztro API.)

---

## 🧪 Running the App

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

---

## ☁️ Deployment (Heroku)

1. Create a `Procfile` with this content:

```
web: python app.py
```

2. Add `requirements.txt`:

```bash
pip freeze > requirements.txt
```

3. Push to Heroku:

```bash
heroku login
heroku create astrology-chatbot-app
git add .
git commit -m "Initial commit"
git push heroku main
heroku open
```

---

## 📁 Project Structure

```
astrology-chatbot/
│
├── app.py
├── templates/
│   └── index.html
├── utils/
│   ├── astrology_api.py
│   └── llm_interpreter.py
├── static/ (optional for CSS/JS)
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🎥 Demo

_A 1–2 minute video demonstrating the form input, horoscope fetch, and Gemini interpretation._

---

## 📌 Notes

- Aztro API only supports Sun sign-based horoscopes.
- If Aztro fails, Gemini 1.5 Flash provides fallback response.

---

## 🙋‍♂️ Author

Jagannath Panigrahi  
jagannathms07@gmail.com
