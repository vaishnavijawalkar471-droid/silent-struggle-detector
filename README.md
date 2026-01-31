 🔍 Silent Struggle Detector

Silent Struggle Detector identifies hidden dissatisfaction in user feedback — cases where users give high ratings but use hesitant or vague language, signaling unresolved concerns.

💡 Problem

User ratings alone are misleading.

Many users give 4–5 stars out of politeness but express uncertainty through words like “okay”, “maybe”, or “I guess”.
These silent struggles often go unnoticed, leading to churn and missed insights.

🚀 Solution

A rule-based feedback analysis tool that flags Silent Struggle cases by combining:

Numerical ratings

Textual hesitation cues

The approach is simple, transparent, and easy to explain — no black-box ML.

🧠 How It Works
Classification Rules

🟡 Silent Struggle

Rating ≥ 4

Comment contains vague or hesitant language

🔴 Strong Negative

Rating ≤ 2

Clear negative feedback

🟢 Clear Opinion

Confident positive or negative feedback

🛠️ Tech Stack

Python

Streamlit

Pandas

Lightweight, fast, and hackathon-ready.

🧪 Demo Flow

Upload a feedback CSV

View auto-classified results

Identify Silent Struggle cases

Download analyzed data

End-to-end flow in seconds.

📂 Input Format

CSV with the following columns:

id | rating | comment | date

Sample data included for quick testing.

🎯 Impact & Use Cases

Customer experience analysis

Product feedback monitoring

Survey and review analysis

Early detection of hidden dissatisfaction

Helps teams act before issues escalate.

🔮 Future Scope

Advanced NLP / sentiment analysis

Multi-language support

Real-time feedback streams

Integrations with survey platforms

✅ Why This Stands Out

Explainable logic

No heavy dependencies

Easy to demo

Solves a real, overlooked problem

Built for hackathons. Designed for insight.