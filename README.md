# Real-Time Monocular Depth Estimation using Synthetic Data with Domain Adaptation via Image Style Transfer

Requires [PyTorch](http://pytorch.org), [OpenCV](http://www.opencv.org), Python 2 or 3, NVIDIA GPU + CUDA CuDNN.

![General Pipeline](https://github.com/atapour/styleDepth-Inference/blob/master/imgs/pipeLine.png)
General Pipeline of the approach
## Method:

_"Monocular depth estimation using learning-based approaches has become relevant and promising in recent years. However, most monocular depth estimators either need to rely on large quantities of ground truth depth data, which is extremely expensive and difficult to obtain or predict disparity as an intermediary step using a secondary supervisory signal, leading to blurring and other artefacts. Training a depth estimation model using pixel-perfect synthetic environment data can resolve most of these issues, but introduces the problem of domain bias. This is the inability
to apply a model trained on synthetic data to real-world scenarios. With recent advances in image style transfer and its connections with domain adaptation (Maximum Mean Discrepancy), our approach takes advantage of style transfer and adversarial training to predict pixel perfect depth from
a single real-world color image based on training over a large corpus of synthetic environment data. Experimental results indicate the efficacy of our approach compared to contemporary state-of-the-art."_

[[Atapour-Abarghouei, Breckon, Proc. CVPR, 2018](http://breckon.eu/toby/publications/papers/abarghouei18monocular.pdf)]

---

## Reference implementation:
Produces a depth map output image based on a a monocular color image input.
* The input RGB map will first be transormed into the style of the images captured from a highly realistic synthetic virtual environment, the depth prediction network is trained on.
* The provided color image is used as the input to [CycleGAN](https://junyanz.github.io/CycleGAN/), which transform the style of the image. Image style transfer is used a method of domain adaptation.
* The styled transferred image is used as the input to a model trained on synthetic images and can produce pixel-perfect outputs.
* The code provides an inference pipeline and can be run using the test harness: run_test.py
* Example images are provided in the Examples sub-directory.
* The training was in part performed based on code from [https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix).


![](https://github.com/atapour/styleDepth-Inference/blob/master/imgs/sample.png)
Example of the results of the approach

## Instructions to run the inference code:

```
$ git clone https://github.com/atapour/styleDepth-Inference.git
$ cd styleDepth-Inference
$ python run_test.py
```

The output results are written in the 'results' directory:
* the file with the suffix "-PROCESSED" is the despeckled depth image.
* the file with the suffix "-FILLED" is the filled depth image.
* The file "data.txt" contains information about run-time and number of cases.

---


## Example:
[![Video Example](https://github.com/atapour/styleDepth-Inference/blob/master/imgs/thumbnail.jpg)](https://vimeo.com/260393753 "Video Example - Click to Play")

Video Example - click image above to play.

---

## Reference:

[DepthComp: Real-Time Monocular Depth Estimation using Synthetic Data with Domain Adaptation via Image Style Transfer](http://breckon.eu/toby/publications/papers/abarghouei18monocular.pdf)
(A. Atapour-Abarghouei, T.P. Breckon), In Proc. Conf. Computer Vision and Pattern Recognition, 2018. [[pdf](http://breckon.eu/toby/publications/papers/abarghouei18monocular.pdf)] [[demo](https://vimeo.com/260393753)]

```
@InProceedings{abarghouei18monocular,
  author = 		{Atapour-Abarghouei, A. and Breckon, T.P.},
  title = 		{Real-Time Monocular Depth Estimation using Synthetic Data with Domain Adaptation},
  booktitle = 		{Proc. Computer Vision and Pattern Recognition},
  pages =		{1-8},
  year = 		{2018},
  month = 		{June},
  publisher = 		{IEEE}, 
  keywords = 		{monocular depth, generative adversarial network, GAN, depth map, disparity, depth from single image},
  url = 		{http://community.dur.ac.uk/toby.breckon/publications/papers/abarghouei18monocular.pdf},
  OPTdoi = 		{},
  comment = 		{<a class="demolink" href="https://vimeo.com/260393753">demo</a>},
}

```
---
