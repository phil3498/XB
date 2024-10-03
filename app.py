



from flask import Flask, render_template, request, redirect, url_for 
import os
from werkzeug.utils import secure_filename

app= Flask(__name__)

UPLOAD_FOLDER = 'static/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
 
    file = request.files['file']  
    filename = secure_filename(file.filename)     
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('uploaded_file', filename=filename))    

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded.html', filename=filename)

if __name__ =='__main__': 
    app.run(debug=True)





