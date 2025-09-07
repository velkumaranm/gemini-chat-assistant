from flask import Blueprint, request, jsonify
import google.generativeai as genai

chat_bp = Blueprint('chat_bp', __name__)

# Load Gemini model (reuse from main app)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

@chat_bp.route('/generate', methods=['POST'])
def generate_response():
    try:
        user_input = request.json['prompt']
        print("📩 Received prompt:", user_input)

        response = model.generate_content(user_input)
        print("🤖 Gemini response:", response.text)

        return jsonify({'response': response.text})
    except Exception as e:
        print("❌ Error during Gemini response:", e)
        return jsonify({'response': f"⚠️ Gemini API error: {str(e)}"})