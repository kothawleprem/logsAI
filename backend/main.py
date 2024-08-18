from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from utils.file_parser import allowed_file, parse_log_file
# from utils.ai_service import analyze_log

app = Flask(__name__)
CORS(app)


UPLOAD_FOLDER = 'logs/'

# Route to upload the logfile
@app.route('/api/upload', methods=['POST'])
def upload_file():
    # return jsonify({"resp": "hiii"})
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "file_path": file_path}), 200
    return jsonify({"error": "File type not allowed"}), 400



# Route to analyze the logfile
@app.route('/api/analyze', methods=['POST'])
def analyze_file():
    data = request.json
    if not data or 'file_path' not in data:
        return jsonify({"error": "File path is missing"}), 400
    file_path = data['file_path']
    if not os.path.exists(file_path):
        return jsonify({"error": "File does not exist"}), 404

    content = parse_log_file(file_path)
    # ai_result = analyze_log(content)
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True)
