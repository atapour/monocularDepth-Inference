# Real-Time Monocular Depth Estimation using Synthetic Data with Domain Adaptation via Image Style Transfer

Requires an NVIDIA GPU, Python 2 or 3, [CUDA CuDNN](https://developer.nvidia.com/cudnn), [PyTorch 0.3.1](https://pytorch.org/previous-versions/) or [PyTorch 0.4.0](http://pytorch.org), and [OpenCV](http://www.opencv.org),

![General Pipeline](https://github.com/atapour/styleDepth-Inference/blob/master/imgs/pipeLine.png)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;General pipeline of the approach
## Method:

_"Monocular depth estimation using learning-based approaches has become relevant and promising in recent years. However, most monocular depth estimators either need to rely on large quantities of ground truth depth data, which is extremely expensive and difficult to obtain or predict disparity as an intermediary step using a secondary supervisory signal, leading to blurring and other artefacts. Training a depth estimation model using pixel-perfect synthetic environment data can resolve most of these issues, but introduces the problem of domain bias. This is the inability
to apply a model trained on synthetic data to real-world scenarios. With recent advances in image style transfer and its connections with domain adaptation (Maximum Mean Discrepancy), our approach takes advantage of style transfer and adversarial training to predict pixel perfect depth from
a single real-world color image based on training over a large corpus of synthetic environment data. Experimental results indicate the efficacy of our approach compared to contemporary state-of-the-art."_

[[Atapour-Abarghouei and Breckon, Proc. CVPR, 2018](http://breckon.eu/toby/publications/papers/abarghouei18monocular.pdf)]

---

## Reference implementation:
Produces a depth map output image based on a monocular color image input.
* The input RGB image will first be transformed into the style of the images captured from a highly realistic synthetic virtual environment, on which the depth prediction network is trained.
* The provided color image is used as the input to [CycleGAN](https://junyanz.github.io/CycleGAN/), which transforms the style of the image. Image style transfer is used as a method of domain adaptation.
* The style transferred image is used as the input to a model trained on synthetic images and can produce pixel-perfect depth outputs.
* The code provides an inference pipeline and can be run using the test harness: run_test.py
* Example images are provided in the 'Examples' directory.
* The training was in part performed based on the code from [https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix), and we would like to thank the authors and contributors.


![](https://github.com/atapour/styleDepth-Inference/blob/master/imgs/sample.png)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Example of the results of the approach

---
## Instructions to run the inference code using PyTorch 0.3.1:

```
$ git clone https://github.com/atapour/monocularDepth-Inference.git
$ cd monocularDepth-Inference
$ chmod +x ./download_pretrained_models.sh
$ ./download_pretrained_models.sh
$ python run_test.py --data_directory=./Examples --checkpoints_dir=./checkpoints --results_dir=./results
```
---
## Instructions to run the inference code using PyTorch 0.4.0:

```
$ git clone https://github.com/atapour/monocularDepth-Inference.git
$ cd monocularDepth-Inference
$ chmod +x ./download_pretrained_models.sh
$ ./download_pretrained_models.sh
$ python remove_running_stats.py
$ python run_test.py --data_directory=./Examples --checkpoints_dir=./checkpoints --results_dir=./results
```
---

The output results are written in a directory taken as an argument to the test harness ('./results' by default):
* the script entitled "download_pretrained_models.sh" will download the required pre-trained models and checks the downloaded file integrity using MD5 checksum.
* the checkpoints that are available for direct download were created using pyTorch 0.3.1 and will not work if you are using pyTorch 0.4.0. The provided python script named ' remove_running_stats.py' will remedy the situation.
* the file with the suffix "_original" is the original input image.
* the file with the suffix "_restyled" is the style transferred image.
* the file with the suffix "_depth" is the output depth image.

---


## Example:
[![Video Example](https://github.com/atapour/styleDepth-Inference/blob/master/imgs/thumbnail.jpg)](https://vimeo.com/260393753 "Video Example - Click to Play")

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Video Example - click image above to play.

---

## Reference:

[Real-Time Monocular Depth Estimation using Synthetic Data with Domain Adaptation via Image Style Transfer](http://breckon.eu/toby/publications/papers/abarghouei18monocular.pdf)
(A. Atapour-Abarghouei, T.P. Breckon), In Proc. Conf. Computer Vision and Pattern Recognition, 2018. [[pdf](http://breckon.eu/toby/publications/papers/abarghouei18monocular.pdf)] [[demo](https://vimeo.com/260393753)]

```
@InProceedings{abarghouei18monocular,
  author = 		{Atapour-Abarghouei, A. and Breckon, T.P.},
  title = 		{Real-Time Monocular Depth Estimation using Synthetic Data with Domain Adaptation},
  booktitle = 	{Proc. Computer Vision and Pattern Recognition},
  pages =		{1-8},
  year = 		{2018},
  month = 		{June},
  publisher = 	{IEEE},
  keywords = 		{monocular depth, generative adversarial network, GAN, depth map, disparity, depth from single image},
}

```
---
