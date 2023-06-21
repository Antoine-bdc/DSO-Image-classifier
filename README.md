# Deep Space Object Classifier

## Description

This project aims to create a model classifying Deep Space Objects (DSO) images. In order to do so, it scrapes image and label data from `https://simbad.u-strasbg.fr`. Then trains a deep learning model to classify between the two most prominent classes: Galaxies and open clusters.

## How to run

Run data scrappers: 
```bash
node scrapping/dataScrapper.js
node scrapping/labelScrapper.js
```

Clean the data:
```bash
python cleaning/cleaning_labels.py
python cleaning/crop_images.py
python cleaning/sort_images.py
```

Train the model:
Run through the `learning/learning.ipynb` notebook.

The model is then saved in the `data/trained_model` directory

## How to use

You can use the classifier on images stored locally on your machine using the `learning/classifier.py` script and providing the path to your image.

```bash
python learning/classifier.py data/cropedData/dss/ngc222.png
```

## License

All code written in this repository is published as GPL License
