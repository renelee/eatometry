import os
from flask import Flask, render_template, request, redirect, url_for
from flask import send_from_directory
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class, UploadNotAllowed
# from PIL import Image
import pytesseract

app = Flask(__name__)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/static/img'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

@app.route('/')
def home():
	return render_template('index.html')

'''
@app.route('/upload', methods=['POST'])
def get_ingredients_from_image():
	if request.method == 'POST':
		# if the request method is post, then we get the form image and unwanted ingredients
		path_to_image = request.form['image']
		ingredients = processList(pytesseract.image_to_string(Image.open(path_to_image)))
		unwanted_ingredients = set(processList(request.form['unwanted_ingredients']))
		results = []
		for u in unwanted_ingredients:
			if u in ingredients:
				results.append(u)
		return render_template('results.html', ingredients=results)
	return render_template('index.html')

def processList(s):
	return ...
	'''

@app.route('/upload', methods=['GET', 'POST'])
def upload():
	try: 
		if request.method == 'POST' and 'photo' in request.files:
			filename = photos.save(request.files['photo'])
			return render_template('upload.html', success=True)
	except UploadNotAllowed:
		return render_template('upload.html', success=False)

if __name__ == "__main__":
    app.run(debug=True)
