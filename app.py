




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

static

uploaded.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Uploaded Image</title>
</head>
<body>
    <h1>Uploaded Image</h1>
  
    <p>
        <img src="{{ url_for('static', filename=filename) }}"alt="Uploaded image">
    </p>
   
</body>
</html



index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Image</title>
</head>
<body>
    <h1>Upload Image</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*">
        <input type="submit" value="Upload">
    </form>
</body>
</html>





