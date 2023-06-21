import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import os
import sys


print("\nLoading classifier model")

model = keras.models.load_model('data/trained_model')

if len(sys.argv) < 2:
    image_path = input("Provide image path:")
else:
    image_path = sys.argv[1]

print(f"\nLoading image '{image_path}'")

image = keras.utils.load_img(image_path)

resized_image = keras.preprocessing.image.smart_resize(image, (161, 161))

img_array = keras.utils.img_to_array(resized_image)
img_array = tf.expand_dims(img_array, 0)  # Create batch axis


predictions = model.predict(img_array)
score = float(predictions[0])
label = f"galaxy: {100 * (1 - score):.2f}% \nopen cluster: {100 * score:.2f}%"
plt.imshow(img_array[0] / 255)
plt.axis('off')
plt.title(label)
plt.show()

print(label)
