#!/usr/bin/env python3
import json
import random
import shutil
import os

# Load the original annotations JSON
with open('/mnt/c/mygit/DeepDataMiningLearning/DeepDataMiningLearning/data/annotations/instances_val2017.json') as file:
    data = json.load(file)

# Determine the subset size (1% of the images)
num_images = len(data['images'])
subset_size = int(num_images * 0.05)

# Randomly select the subset of images
selected_images = random.sample(data['images'], subset_size)

# Extract IDs for these images
selected_image_ids = {img['id'] for img in selected_images}

# Extract corresponding annotations
selected_annotations = [anno for anno in data['annotations'] if anno['image_id'] in selected_image_ids]

# Save the new subset JSON
subset_data = {
    'images': selected_images,
    'annotations': selected_annotations,
    'categories': data['categories']
}
with open('/mnt/c/mygit/DeepDataMiningLearning/DeepDataMiningLearning/data/annotations/instances_subval2017.json', 'w') as outfile:
    json.dump(subset_data, outfile)

# Directory paths for images
source_directory = '/mnt/c/mygit/DeepDataMiningLearning/DeepDataMiningLearning/data/val2017/'
destination_directory = '/mnt/c/mygit/DeepDataMiningLearning/DeepDataMiningLearning/data/test_subset_images/'

# Ensure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Copy selected image files
for img in selected_images:
    source_path = os.path.join(source_directory, img['file_name'])
    destination_path = os.path.join(destination_directory, img['file_name'])
    shutil.copy(source_path, destination_path)
