import os


# Resize 2mass images
print("Starting croping DSS images")
os.system(f"mogrify -shave '49x44' -path data/cropedData/dss data/rawData/dss/*.png")
print("DSS images finished croping.")

# Resize 2mass images
print("Starting croping 2mass images")
os.system(f"mogrify -shave '49x44' -path data/cropedData/2mass data/rawData/2mass/*.png")
print("2mass images finished croping.")