# Chat bot application

# Features

-> Interactive Q&A Interface: Users can input questions and receive responses in real-time.
-> Session Management: The chat history is managed within the session, allowing users to see past interactions.
-> Environment Variable Management: Sensitive information such as API keys are managed via environment variables for security.

# Memory Optimization

-> Chat History Management: The application maintains a cap on the number of chat entries stored, limiting it to the 20 most recent interactions. This prevents memory bloat over time by discarding older entries.

-> Garbage Collection: Python’s garbage collection is invoked explicitly after significant memory-intensive operations to free up unused memory, ensuring that the application remains efficient across multiple sessions.

# How It Works

-> Input Questions: Users enter their questions into the text input box.
-> Get Responses: Upon submitting the question, the application processes the input using the Gemini Pro model and displays the response.
-> View Chat History: The chat history is displayed below the response area, showing a record of the interaction within the session.

# For starting the app

1. Env setup
   python -m venv myenv
   Create a .env file in the root directory of the project.
   Add the following line, replacing <your_google_api_key> with your actual API key:
2. activate the environment
   myenv\Scripts\activate
3. Install the required packages
   pip install -r requirements.txt
4. Run the app
   streamlit run app.py
