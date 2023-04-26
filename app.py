from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/excel-to-json', methods=['POST'])
def excel_to_json():
    excel_file = request.files['file']
    if not excel_file:
        return jsonify({'error': 'No file provided'})

    # Read Excel data
    data = pd.read_excel(excel_file)
    # Convert to JSON
    json_data = data.to_dict(orient='records')

    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
