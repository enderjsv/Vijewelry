import os
from flask import Flask, flash, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename

def allowed_file(filename,allowed_extensions):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions


def upload_file():

    allowed_extensions = {'jpg'}

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = r"website\static\images"
    
    return_page = 'admin.html'

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file',category="error")
            return render_template(return_page)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file',category="error")
            return render_template(return_page)
        if not allowed_file(file.filename,allowed_extensions):
            flash('Incorrect File Type',category="error")
            return render_template(return_page)
        if file:
            filename = secure_filename(file.filename)
            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename).replace('\\','/'))
            flash('File Saved',category="success")
            return render_template(return_page)

    return render_template(return_page)
