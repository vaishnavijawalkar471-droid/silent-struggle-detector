 🔍 Silent Struggle Detector

Silent Struggle Detector is a lightweight feedback analysis tool that uncovers hidden dissatisfaction in user reviews — situations where users give high ratings but express hesitation or uncertainty in their comments.

It helps teams catch what ratings alone fail to reveal.

💡 Problem Statement

User ratings can be misleading.

Many users rate products or services 4–5 stars out of politeness, while their written feedback contains phrases like:

“It was okay”

“Maybe”

“I guess”

“Could be better”

These silent struggles often go unnoticed, leading to:

Missed product insights

Unaddressed user concerns

Increased churn over time

🚀 Solution

A rule-based feedback classification system that combines:

⭐ Numerical ratings

📝 Textual hesitation cues

to flag feedback that appears positive on the surface but signals unresolved concerns.

✅ No black-box ML
✅ Fully explainable logic
✅ Fast and hackathon-ready

🧠 How It Works
Classification Rules
Category	Criteria
🟡 Silent Struggle	Rating ≥ 4 and comment contains vague or hesitant language
🔴 Strong Negative	Rating ≤ 2 with clear negative feedback
🟢 Clear Opinion	Confident positive or negative feedback

Hesitation cues include words such as:
okay, maybe, guess, fine, somewhat, not sure, etc.

🛠️ Tech Stack

Python

Streamlit

Pandas

Lightweight, fast, and easy to deploy.

🧪 Demo Flow

Upload a feedback CSV file

Automatically classify each entry

Highlight Silent Struggle cases

Download the analyzed dataset

⏱️ End-to-end flow completes in seconds.

📂 Input Format

The tool expects a CSV file with the following columns:

id | rating | comment | date


Sample data is included in the repository for quick testing.

🎯 Impact & Use Cases

Customer experience analysis

Product feedback monitoring

Survey and review analysis

Early detection of hidden dissatisfaction

Helps teams act before issues escalate.

🔮 Future Scope

Advanced NLP and sentiment analysis

Multi-language support

Real-time feedback ingestion

Integration with survey platforms (Google Forms, Typeform, etc.)

✅ Why This Project Stands Out

Explainable, rule-based logic

No heavy dependencies

Easy to demo and extend

Solves a real, overlooked problem

Built for hackathons. Designed for insight.
