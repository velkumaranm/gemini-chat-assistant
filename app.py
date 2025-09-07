from flask import Flask, render_template, make_response
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Flask app
app = Flask(__name__)

# Register Blueprints
from routes.chat import chat_bp
app.register_blueprint(chat_bp)

# Homepage route
@app.route('/')
def home():
    response = make_response(render_template('index.html'))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8000)