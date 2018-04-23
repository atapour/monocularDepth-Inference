# DepthComp: Real-Time Monocular Depth Estimation using Synthetic Data with Domain Adaptation via Image Style Transfer

Requires [OpenCV](http://www.opencv.org), Python 2 or 3, NVIDIA GPU + CUDA CuDNN.

<img src='imgs/pipeLine.pdf' align="center">

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
* A generic interface C++ object is provided within the depthComp.{cpp|.hpp} files.

```

DepthComp (c) Amir Atapour-Abarghouei, 2017
GPL - http://www.gnu.org/licenses/gpl.html

Compilation and Run Instructions for the Example Code:

$ mkdir build
$ cd build
$ cmake ..
$ make
$ ./depthComp ./../Examples/city1-depth.png ./../Examples/city1-seg.png)
```

The output results are written in the 'Examples' directory:
* the file with the suffix "-PROCESSED" is the despeckled depth image.
* the file with the suffix "-FILLED" is the filled depth image.
* The file "data.txt" contains information about run-time and number of cases.

---

## Example:
[![Video Example](https://i.imgur.com/ZlOPibl.jpg)](https://vimeo.com/224513553 "Video Example - Click to Play")

Video Example - click image above to play.

---

## Reference:

[DepthComp: Real-time Depth Image Completion Based on  Semantic Scene Segmentation](http://breckon.eu/toby/publications/papers/abarghouei17depthcomp.pdf)
(A. Atapour-Abarghouei, T.P. Breckon), In Proc. British Machine Vision Conference, 2017. [[pdf](http://breckon.eu/toby/publications/papers/abarghouei17depthcomp.pdf)] [[demo](https://vimeo.com/224513553)]

```
@InProceedings{abarghouei17depthcomp,
  author = 	 {Atapour-Abarghouei, A. and Breckon, T.P.},
  title = 	 {DepthComp: Real-time Depth Image Completion Based on Prior Semantic Scene Segmentation},
  booktitle = 	 {Proc. British Machine Vision Conference},
  pages = 	 {208.1-208.13},
  year = 	 {2017},
  month = 	 {September},
  publisher =    {BMVA},
  keywords =     {depth filling, RGB-D, surface relief, hole filling, surface completion, 3D texture, depth completion, depth map, disparity hole filling},
  url = 	 {http://community.dur.ac.uk/toby.breckon/publications/papers/abarghouei17depthcomp.pdf}
}
```
---
