import os
from flask import Flask, request, render_template
from werkzeug import secure_filename

from cutter import Cutter

knk = Cutter()

UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['svg'])

app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/move')
def move():
	if(request.method == 'GET'):
		direction = request.args.get('direction')
		knk.move_direction(direction)
	return direction

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploadajax', methods=['GET', 'POST'])
def uploadajax():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	return 'hello'

@app.route('/')
def root():
	return render_template('index.html')
	
if __name__ == '__main__':
  app.run(debug=True)