from flask import Flask, request, render_template, jsonify
import os
import csv
from data_model import DataModel, load_excel_files

app = Flask(__name__)
data_model = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global data_model
    results = None
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        if search_term:
            results = data_model.query_like(search_term)
    return render_template('index.html', results=results)

@app.route('/load_data', methods=['POST'])
def load_data():
    global data_model
    excel_directory = request.json.get('directory')
    if excel_directory:
        data_model = load_excel_files(excel_directory)
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Directory not provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)