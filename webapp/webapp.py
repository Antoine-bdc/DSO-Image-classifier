import os
import uuid
import urllib
import tensorflow as tf
from tensorflow import keras
from flask import Flask, render_template, request


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = keras.models.load_model('../data/trained_model')
INDEX_PATH = "index.html"
SUCCESS_PATH = "success.html"

ALLOWED_EXT = set(['jpg', 'jpeg', 'png', 'jfif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXT


classes = ['open cluster', 'galaxy']


def predict(filename, model):

    image = keras.utils.load_img(filename)

    resized_image = keras.preprocessing.image.smart_resize(image, (161, 161))

    img_array = keras.utils.img_to_array(resized_image)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = model.predict(img_array)
    result = float(predictions[0])

    if result < 0.5:
        class_result = [classes[0], classes[1]]
    else:
        class_result = [classes[1], classes[0]]

    prob_result = [
        round(result * 100, 2),
        round((1 - result) * 100, 2),
    ]

    print(prob_result)

    return class_result, prob_result


@app.route('/')
def home():
    return render_template(INDEX_PATH)


@app.route('/success', methods=['GET', 'POST'])
def success():
    error = ''
    target_img = os.path.join(os.getcwd(), 'static/images')
    if request.method == 'POST':
        if (request.form):
            link = request.form.get('link')
            try:
                resource = urllib.request.urlopen(link)
                unique_filename = str(uuid.uuid4())
                filename = unique_filename+".jpg"
                img_path = os.path.join(target_img, filename)
                output = open(img_path, "wb")
                output.write(resource.read())
                output.close()
                img = filename

                class_result, prob_result = predict(img_path, model)

                predictions = {
                    "class1": class_result[0],
                    "class2": class_result[1],
                    "prob1": prob_result[0],
                    "prob2": prob_result[1],
                }

            except Exception as e:
                print(str(e))
                error = 'This image from this site is not accesible or inappropriate input'

            if (len(error) == 0):
                return render_template(SUCCESS_PATH, img=img, predictions=predictions)
            else:
                return render_template(INDEX_PATH, error=error) 

        elif (request.files):
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(os.path.join(target_img, file.filename))
                img_path = os.path.join(target_img, file.filename)
                img = file.filename

                class_result, prob_result = predict(img_path, model)

                predictions = {
                    "class1": class_result[0],
                    "class2": class_result[1],
                    "prob1": prob_result[0],
                    "prob2": prob_result[1],
                }

            else:
                error = "Please upload images of jpg, jpeg and png extension only"

            if (len(error) == 0):
                return render_template(SUCCESS_PATH, img=img, predictions=predictions)
            else:
                return render_template(INDEX_PATH, error=error)

    else:
        return render_template(INDEX_PATH)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
