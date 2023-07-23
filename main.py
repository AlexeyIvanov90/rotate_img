import os
import cv2
import numpy as np
import csv


def is_png(file_name):
    if file_name.find(".png") == -1:
        return False
    return True


def add_rotate_img(paths, out_path):
    img_count = 0
    for path in paths:
        print(path.path)

        if is_png(path.path):
            img = cv2.imdecode(np.fromfile(path.path, dtype=np.uint8), cv2.IMREAD_COLOR)
            name = out_path + str(img_count) + '.png'
            cv2.imwrite(name, img)

            img = cv2.flip(img, 0)
            name = out_path + str(img_count + 1) + '.png'
            cv2.imwrite(name, img)

            img = cv2.flip(img, 1)
            name = out_path + str(img_count + 2) + '.png'
            cv2.imwrite(name, img)

            img = cv2.flip(img, 0)
            name = out_path + str(img_count + 3) + '.png'
            cv2.imwrite(name, img)
            img_count += 4


def delete_file_for_csv(path):
    with open(path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row[0])
            os.remove(str(row[0]))


data = os.scandir('D:/alex/Image_marker/dataRGB/clop')
path_to_save = 'D:/alex/rotate_img/test/'
path_csv_file = 'D:/alex/Image_marker/data_set/delete_data_set.csv'


add_rotate_img(data, path_to_save)

#delete_file_for_csv(path_csv_file)

