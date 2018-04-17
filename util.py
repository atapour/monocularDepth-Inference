from __future__ import print_function
import torch
import numpy as np
from PIL import Image
import os
# from scipy.misc import imresize
import ntpath
import cv2

# Converts a Tensor into a Numpy array
# |imtype|: the desired type of the converted numpy array
def tensor2im(image_tensor):
    image_numpy = image_tensor[0].cpu().float().numpy()
    if image_numpy.shape[0] == 3:
        image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 255.0
        return image_numpy.astype(np.uint8)

    elif image_numpy.shape[0] == 1:
        print(image_numpy.shape)
        image_numpy = (np.transpose(image_numpy, (1, 2, 0)) + 1) / 2.0 * 65535.0
        return image_numpy.astype(np.uint16)




def diagnose_network(net, name='network'):
    mean = 0.0
    count = 0
    for param in net.parameters():
        if param.grad is not None:
            mean += torch.mean(torch.abs(param.grad.data))
            count += 1
    if count > 0:
        mean = mean / count
    print(name)
    print(mean)


def save_image_color(image_numpy, image_path):
    image_numpy = image_numpy.astype(np.uint8)

    image_pil = Image.fromarray(image_numpy)
    # print (image_numpy.dtype)

    image_pil.save(image_path)
def save_image_depth(image_numpy, image_path):
    # print (image_numpy.dtype)

    cv2.imwrite(image_path,image_numpy)


def print_numpy(x, val=True, shp=False):
    x = x.astype(np.float64)
    if shp:
        print('shape,', x.shape)
    if val:
        x = x.flatten()
        print('mean = %3.3f, min = %3.3f, max = %3.3f, median = %3.3f, std=%3.3f' % (
            np.mean(x), np.min(x), np.max(x), np.median(x), np.std(x)))


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

    ims = []
    txts = []
    links = []

    for label, im in visuals.items():

        image_name = '%s_%s.png' % (name, label)
        save_path = os.path.join(image_dir, image_name)
        h, w, _ = im.shape
        if size!=None:
            #im = imresize(im, (size[1], size[0]), interp='bilinear')
            im = cv2.resize(im, size)
        print (im.dtype)


        if label == 'fake_C':
            save_image_depth(im, save_path)
        else:
            save_image_color(im, save_path)


        ims.append(image_name)
        txts.append(label)
        links.append(image_name)