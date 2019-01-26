
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
#    if fileName:
#        print(fileName)
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
        
def getFPS():
    #note: This fuction does not work if the video does not have the FPS in its properties
    global vidcap
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    return fps 

def openFrames():
    fileName = openFile() # Filename of whichever frame is clicked
    directory = os.path.split(fileName)[0] #Directory that the video frames are stored in
    path, dirs, files = next(os.walk(directory))
    file_count = len(files)
    populateArray(file_count,directory)

    
def openVidFile():
    import ui_MAIN
    global image_list

    fileName = openFile() #openFile() opens file browser and returns name of selected video file
    directory = str(QFileDialog.getExistingDirectory(ui_MAIN.MyMainWindow(),"Select Folder to Store Frames")) # File dialog opens for user to create/selet a folder to store the frames extracted from video
    splitVideo(fileName, image_list, directory) 
    path, dirs, files = next(os.walk(directory))
    file_count = len(files)
    populateArray(file_count,directory)


def populateArray(file_count, directory):
    for x in range(1, file_count + 1):
        image_list.append(directory + "/frame" + str(x) + ".jpg")
        
    if not os.path.exists(directory + "_FRAMEOUTPUT"):
        os.mkdir(directory + "_FRAMEOUTPUT")


def img_list():
    return image_list
    

#Note:last frame come out as NULL image - so it need to be ignored
            
      
            



    
    
            