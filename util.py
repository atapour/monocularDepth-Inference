from __future__ import print_function
import torch
import numpy as np
from PIL import Image
import os
import ntpath
import cv2

def tensor2im(image_tensor):
    image_numpy = image_tensor[0].cpu().float().numpy()
    if image_numpy.shape[0] == 3:
        image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 255.0
        return image_numpy.astype(np.uint8)

    elif image_numpy.shape[0] == 1:
        image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 65535.0
        return image_numpy.astype(np.uint16)

def save_image_color(image_numpy, image_path):
    image_numpy = image_numpy.astype(np.uint8)
    image_pil = Image.fromarray(image_numpy)
    image_pil.save(image_path)

def save_image_depth(image_numpy, image_path):
    cv2.imwrite(image_path,image_numpy)

def mkdirs(paths):
    if isinstance(paths, list) and not isinstance(paths, str):
        for path in paths:
            mkdir(path)
    else:
        mkdir(paths)

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def save_images(results_dir, visuals, image_path, size=None):
    image_dir = results_dir
    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    short_path = ntpath.basename(image_path[0])
    name = os.path.splitext(short_path)[0]

    for label, im in visuals.items():

        image_name = '%s_%s.png' % (name, label)
        save_path = os.path.join(image_dir, image_name)
        h, w, _ = im.shape
        if size!=None:
            im = cv2.resize(im, size)

        if label == 'fake_C':
            save_image_depth(im, save_path)
        else:
            save_image_color(im, save_path)