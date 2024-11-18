# Flask app to handle backend API and interactions
import sys
import os

# Add the parent directory or the directory containing ai_tutor to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ai_tutor')))


from flask import Flask, request, jsonify
from ai_tutor.content_processor import extract_text_from_pdf, process_content
from ai_tutor.quiz_generator import generate_quiz


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload, process content, and generate quiz."""
    file = request.files['file']
    file_path = f"uploads/{file.filename}"
    file.save(file_path)

    content = extract_text_from_pdf(file_path)
    processed_content = process_content(content)
    quiz = generate_quiz(processed_content)

    return jsonify({"quiz": quiz})

if __name__ == '__main__':
    app.run(debug=True)
