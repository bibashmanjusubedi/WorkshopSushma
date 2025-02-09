import cv2
import time
import numpy as np

# importing algorithms
from PCA import pca_class

import os

# Ensure the 'output' directory exists, create it if not
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# importing feature extraction classes
from images_to_matrix import images_to_matrix_class
# from images_matrix_for_2d_square_pca import  images_to_matrix_class_for_two_d
from dataset import dataset_class

# Algo Type
algo_type = "pca"


reco_type = 0

#No of images For Training(Left will be used as testing Image)
no_of_images_of_one_person = 8
dataset_obj = dataset_class(no_of_images_of_one_person)


#Data For Training
images_names = dataset_obj.images_name_for_train
y = dataset_obj.y_for_train
no_of_elements = dataset_obj.no_of_elements_for_train
target_names = dataset_obj.target_name_as_array

#Data For Testing
images_names_for_test = dataset_obj.images_name_for_test
y_for_test = dataset_obj.y_for_test
no_of_elements_for_test = dataset_obj.no_of_elements_for_test


training_start_time = time.process_time()
img_width, img_height = 50, 50

if algo_type == "pca":
    i_t_m_c = images_to_matrix_class(images_names, img_width, img_height)

scaled_face = i_t_m_c.get_matrix()


original_idx = 1

if algo_type == "pca":
    original_image = np.reshape(scaled_face[:, original_idx], [img_height, img_width])
    cv2.imshow("Original Image", cv2.resize(original_image.astype(np.uint8), (200, 200)))
    cv2.waitKey()
    original_image_path = os.path.join(output_dir, "original_image.jpg")
    # Save the original image in JPG format
    cv2.imwrite(original_image_path, np.array(original_image, dtype=np.uint8))

#Algo
if algo_type == "pca":
    my_algo = pca_class(scaled_face, y, target_names, no_of_elements, 70)



new_coordinates = my_algo.reduce_dim()


if algo_type == "pca":
    
    after_pca_image = my_algo.original_data(new_coordinates[original_idx, :])
    after_pca_image = np.reshape(after_pca_image, [img_height, img_width])
    cv2.imshow("After PCA Image", cv2.resize(after_pca_image.astype(np.uint8), (200, 200)))
    cv2.waitKey()
    afterpca_image_path = os.path.join(output_dir, "after_pca_image.jpg")
    # Save the after PCA image in JPG format
    cv2.imwrite(afterpca_image_path, np.array(after_pca_image, dtype=np.uint8))
    


training_time = time.process_time() - training_start_time






