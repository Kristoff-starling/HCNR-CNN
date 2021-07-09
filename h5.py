import os
import numpy as np
import cv2
import h5py
 
 
def save_image_to_h5py(path):
    img_list = []
    label_list = []
    dir_counter = 1
 
    for child_dir in os.listdir(path):
        print(child_dir)
        child_path = os.path.join(path, child_dir)
        num_for_test = 0
        for dir_image in os.listdir(child_path):

            img = cv2.imread(os.path.join(child_path, dir_image))
            img_list.append(img)
            label_list.append(dir_counter)

            if num_for_test > 800:
                break
            num_for_test = num_for_test + 1
 
        dir_counter += 1
 
    img_np = np.array(img_list)
    label_np = np.array(label_list)
 
    f = h5py.File('train.h5', 'w')
    f.create_dataset('train_set_x', data=img_np)
    f.create_dataset('train_set_y', data=label_np)
    f.close()
 
save_image_to_h5py('rawdata/train')