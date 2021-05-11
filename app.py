from flask import Flask, render_template, request, session, redirect, url_for
import os
import visualization as viz

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def index():

    if 'filename' in session and 'filepath' in session:
        filepath = session['filepath']
        filename = session['filename']
    else:
        filepath = None
        filename = "Choose image"
        
    return render_template("index.html", filename=filename, filepath=filepath)
 
@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            filename = image.filename
            print(len(filename))
            if (len(filename) > 0):
                filepath = os.path.join('static/img/', image.filename)
                image.save(filepath)

                session["filepath"] = filepath
                session["filename"] = filename
    
    return redirect(url_for('index'))


@app.route("/detect/", methods=["POST"])
def start_detection():

    if request.method == "POST":
        if 'filename' in session and 'filepath' in session:
            filepath = session['filepath']
            viz.detect_img(filepath)

    return redirect(url_for('index'))


# No caching at all for API endpoints.
@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)