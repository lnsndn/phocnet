import os
import pprint

import numpy as np
from PIL import Image


def summarize_images():
    image_sizes = {}
    amount_images = 0

    for (dirpath, dirnames, filenames) in os.walk('/Users/lena/Downloads/SHIBR_6GB/eval/images'):
        for f in filenames:
            if f.endswith('.jpg'):
                amount_images += 1
                image_name = os.path.join(dirpath, f)
                image_arr = Image.open(image_name)
                size = image_arr.size
                if size in image_sizes:
                    image_sizes[size] += 1
                else:
                    image_sizes[size] = 1

    pp = pprint.PrettyPrinter()
    pp.pprint(image_sizes)
    print("Amount of images: " + str(amount_images))


def produce_patches():
    image = Image.open('/Users/lena/Downloads/SHIBR_6GB/eval/images/43878/v43878.b19.s29.jpg')
    image_arr = np.asarray(image)
    patch_size = (200, 100)
    step_size = 50

    output_dir = 'patches'
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    patches = []
    for y in range(0, image.size[1], step_size):
        for x in range(0, image.size[0], step_size):
            left = x
            top = y
            right = x + patch_size[0]
            bottom = y + patch_size[1]
            im2 = image.crop((left, top, right, bottom))
            im2.save(os.path.join(output_dir, str(x) + "_" + str(y) + ".jpg"), "JPEG")
    
produce_patches()