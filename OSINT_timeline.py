from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os
import re
from werkzeug.utils import secure_filename

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define items per page for pagination
ITEMS_PER_PAGE = 10

# URL validation regex
url_regex = re.compile(
    r'^(?:http|ftp)s?://'  # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
    r'localhost|'  # localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
    r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
    r'(?::\d+)?'  # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

# Allowed file extensions for images and videos
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    timelines = ['Timeline1', 'Timeline2']  # Mocked timeline list
    selected_timeline = request.args.get('selected_timeline')
    return render_template('index.html', timelines=timelines, selected_timeline=selected_timeline)


@app.route('/new_entry', methods=['POST'])
def new_entry():
    # Get form data
    date = request.form['date']
    time = request.form['time']
    location = request.form['location']
    source_link = request.form['source_link']

    # Validate source_link
    if not re.match(url_regex, source_link):
        flash('Invalid URL format.')
        return redirect(url_for('index'))

    # Validate image and video files
    image_file = request.files.get('image')
    video_file = request.files.get('video')

    if image_file and not allowed_file(image_file.filename):
        flash('Invalid image file format.')
        return redirect(url_for('index'))
    if video_file and not allowed_file(video_file.filename):
        flash('Invalid video file format.')
        return redirect(url_for('index'))

    # Save files securely
    if image_file:
        image_filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
    if video_file:
        video_filename = secure_filename(video_file.filename)
        video_file.save(os.path.join(app.config['UPLOAD_FOLDER'], video_filename))

    # Save the entry (mocked example)
    flash('Entry added successfully!')
    return redirect(url_for('index'))


@app.route('/query', methods=['POST', 'GET'])
def query():
    # Mock data for querying (replace with actual timeline data)
    results = ['Result1', 'Result2', 'Result3', 'Result4', 'Result5',
               'Result6', 'Result7', 'Result8', 'Result9', 'Result10',
               'Result11', 'Result12', 'Result13']  # Replace with actual query logic

    page = int(request.args.get('page', 1))
    start = (page - 1) * ITEMS_PER_PAGE
    end = start + ITEMS_PER_PAGE
    paginated_results = results[start:end]
    total_pages = (len(results) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE

    return render_template('query_results.html', query_result=paginated_results, page=page, total_pages=total_pages)


@app.route('/visualize')
def visualize():
    # This should render the basic visualization (static)
    return "Basic Visualization Page (To be implemented)"


@app.route('/visualize_relational')
def visualize_relational():
    # This should render the relational visualization (interactive)
    return "Relational Visualization Page (To be implemented)"


@app.route('/export', methods=['POST'])
def export():
    export_format = request.form['export_format']

    # Mock exporting logic based on format
    if export_format == 'csv':
        # Export logic for CSV
        return "Exported as CSV (To be implemented)"
    elif export_format == 'xls':
        # Export logic for Excel
        return "Exported as Excel (To be implemented)"
    elif export_format == 'pdf':
        # Export logic for PDF
        return "Exported as PDF (To be implemented)"

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

