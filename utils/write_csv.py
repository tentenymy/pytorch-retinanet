import os
import pandas as pd
import numpy as np

label_dir_path = '/Users/meiyiyang/Downloads/train_labeled'
image_dir_path = '/Users/meiyiyang/Downloads/train'


image_no_list = []
bbox_list = []
for tag in os.listdir(label_dir_path):
	if tag == '.DS_Store':
		continue

	label_path = os.path.join(label_dir_path, tag)
	with open(label_path) as file:
		lines = file.read().split('\n')
		bbox = [0, 0, 0, 0]
		for i, line in enumerate(lines):
			if line == '        <bndbox>':
				xmin_str = lines[i + 1].replace('            <xmin>', '')
				bbox[0] = int(xmin_str.replace('</xmin>', '')) - 1

				ymin_str = lines[i + 2].replace('            <ymin>', '')
				bbox[1] = int(ymin_str.replace('</ymin>', '')) - 1

				xmax_str = lines[i + 3].replace('            <xmax>', '')
				bbox[2] = int(xmax_str.replace('</xmax>', '')) - 1

				ymax_str = lines[i + 4].replace('            <ymax>', '')
				bbox[3] = int(ymax_str.replace('</ymax>', '')) - 1

				print(bbox)
				break

	# read to list
	tag = tag.replace('.xml', '.jpg')
	image_no_list.append(tag)
	bbox_list.append(bbox)

# read to csv
bbox_matrix = np.array(bbox_list)
label_list = [0 for i in range(bbox_matrix.shape[0])]
print("bbox: ", bbox_matrix.shape)

data_train = pd.DataFrame(data={
	'col0': image_no_list[0:360],
	'col1': bbox_matrix[0:360, 0],
	'col2': bbox_matrix[0:360, 1],
	'col3': bbox_matrix[0:360, 2],
	'col4': bbox_matrix[0:360, 3],
	'col5': 0
})

print(data_train.head())
data_train.to_csv("label_whale_train.csv", header=False, index=False)

data_test = pd.DataFrame(data={
	'col0': image_no_list[360:],
	'col1': bbox_matrix[360:, 0],
	'col2': bbox_matrix[360:, 1],
	'col3': bbox_matrix[360:, 2],
	'col4': bbox_matrix[360:, 3],
	'col5': 0
})

print(data_test.head())
data_test.to_csv("label_whale_test.csv", header=False, index=False)