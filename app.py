from flask import Flask, render_template, request
from tensorflow import keras

import cv2
import numpy as np
import pandas as pd

app = Flask(__name__)

kotha = keras.models.load_model('kotha_explicittttt/')
print("+"*50, "Model is loaded")

labels = pd.read_csv("labels.txt", sep="\r\n").values

@app.route('/')
def index():
	return render_template("index.html", data="hey")


@app.route("/prediction", methods=["POST"])
def prediction():

	img = request.files['img']

	img.save("img.jpg")

	image = cv2.imread("img.jpg")

	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	image = cv2.resize(image, (224,224))

	image = np.reshape(image, (1,224,224,3))

	pred = kotha.predict(image)

	pred = np.argmax(pred)

	pred = labels[pred]

	return render_template("prediction.html", data=pred)


if __name__ == "__main__":
	app.run(debug=True)
