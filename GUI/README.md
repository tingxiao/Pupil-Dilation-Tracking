# Pupil Dilation Tracker

The Pupil Dilation Tracker uses ellipse fitting techniques to automatically measure changes in pupil diameter throughout videos. Data is recorded at each frame and can be exported as a csv file.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)

## Features
**Frame extraction**  
Frames can extracted from videos or directly imported into the program.

**Optimizing the detection**
Detections can be done and later edited on single frames, a custom range, or all of the frames. The threshold and center can be customized with a click for further optimization. 

**Blink management** 
In the case of a blink or faulty detection, a checkbox can be marked to indicate to use data from the previous frame.

**Exporting data to csv**
Pupil diameter measurements can be exported to a csv file.

## Installation

**1. Download Anaconda** Python Version 3.5+  https://www.anaconda.com/download/

**2. Install packages** - Open the Anaconda Prompt and install the necessary packages

- *opencv* `conda install -c menpo opencv`

- *filterpy* `conda install -c conda-forge filterpy`

- *imageio* `conda install -c conda-forge imageio`

- *pyqt* `conda install pyqt`

- *pyqtgraph* `conda install pyqtgraph`

- *numpy* `conda install numpy`

- *pillow* `conda install pillow`

- *pandas* `conda install pandas`

**3. Clone repository**
`git clone https://github.com/j-adamski/Pupil-Dilation-Tracking-GUI.git`

**4. Run program**
`python ui_MAIN.py`
