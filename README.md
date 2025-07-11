 <h1><mark> <i> Nlp-Web-app <i> <mark></h1>

<h1>🧠 LP Web App – Sentiment Analysis & Named Entity Recognition</h1>

A **full-stack Natural Language Processing web application** built using **Flask, HuggingFace Transformers, HTML, and CSS**.  
It allows users to log in securely and analyze text for **sentiment** (positive, neutral, negative) and **named entities** (person, location, organization, etc.) in real time.

---

🚀 Key Highlights

- 🔐 **User Authentication** — Secure Register & Login with Flask Sessions
- 💬 **Sentiment Analysis** — Instantly detect emotions in any sentence
- 🧠 **Named Entity Recognition (NER)** — Extract names, places, brands, dates & more
- 📡 **Real-time NLP via HuggingFace API**
- 🎯 Clean, intuitive UI — recruiter-ready presentation

---

👨‍💻 Skills Demonstrated

| Area              | What I Used                            |
|-------------------|-----------------------------------------|
| Backend           | Python, Flask, Routing, Session Mgmt    |
| Frontend          | HTML, CSS, Templates (Jinja2)           |
| API Integration   | HuggingFace Transformers Inference API  |
| Authentication    | Custom user login & register logic      |
| State Handling    | Flask `session[]` for login persistence |
| Code Management   | Modular, production-ready structure     |

---

🎯 Why I Built This

> To demonstrate my ability to build a **real-world AI-powered web app** from scratch — including authentication, API integration, and meaningful UI/UX.  
It reflects my ability to think **end-to-end** like a full-stack engineer.

Screenshot 

<video src=https://github.com/user-attachments/assets/ba15aff3-89e6-4c79-95f8-68978d5ef261 controls autoplay  height ="500px" width="700px">Coudnt load Thsi Time<


⚙️ How to Run Locally

1. Clone the Repo

```bash
git clone https://github.com/your-username/nlp-web-app.git
cd nlp-web-app

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Add HuggingFace API Token
Open app.py and replace this:

"Authorization": "Bearer YOUR_TOKEN"

💬 Sample Use Cases
I love this course! → 😊 POSITIVE

Barack Obama was born in Hawaii. → Extracts PERSON + LOCATION

💡 Future Improvements
Add Text Summarization feature

Use SQLite/PostgreSQL for user database
