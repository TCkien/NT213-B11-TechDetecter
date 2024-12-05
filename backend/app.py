from flask import Flask, request, jsonify
from flask_cors import CORS
import cms_detection
import backend_framework_detection
import javascript_library_detection
import web_server_detection
import ssl_fingerprint_analysis
import api_path_analysis

app = Flask(__name__)
CORS(app)

@app.route('/run', methods=['POST'])
def run_function():
    data = request.json
    url = data.get('url', '')
    function = data.get('function', '')

    if not url:
        return jsonify({"error": "URL is required"}), 400

    if function == "detect_cms":
        result = cms_detection.run(url)
    elif function == "detect_backend_framework":
        result = backend_framework_detection.run(url)
    elif function == "detect_js_libraries":
        result = javascript_library_detection.run(url)
    elif function == "detect_web_server":
        result = web_server_detection.run(url)
    elif function == "analyze_ssl_fingerprint":
        result = ssl_fingerprint_analysis.run(url)
    elif function == "analyze_api_paths":
        result = api_path_analysis.run(url)
    elif function == "all":
        result = "\n".join([
            cms_detection.run(url),
            backend_framework_detection.run(url),
            javascript_library_detection.run(url),
            web_server_detection.run(url),
            ssl_fingerprint_analysis.run(url),
            api_path_analysis.run(url)
        ])
    else:
        result = "Unknown function"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
