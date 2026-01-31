🤖 AI Chatbot using OpenAI API (Python)

This project is a simple command-line AI chatbot built using Python and the OpenAI API.
The chatbot takes user input from the terminal and generates intelligent responses using an OpenAI language model. The chat continues until the user types exit.

This project is beginner-friendly and helps understand API integration, Python scripting, and basic AI interaction.

📌 Features

Interactive terminal-based chatbot

Uses OpenAI language model for generating responses

Simple and clean Python code

Easy to understand and extend

🛠️ Technologies Used

Python 3

OpenAI Python SDK

📂 Project Structure
Agent_for_weather/
│── chatbot.py
│── README.md

▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/bavinkumar451/Agent_for_weather.git
cd Agent_for_weather

2️⃣ Install Required Package
pip install openai

3️⃣ Set OpenAI API Key (IMPORTANT)

❌ Do NOT hardcode your API key in the code

✅ Recommended way (Environment Variable):

Windows (Command Prompt):

set OPENAI_API_KEY=your_api_key_here


Linux / macOS:

export OPENAI_API_KEY="your_api_key_here"

4️⃣ Run the Chatbot
python chatbot.py

💬 Usage

Type your message and press Enter

The chatbot will respond

Type exit to stop the program

Example:

You: Hello
Chatbot: Hi! How can I help you today?

🔐 Security Note

⚠️ Never upload your OpenAI API key to GitHub
Always use environment variables to keep your key safe.

📚 Learning Outcomes

Understanding API-based AI communication

Using Python functions and loops

Building a real-world AI chatbot

Best practices for API key security

🚀 Future Improvements

Add web interface using Flask or FastAPI

Add conversation history

Improve error handling

Use newer OpenAI models

👤 Author

BAVIN
IT Student | Python & AI Enthusiast
