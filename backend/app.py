from flask import Flask, jsonify
from flask_cors import CORS  # Thêm dòng này
import scenario1
import scenario2
import scenario3
import scenario4
import scenario5
import scenario6

app = Flask(__name__)
CORS(app)  # Thêm dòng này

@app.route('/run/<scenario>', methods=['GET'])
def run_scenario(scenario):
    if scenario == "scenario1":
        result = scenario1.run()
    elif scenario == "scenario2":
        result = scenario2.run()
    elif scenario == "scenario3":
        result = scenario3.run()
    elif scenario == "scenario4":
        result = scenario4.run()
    elif scenario == "scenario5":
        result = scenario5.run()
    elif scenario == "scenario6":
        result = scenario6.run()
    elif scenario == "all":
        result = "\n".join([
            scenario1.run(),
            scenario2.run(),
            scenario3.run(),
            scenario4.run(),
            scenario5.run(),
            scenario6.run()
        ])
    else:
        result = "Unknown scenario"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
