import os
from flask import Flask, request, render_template
from werkzeug import secure_filename

from cutter import Cutter

knk = Cutter()

UPLOAD_FOLDER = './static/svg/'
ALLOWED_EXTENSIONS = set(['svg'])

app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/move', methods=['POST'])
def move():
	if(request.method == 'POST'):
		direction = request.form['direction']
		knk.move_direction(direction)
	return direction
	
@app.route('/cut', methods=['POST'])
def cut():
	if(request.method == 'POST'):
		knk.cut_file()
	return "cut"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploadajax', methods=['POST'])
def uploadajax():
	if request.method == 'POST':
		file = request.files['file_input']
		if file and allowed_file(file.filename):
			filename = 'pattern.svg'
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			output = knk.open_svg()
	return output

@app.route('/')
def root():
	return render_template('index.html')
	
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)