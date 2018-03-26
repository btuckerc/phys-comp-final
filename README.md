## Physical Computing Final Project
Dummy owl which will analyze pi-camera data to figure out either fashion trends, if students tend to leave on bike, if they leave with backpacks, etc. A microphone will be used to analyze overall volume of the environment. A daylight sensor will help the owl decide when to sleep (or sleep only certain sensors). Tweets will be produced related to the data; either count of people walking/biking, average color of shirt, average/max volume of the day. Data will be visualized using Dash. See sentdex tutorial on YouTube.

## Deployment

Python Dependencies:
	numpy
	matplotlib
	cv2 (opencv)

To download opencv on linux:

```
sudo apt-get install libopencv-dev python-opencv
```

Sensors:
	pi-camera
	microphone

## Built With

* [OpenCV](https://opencv.org/) - A computer vision module for Python.
* [HaarCascades](https://github.com/opencv/opencv/tree/master/data/haarcascades) - Definition of objects to be found in video stream in conjunction with OpenCV.

## Authors

* **Tucker Craig** - Davidson College Class of 2020 - [tucraig](https://github.com/tucraig)

See also the list of [contributors](https://github.com/tucraig/phys-comp-final/contributors) who participated in this project.

## Acknowledgments

* sentdex on YouTube
