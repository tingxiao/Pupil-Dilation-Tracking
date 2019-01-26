# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #MainWindow.setWindowTitle('PictureWorkshop')
        MainWindow.setObjectName("Pupil Dilation Tracker")
        MainWindow.resize(1603, 1158)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.video_title = QtWidgets.QLabel(self.centralwidget)
        self.video_title.setStyleSheet("font: 75 11pt \"Adobe Devanagari\";")
        self.video_title.setObjectName("video_title")
        self.gridLayout.addWidget(self.video_title, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_FrameViewer = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_FrameViewer.sizePolicy().hasHeightForWidth())
        self.tab_FrameViewer.setSizePolicy(sizePolicy)
        self.tab_FrameViewer.setObjectName("tab_FrameViewer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_FrameViewer)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.tab_FrameViewer)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))
        self.frame.setSizeIncrement(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(self.frame_2)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_3.addWidget(self.horizontalSlider, 0, 1, 1, 2)
        self.label_frameNum = QtWidgets.QLabel(self.frame_2)
        self.label_frameNum.setStyleSheet("font: 75 9pt \"Adobe Devanagari\";")
        self.label_frameNum.setObjectName("label_frameNum")
        self.gridLayout_3.addWidget(self.label_frameNum, 2, 1, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.L_button = QtWidgets.QPushButton(self.frame_2)
        self.L_button.setMinimumSize(QtCore.QSize(100, 100))
        self.L_button.setMaximumSize(QtCore.QSize(100, 100))
        self.L_button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.L_button.setObjectName("L_button")
        self.gridLayout_3.addWidget(self.L_button, 1, 1, 1, 1)
        self.R_button = QtWidgets.QPushButton(self.frame_2)
        self.R_button.setMinimumSize(QtCore.QSize(100, 100))
        self.R_button.setMaximumSize(QtCore.QSize(100, 100))
        self.R_button.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.R_button.setObjectName("R_button")
        self.gridLayout_3.addWidget(self.R_button, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_2)
        self.gridLayout_2.addWidget(self.frame, 2, 1, 1, 1)
        self.checkBox_UsePrevData = QtWidgets.QCheckBox(self.tab_FrameViewer)
        self.checkBox_UsePrevData.setObjectName("checkBox_UsePrevData")
        self.gridLayout_2.addWidget(self.checkBox_UsePrevData, 0, 1, 1, 1, QtCore.Qt.AlignRight)
        
        
        self.start_push_button = QtWidgets.QPushButton(self.tab_FrameViewer)
       # self.start_push_button.setGeometry(QtCore.QRect(350, 10, 131, 40))
        self.start_push_button.setGeometry(QtCore.QRect(180, 10, 131, 40))   
        self.start_push_button.setObjectName("start_push_button")
        self.custom_range_box = QtWidgets.QLineEdit(self.tab_FrameViewer)
        self.custom_range_box.setGeometry(QtCore.QRect(90, 10, 71, 41))
        self.custom_range_box.setObjectName("custom_range_box")
        self.threshold_box = QtWidgets.QLineEdit(self.tab_FrameViewer)
       # self.threshold_box.setGeometry(QtCore.QRect(260, 10, 61, 41))
        self.threshold_box.setGeometry(QtCore.QRect(580, 10, 61, 41)) 
        self.threshold_box.setObjectName("threshold_box")
        self.threshold_label = QtWidgets.QLabel(self.tab_FrameViewer)
       # self.threshold_label.setGeometry(QtCore.QRect(170, 10, 81, 23))
        self.threshold_label.setGeometry(QtCore.QRect(490, 10, 81, 23))
        self.threshold_label.setObjectName("threshold_label")
        self.label_2 = QtWidgets.QLabel(self.tab_FrameViewer)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 80, 23))
        self.label_2.setObjectName("label_2")
        self.customRange_label = QtWidgets.QLabel(self.tab_FrameViewer)
        self.customRange_label.setGeometry(QtCore.QRect(30, 30, 80, 23))
        self.customRange_label.setObjectName("customRange_label")
        self.progressBar = QtWidgets.QProgressBar(self.tab_FrameViewer)
        #self.progressBar.setGeometry(QtCore.QRect(500, 20, 124, 25))
        self.progressBar.setGeometry(QtCore.QRect(320, 20, 124, 25))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.threshold_label_2 = QtWidgets.QLabel(self.tab_FrameViewer)
       # self.threshold_label_2.setGeometry(QtCore.QRect(170, 30, 81, 23))
        self.threshold_label_2.setGeometry(QtCore.QRect(490, 30, 81, 23))
        self.threshold_label_2.setObjectName("threshold_label_2")
        
        
        
        #self.graphicsView = PlotWidget(self.tab_FrameViewer)
        #self.graphicsView.setObjectName("graphicsView")
        #self.graphicsView.setAspectLocked(True) #keeps aspect locked for imported video frames, otherwise it stretches everything out.        
        
    
        self.graphicsView = PlotWidget(self.tab_FrameViewer)
        graphicsView = self.graphicsView
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setAspectLocked(True) #keeps aspect locked for imported video frames, otherwise it stretches everything out.        
        self.gridLayout_2.setContentsMargins(0,40,0,0) # Lowers grphicsView a little, so the options are visible at the top
        
        self.gridLayout_2.addWidget(self.graphicsView, 1, 1, 1, 1)
        
        self.tabWidget.addTab(self.tab_FrameViewer, "")
        self.tab_Data = QtWidgets.QWidget()
        self.tab_Data.setObjectName("tab_Data")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_Data)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        #self.graphicsView_Plot = QtWidgets.QGraphicsView(self.tab_Data)
        self.graphicsView_Plot = PlotWidget(self.tab_Data)
        self.graphicsView_Plot.setObjectName("graphicsView_Plot")
        
        #sizePolicy.setHeightForWidth(self.graphicsView_Plot.sizeAdjustPolicy())        
        self.horizontalLayout_2.addWidget(self.graphicsView_Plot)
        self.dataDisplay = QtWidgets.QTextBrowser(self.tab_Data)
        self.dataDisplay.setMaximumSize(QtCore.QSize(640, 16777215))
        self.dataDisplay.setObjectName("dataDisplay")
        self.horizontalLayout_2.addWidget(self.dataDisplay)
        self.tabWidget.addTab(self.tab_Data, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1603, 47))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
    
        
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionUpload_new = QtWidgets.QAction(MainWindow)
        self.actionUpload_new.setObjectName("actionUpload_new")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionKalman = QtWidgets.QAction(MainWindow)
        self.actionKalman.setObjectName("actionKalman")
        self.actionProperties = QtWidgets.QAction(MainWindow)
        self.actionProperties.setObjectName("actionProperties")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        
        self.actionEllipseFitting = QtWidgets.QAction(MainWindow)
        self.actionEllipseFitting.setObjectName("actionEllipseFitting")
        self.actionEllipseFitting.setCheckable(True)
        self.actionEllipseFitting.setChecked(True)
        
        
        # Commented out for now - until we can implement this feature in the future
        '''
        self.actionManualSelection = QtWidgets.QAction(MainWindow)
        self.actionManualSelection.setCheckable(True)
        self.actionManualSelection.setChecked(False)
        self.actionManualSelection.setObjectName("actionManualSelection")
        '''

            
        '''
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setCheckable(True)
        self.action1.setObjectName("action1")
        self.action2 = QtWidgets.QAction(MainWindow)
        self.action2.setObjectName("action2")
        self.action3 = QtWidgets.QAction(MainWindow)
        self.action3.setCheckable(True)
        self.action3.setObjectName("action3")
        '''        
        
        # Adding menu actions under "FILE" 
        self.menuFile.addAction(self.actionUpload_new)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionKalman)
        
           
        #Adding menu actions under "OPTIONS"
     #   self.menuOptions.addAction(self.actionEllipseFitting)
     #   self.menuOptions.addAction(self.actionManualSelection)
                
     
        #Creating QActionGroup to have radio buttons in the file menu,  code w/o radio buttons commented out above
        self.ag = QtGui.QActionGroup(MainWindow, exclusive=True)
        self.a1 = self.ag.addAction(self.actionEllipseFitting)
        self.menuOptions.addAction(self.a1)
      #  self.a2 = self.ag.addAction(self.actionManualSelection)
      #  self.menuOptions.addAction(self.a2)
      
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pupil Dilation Tracker"))
        self.video_title.setText(_translate("MainWindow", "Click FILE to upload frames"))
        self.label_frameNum.setText(_translate("MainWindow", "No frames to display"))
        self.L_button.setText(_translate("MainWindow", "🡰"))
        self.R_button.setText(_translate("MainWindow", "🡲"))
        self.checkBox_UsePrevData.setText(_translate("MainWindow", "Use Previous Frame Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_FrameViewer), _translate("MainWindow", "Video frames"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Data), _translate("MainWindow", "Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
  #      self.actionManualSelection.setText(_translate("MainWindow", "Manual Selection"))
        self.actionEllipseFitting.setText(_translate("MainWindow", "Ellipse Fitting"))
       
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionUpload_new.setText(_translate("MainWindow", "Upload video"))
        self.actionOpen.setText(_translate("MainWindow", "Open frames"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionKalman.setText(_translate("MainWindow", "Apply Kalman Filter"))
        
        self.actionProperties.setText(_translate("MainWindow", "Properties"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))
        
        self.start_push_button.setText(_translate("MainWindow", "START"))
        self.threshold_label.setText(_translate("MainWindow", "   Custom"))
        self.threshold_label_2.setText(_translate("MainWindow", "Threshold"))
        self.customRange_label.setText(_translate("MainWindow", "Range"))
        self.label_2.setText(_translate("MainWindow", "Custom"))
        self.threshold_box.setText(_translate("MainWindow", "0.5"))
        
        self.progressBar.setProperty("value", 0)

        
        '''
        self.action1.setText(_translate("MainWindow", "1 - Manual selection"))
        self.action2.setText(_translate("MainWindow", "2 - Gaussian Filter"))
        self.action3.setText(_translate("MainWindow", "3 - Kalman Filter"))
        '''
        
from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

