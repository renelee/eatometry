import os
from flask import Flask, render_template, request, redirect, url_for
from flask import send_from_directory
# from PIL import Image
import pytesseract

UPLOAD_FOLDER = '/uploads/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# function to get the unwanted ingredients from user
@app.route('/', methods=['POST'])
def my_form_post():
	text = request.form['text']
    # processed_text = text.upper()
    return processed_text


@app.route('/', methods=['POST'])
def get_ingredients_from_image(path_to_image):
	ingredients = pytesseract.image_to_string(Image.open(path_to_image))
	unwanted_ingredients = set(request.form['unwanted_ingredients'])
	results = []
	for u in unwanted_ingredients:
		if u in ingredients:
			results.append(u)
	return render_template('results.html', ingredients=results)




if __name__ == "__main__":
    app.run(debug=True)
