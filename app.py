from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
items = []  # In-memory storage

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image = request.files['image']
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)

        items.append({
            'name': name,
            'description': description,
            'image': image.filename
        })
        return redirect(url_for('index'))
    return render_template('report.html')

if __name__ == '__main__':
    app.run(debug=True)
