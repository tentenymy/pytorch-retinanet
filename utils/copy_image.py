import pandas as pd
import shutil
import os

image_dir_path = '/Users/meiyiyang/Downloads/train'
data_train = pd.read_csv("label_whale_test.csv", header=None)
print(data_train.head())

for path in data_train[0]:
	print(path)
	image_name = path.split('/')[-1]
	shutil.copy(
		os.path.join(image_dir_path, image_name),
		"test/" + image_name
	)