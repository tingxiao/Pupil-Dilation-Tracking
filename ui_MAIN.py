import sys, random
from PyQt5 import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
import pyqtgraph as pg
import numpy as np
import upload
from main import *
import warnings
from os.path import basename
import kalmanFilter
import ellipseFitting

count = 1 #keeps track of the frame that is currently being displayed on the screen
global frames #number of frames, is updated after uploading video or selecting folder with frames
image_list = [] #stores paths of all frames extracted from video
radius_data = [] #radius data that is collected by fitting the ellipse on the frames, then this array is exported to csv file
image_list = upload.image_list 
usePrevFrame = [] # array that holds the frames that will have the previous data used


class MyMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) 
        self.graphicsView.enableAutoRange('xy') # the axis will NOT automatically rescale when items are added/removed or change their shape. 
        self.L_button.clicked.connect(self.on_clickLeft) # connecting L mouse button to on_clickLeft function
        self.R_button.clicked.connect(self.on_clickRight) # connecting R mouse button to on_clickRight function
        self.actionUpload_new.triggered.connect(self.FILEMENU_upload) # connecting upload button to FILEMENU_upload
        self.horizontalSlider.sliderMoved.connect(self.sliderMoved) # when slider is moved, it will trigger sliderMoved function
        self.checkBox_UsePrevData.stateChanged.connect(self.checkBox) # when checkbox is checked or unchecked, the checkbox() function is triggered
        self.actionSave.triggered.connect(self.csv) #Saves as CSV file when save is clicked
        self.actionKalman.triggered.connect(self.applyKalman) #kalman filter applied when it is clicked in the file menu by triggering applyKAlman() function and saving as csv
        self.graphicsView.scene().sigMouseClicked.connect(self.onClick) # Connect onClick function to mouse click
        self.start_push_button.clicked.connect(self.fitFrameRange) # when clicking start button, fitFrameRange() is called - which fits the range that is specified in the box

        
# - - - - - - - - Keyboard/Click Events - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Events for left click, right click, if the slider is moved, and if certain keys are pressed
        
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
                   
# - - - - - - - - - - - - - - - - -  File Menu - - - - - - - - - - - - - - - - - #
'''
 If "open" is triggered in the file menu, the file dialog opens and allows the user to select a video to extract frames from then it prompts them to 
 select/create a folder to store those frames into. Frames that have already been extracted from a video can also be imported into the program by selecting one of the frames
 when the file dialog open. This function also calles update() to display the current frame onto to view, calculates the number of frames, and creates an empty array for the frames.
''' 
   def FILEMENU_upload(self):
        global originalImageDir
        global originalImageFolder
        global fps
        upload.openVidFile()
        self.update()
        originalImageDir = image_list[0].rsplit('/',1)[0]
        originalImageFolder = originalImageDir.rsplit('/',1)[-1]
        
        num_of_frames = len(image_list) #total num of frames
    
        #populating array with 0's 
        for x in range(0,num_of_frames):    
            radius_data.append(0)


  
#- - - - - - - Displaying image on GUI and updating - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
'''
opens the frame and displays it onto the graphics view. The label and slider position are updated with the frame currently being viewed. 
The checkbox also checks or unchecks depending on if that frame has been added to the UsePrevData array.
'''
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
             self.checkBox_UsePrevData.setChecked(True) 
        else:
            self.checkBox_UsePrevData.setChecked(False) 
 
'''
Saving to csv file with the original folder name that the frame images were stored in with _DATA added to the name 
'''
    def csv(self):
        csv_file = originalImageFolder + "_DATA.csv"
        ellipseFitting.export_to_csv(radius_data,csv_file)
        print("radius_data saved to CSV as", csv_file)
        
'''
Applies Kalman filter to the csv file - which must be created first
# TO DO - if csv file does not exist, create it then apply kalman
'''        
    def applyKalman(self):
        csv_file = originalImageFolder + "_DATA.csv"
        kalmanFilter.applyKalmanFilter(csv_file, originalImageFolder)


#- - - - - - Ellipse Fitting - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

'''
If there is a click on the image on the graphicsView, then collect the coordinates, update the threshold multiplier (if necessary), check if the frame already has a circle,

'''        
    def onClick(self,event):        
        global coordinates
        global count
        global output_directory
        # Getting center coordinates from click
        cor = img_arr.mapFromScene(event.scenePos()) #maps coordinate from image pixels
        x = int(cor.x())
        y = int(cor.y())
        coordinates = [y,x] #Axis of image is flipped for some reason
        print("Center click:", coordinates, "**Axis flipped for img**")
         
        thresholdMultiplier = self.threshold_box.text()
        thresholdMultiplier = float(thresholdMultiplier)
        print("ThresholdMultiplier:",thresholdMultiplier)
        
        # If "circle.jpg" is not in the image name for the current frame, then call fitSingleFrame, else - get the original image w/o the circle drawn and fit the frame again
        output_directory = originalImageFolder + "_FRAMEOUTPUT"
        if 'circle.jpg' not in image_list[count]:
            self.fitSingleFrame(image_list[count],count, output_directory, thresholdMultiplier)
        else:
            originalImagePath = originalImageDir + "/frame" + str(count) + ".jpg"
            self.fitSingleFrame(originalImagePath, count, output_directory, thresholdMultiplier)
    
            
       
'''
Detection on a single frame using ellipse fitting
'''
    def fitSingleFrame(self, frame, frame_num, outputFolder, thresholdMultiplier):  
        global frameName
        global outputName
        global phi
  
        
        #Setting output name and folder
        frameName = basename(frame)             
        outputName = outputFolder + '/' + frameName.split('.')[0] + 'circle.jpg'        
        
        img=ellipseFitting.get_image_mat(frame)                
        threshold = img.mean(axis=0).mean()* thresholdMultiplier
        img = ellipseFitting.get_binary_image_mat(frame,threshold)
        
        ##########################################################
        estimate_center = np.array(coordinates)
        print("estimate_center:", estimate_center)
        estimate_radius = 300

        estimate_a = estimate_radius
        estimate_b = estimate_radius
        
        points = ellipseFitting.find_edge_points(estimate_center,estimate_radius,img)
        a_points = np.array(points)
        x = a_points[:, 0]
        y = a_points[:, 1]

        eye = ellipseFitting.fitEllipse(x,y)
        center = ellipseFitting.ellipse_center(eye)
               
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
        
        
        # Have to declare these global variables, otherwise they are not defined
        global prev_radius
        global prev_center
        global prev_a
        global prev_b
        global prev_threshold
        
        # Use previous data if the frame is in the usePrevFrame array
        if frame_num not in usePrevFrame:
            prev_radius = r
            prev_center = center
            prev_a = a
            prev_b = b
            prev_threshold = threshold
        else: 
            r = prev_radius
            center = prev_center
            a = prev_a
            b = prev_b
            threshold = prev_threshold
             
        
        show_circle_img = ellipseFitting.get_image_mat(frame)
        ellipseFitting.add_circle(show_circle_img,center,r,255)

        radius_data[frame_num-1] = r
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            ellipseFitting.save_image(show_circle_img,center,r,a,b,phi,outputName) 

        self.updateCircleImage(outputName, frame_num)
      
                    
    # Updates the image on graphicsView with new circle drawn
    def updateCircleImage(self,output_frame, frame_num):                   
        updateImg = Image.open(output_frame)
        ar = np.array(updateImg)
        ar = np.rot90(ar, -1)
        img_ar = pg.ImageItem(ar)
        self.graphicsView.addItem(img_ar)
        image_list[frame_num] = output_frame

'''
For fitting a range of frames, the range is specified in the text box with a dash (EX: frames one to five --->   1-5)
'''
    def fitFrameRange(self):
        output_directory = originalImageFolder + "_FRAMEOUTPUT"
        
        thresholdMultiplier = self.threshold_box.text()
        thresholdMultiplier = float(thresholdMultiplier)
        print("ThresholdMultiplier:",thresholdMultiplier)
        
        customRange = self.custom_range_box.text()
        customRange = customRange.split('-')
        
        start = int(customRange[0])
        stop = int(customRange[1])
        
        
        rangeLen = stop - start
        for i in range(start,stop+1):
            if 'circle.jpg' not in image_list[count]:
                self.fitSingleFrame(image_list[i], i, output_directory, thresholdMultiplier)
            #    print(i/rangeLen)
                
            else:
                print("COUNT IS:", i)
                originalImagePath = originalImageDir + "/frame" + str(i) + ".jpg"
                self.fitSingleFrame(originalImagePath, i, output_directory, thresholdMultiplier)
                self.progressBar.setProperty("value", (i/rangeLen)*100)
            
    # If the check box is checked, then the current count is added to array "usePrevFrame" and removed if the checkbox is unchecked
    # The purpose of the checkbox being checked is to use data from the previous frame in case of a blink or faulty detection    
    def checkBox(self):
        if self.checkBox_UsePrevData.isChecked() == True:
            usePrevFrame.append(count)
        if self.checkBox_UsePrevData.isChecked() == False and count in usePrevFrame:
            usePrevFrame.remove(count)
    

def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = MyMainWindow()  # Set form
    form.show()  # Show the form
    app.exec_()  # and execute the app



if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main functiond