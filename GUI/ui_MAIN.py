import sys, random
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
import glob
import pyqtgraph as pg
import numpy as np
import math
import csv
import upload
from saveData import *
import saveData
from main import *
import warnings
from os.path import basename


import pylab as py
import ellipseFitting

count = 1
frames= 0
image_list = [] #stores paths of all frames extracted from video
radius_data = []

for x in range(0,50):    #TO DO: add unique range based on # of image frames. Left like this for now for testing purposes
    radius_data.append(0)

image_list = upload.image_list

csv_file = 'radius_data.csv'
thresholdMultiplier = 0.5

usePrevFrame = []


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) 
        self.graphicsView.enableAutoRange('xy') # the axis will NOT automatically rescale when items are added/removed or change their shape. 
        self.L_button.clicked.connect(self.on_clickLeft) # connecting L mouse button to on_clickLeft function
        self.R_button.clicked.connect(self.on_clickRight) # connecting R mouse button to on_clickRight function
        self.actionUpload_new.triggered.connect(self.FILEMENU_upload) # connecting upload button to FILEMENU_upload
        self.horizontalSlider.sliderMoved.connect(self.sliderMoved) # when slider is moved, it will trigger sliderMoved function
      #  self.action1.triggered.connect(self.manualSelection)
      
        self.checkBox_StoreData.stateChanged.connect(self.checkBox) 
    
        self.actionSave.triggered.connect(self.csv)
        self.graphicsView.scene().sigMouseClicked.connect(self.onClick) # Connect onClick function to mouse click
        
        self.start_push_button.clicked.connect(self.fitFrameRange)

        
        
# - - - - - - - - Keyboard/Click Events - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def connection(self):
        print("checked")

    def on_clickLeft(self): 
        global count
        if count > 0:
                count= count - 1              
        self.update()
                
    def on_clickRight(self):
        global count
        if count < len(image_list)-1:
                count = count + 1
        self.update()
                
    def sliderMoved(self, val): 
        global count
        count = val
        self.update()
        
    def keyPressEvent(self, event):
        global count
        global navigation
        key = event.key()
        if key == Qt.Key_A:
            if count > 0:
                count= count - 1 
                self.update()
                navigation = "L"

        elif key == Qt.Key_D:
            if count < len(image_list)-1:
                count = count + 1
            
                self.update()
                navigation = "R"
                 
        '''
        elif key == Qt.Key_Delete: #if del key is pressed, ROI is removed. #STILL have to manually remove data though. #TO DO
            self.graphicsView.removeItem(cir)
            self.checkBox_StoreData.setChecked(False) 
            coordinates[:] = []
            print("  ")
            print("delete", diameter_data)
            print(" ")
        '''

        
# - - - - - - - - - - - - - - - - -  File Menu - - - - - - - - - - - - - - - - - #
    def FILEMENU_upload(self):
        global originalImageDir
        upload.openVidFile()
        self.update()
        originalImageDir = image_list[0].rsplit('/',1)[0]
    
    # Example of action in menu triggered
    '''
    def fileMenu(self):  #FOR TESTING -- delete later
        print("fileMenu triggered")
        if self.action1.isChecked() == True:
            pass
    '''
        
        
#- - - - - - - Displaying image on GUI and updating - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
    def update(self):
        global img_arr
        global maxCount
        global cir
        global img
        img = Image.open(image_list[count])
        arr = np.array(img)
        arr = np.rot90(arr, -1)
        img_arr = pg.ImageItem(arr)
        self.graphicsView.addItem(img_arr)
        
        self.label_frameNum.setText("Frame " + str(count))
        self.horizontalSlider.setSliderPosition((count/len(image_list))*100) #setting the slider proportionate to the position of the current frame    

        if count in usePrevFrame:
             self.checkBox_StoreData.setChecked(True) 
        else:
            self.checkBox_StoreData.setChecked(False) 
 
 
    def csv(self):
        #save.export_to_csv(self, diameter_data)
        ellipseFitting.export_to_csv(radius_data,csv_file)
        print("radius_data saved to CSV as", csv_file)
        



        
        
#- - - - - - Ellipse Fitting - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


        
    def onClick(self,event):        
        global coordinates
        global count

        # Getting center coordinates from click
        cor = img_arr.mapFromScene(event.scenePos()) #maps coordinate from image pixels
        x = cor.x()
        y = cor.y()
        coordinates = [x,y]
        print("Center click:", coordinates)
        
        
        
        if 'circle.jpg' not in image_list[count]:
            self.fitSingleFrame(image_list[count],count, 'circles', thresholdMultiplier)
        else:
            print("COUNT IS:", count)
            originalImagePath = originalImageDir + "/frame" + str(count) + ".jpg"
            self.fitSingleFrame(originalImagePath, count, 'circles', thresholdMultiplier)
            
       
        
        
    def fitSingleFrame(self, frame, frame_num, outputFolder, thresholdMultiplier):  
        
        #Setting output name and folder
        frameName = basename(frame)             
        outputName = outputFolder + '/' + frameName.split('.')[0] + 'circle.jpg'        
        
        
        img=ellipseFitting.get_image_mat(frame)                
        threshold = img.mean(axis=0).mean()* thresholdMultiplier
        img = ellipseFitting.get_binary_image_mat(frame,threshold)
        
        ##########################################################
        estimate_center = np.array([600,800])
        print("estimate_center:", estimate_center)
        estimate_radius = 300

        estimate_a = estimate_radius
        estimate_b = estimate_radius
        
        points = ellipseFitting.find_edge_points(estimate_center,estimate_radius,img)
        a_points = np.array(points)
        x = a_points[:, 0]
        y = a_points[:, 1]
#        py.scatter(x,y, color="blue")
        
      
        eye = ellipseFitting.fitEllipse(x,y)
        center = ellipseFitting.ellipse_center(eye)
        #center = np.array(coordinates)
        
        
        if isinstance(center[0], complex):
            center = estimate_center
            r = estimate_radius
            a = estimate_a
            b = estimate_b  
            
        else:
            phi = ellipseFitting.ellipse_angle_of_rotation2(eye)
            axes = ellipseFitting.ellipse_axis_length(eye)
            a, b = axes
            area = np.pi*a*b
            r = np.sqrt(a*b)
        
        
        print ("center = ",  center)
        print ("angle of rotation = ",  phi)
        print ("axes = ", axes)
        print ("area = ", area)
        print ("radius = ", r)
        
        R = np.arange(0,2*np.pi, 0.01)
        xx = center[0] + a*np.cos(R)*np.cos(phi) - b*np.sin(R)*np.sin(phi)
        yy = center[1] + a*np.cos(R)*np.sin(phi) + b*np.sin(R)*np.cos(phi)
        


        #########################################'
        
        show_circle_img = ellipseFitting.get_image_mat(frame)
        ellipseFitting.add_circle(show_circle_img,center,r,255)

        radius_data[frame_num] = r
        print(radius_data)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ellipseFitting.save_image(show_circle_img,center,r,a,b,phi,outputName) 
        
        self.updateCircleImage(outputName, frame_num)
                    
    
    def updateCircleImage(self,output_frame, frame_num):                   
        updateImg = Image.open(output_frame)
        ar = np.array(updateImg)
        ar = np.rot90(ar, -1)
        img_ar = pg.ImageItem(ar)
        self.graphicsView.addItem(img_ar)
        image_list[frame_num] = output_frame

        
    def fitFrameRange(self):
        
        start = 1 
        stop = 50
        
        rangeLen = stop - start
        for i in range(start,stop):
            self.fitSingleFrame(image_list[i], i, 'circles', thresholdMultiplier)
            
            print(i/rangeLen)
            
            self.progressBar.setProperty("value", (i/rangeLen)*100)
            
            
    def checkBox(self):
        if self.checkBox_StoreData.isChecked() == True:
            usePrevFrame.append(count)
        if self.checkBox_StoreData.isChecked() == False and count in usePrevFrame:
            usePrevFrame.remove(count)
        
            
            
    def usePrevData(frame, self):
        pass
         
               
#Old portion of code from before - remove later.         
'''     
            
            LLC = (x1 - (d/2), (y1 - (d/2))) # lower left corner of bounding box
            cir = pg.CircleROI(LLC, [d,d], pen=(4,8)) #blue
            self.graphicsView.addItem(cir)
            self.checkBox_StoreData.setChecked(True)
'''  


def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = MyMainWindow()  # Set form
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main functiond