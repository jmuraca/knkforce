import os
from flask import Flask, request, render_template
from werkzeug import secure_filename
from Cutter import Cutter

UPLOAD_FOLDER = './static/svg/'
ALLOWED_EXTENSIONS = set(['svg'])

knk = Cutter()
dimensions = knk.load_file()

app = Flask(__name__, static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/dimensions', methods=['POST'])
def dimensions():
	if(request.method == 'POST'):
		dimensions = knk.display_dimensions()
	return dimensions

@app.route('/move', methods=['POST'])
def move():
	if(request.method == 'POST'):
		direction = request.form['direction']
		knk.move_direction(direction)
	return direction
	
@app.route('/cut', methods=['POST'])
def cut():
	if(request.method == 'POST'):
		knk.cut()
	return "cut"
	
@app.route('/setting', methods=['POST'])
def setting():
	if(request.method == 'POST'):
		setting = request.form['setting']
		value = request.form['value']
		knk.change_setting(setting, value)
	return "ok!"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploadajax', methods=['POST'])
def uploadajax():
	if request.method == 'POST':
		file = request.files['file_input']
		if file and allowed_file(file.filename):
			filename = 'pattern.svg'
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			knk.load_file(UPLOAD_FOLDER+filename)
			dimensions = knk.display_dimensions()
	return dimensions

@app.route('/')
def root():
	return render_template('index.html')
	
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80, debug=True)