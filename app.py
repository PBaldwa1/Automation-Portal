from flask import Flask, request, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(filepath)

        # Process: Make headers uppercase
        df = pd.read_excel(filepath)
        df.columns = [col.upper() for col in df.columns]

        output_file = os.path.join(UPLOAD_FOLDER, f'processed_{uploaded_file.filename}')
        df.to_excel(output_file, index=False)

        return send_file(output_file, as_attachment=True)

    return render_template('index.html')
