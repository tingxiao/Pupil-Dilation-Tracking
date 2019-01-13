
import sys
import cv2
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import time
import numpy as np
import os
global vidcap
import main 

from PIL import Image

global directory

image_list = [] #stores paths of all frames extracted from video
    
def openFile():   
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","Video Files (* avi);;Python Files (*.py)", options=options)
    if fileName:
        print(fileName)
    return fileName



def splitVideo(vidFileName, imageListInput, folderName):
    global vidcap
    framecount = 1 
    folder = folderName    
    vidcap = cv2.VideoCapture(str(vidFileName))
    success,image = vidcap.read()
    success = True
    while success:
            success,image = vidcap.read()
            print ('Read a new frame: '), success
            cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(framecount)), image)     # save frame as JPEG file
            print("{} images are extacted in {}.".format(framecount,folder))
            framecount += 1
 
    if not os.path.exists(folder + "_FRAMEOUTPUT"):
        os.mkdir(folder + "_FRAMEOUTPUT")
 
        
def getFPS():
    #note: This fuction does not work if the video does not have the FPS in its properties
    global vidcap
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    return fps 

def calculateFPS():
    #Just for testing on specific vids
    s = 41
    frames = 737
    fps = frames/s
    return fps


def openVidFile():
    import ui_MAIN
    from ui_MAIN import MyMainWindow
    global image_list

    fileName = openFile() #openFile() opens file browser and returns name of selected video file
    directory = str(QFileDialog.getExistingDirectory(ui_MAIN.MyMainWindow(),"Select Folder to Store Frames")) # File dialog opens for user to create/selet a folder to store the frames extracted from video
    print("directory is:", directory)
    splitVideo(fileName, image_list, directory) 
    
.
    #TO DO: add loading status bar while frames are being uploaded      
    
    path, dirs, files = next(os.walk(directory))
    file_count = len(files)

    for x in range(1, file_count + 1):
        image_list.append(directory + "/frame" + str(x) + ".jpg")
        
    #ui_MAIN.MyMainWindow.horizontalSlider.setRange(0,len(image_list)-1)
    #ui_MAIN.MyMainWindow.video_title.setText(fileName)
    #ui_MAIN.MyMainWindow().add_img()


def img_list():
    return image_list
    

#Note:last frame come out as NULL image - so it need to be ignored
            
      
            



    
    
            