from flask import Blueprint, request, jsonify
import google.generativeai as genai

chat_bp = Blueprint('chat_bp', __name__)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def format_response(text):
    lines = text.strip().split('\n')
    formatted = ""
    for line in lines:
        if line.strip().startswith(('1.', '2.', '3.', '4.', '•', '-')):
            formatted += f"<li>{line.strip()}</li>"
        else:
            formatted += f"<p>{line.strip()}</p>"
    return f"<ul>{formatted}</ul>" if "<li>" in formatted else formatted

@chat_bp.route('/generate', methods=['POST'])
def generate_response():
    try:
        user_input = request.json['prompt']
        response = model.generate_content(user_input)
        formatted = format_response(response.text)
        return jsonify({'response': formatted})
    except Exception as e:
        return jsonify({'response': f"<p>⚠️ Gemini API error: {str(e)}</p>"})