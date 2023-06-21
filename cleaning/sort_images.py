import os
import pandas as pd

labels = pd.read_csv(
    "data/cleanedLabels/labels.txt",
    sep=";",
    names=["id", "verbose_label", "label"],
)

for id, label in zip(labels["id"], labels["label"]):
    os.system(f"cp data/cropedData/2mass/ngc{id}.png data/sortedData/2mass/{label}/{id}.png")
    os.system(f"cp data/cropedData/dss/ngc{id}.png data/sortedData/dss/{label}/{id}.png")
