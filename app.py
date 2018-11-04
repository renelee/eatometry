import os
from flask import Flask, render_template, request, redirect, url_for
from flask import send_from_directory
# from PIL import Image
import pytesseract

UPLOAD_FOLDER = '/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
	return render_template('index.html')

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
	return 

if __name__ == "__main__":
    app.run(debug=True)
