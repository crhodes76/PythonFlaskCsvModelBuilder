from flask import Flask, request, render_template
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
        excel_directory = request.form['directory']
        search_term = request.form['search_term']
        if data_model is None:
            data_model = load_excel_files(excel_directory)
        results = data_model.query_like(search_term)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)