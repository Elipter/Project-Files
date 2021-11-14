# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 17:53:23 2021

@author: aszem
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 16:29:29 2021

@author: aszem
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:37:48 2021

@author: aszem
"""

 
 
import sys

import numpy as np

import PyQt5

from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial, QDoubleSpinBox, QFontComboBox, QLCDNumber,QLabel, QLineEdit, QProgressBar, QPushButton, QRadioButton, QSlider, QSpinBox, QTimeEdit, QListWidget, QButtonGroup, QGroupBox
from PyQt5.QtCore import QSize 
 
from PyQt5 import QtGui

from PyQt5.QtGui import QFont

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
 

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from matplotlib.pyplot import figure


import os


#Fixes issue with high resolution monitor and scaling
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)


#data directory
data_dir = '/Users/aszem/.spyder-py3/'

     


 
fig, (ax1) = plt.subplots(1, 1, sharex=True, sharey=True, figsize = (6, 6),  dpi=80)

fig2, (ax2) = plt.subplots(1, 1, sharex=True, sharey=True, figsize = (6, 6),  dpi=80)

fig.set_size_inches(10, 10)
fig2.set_size_inches(10, 10)

                
ax1.set_xlabel('X-axis', size = 30) 
ax1.set_ylabel('Y-axis', size = 30) 


ax2.set_xlabel('X-axis', size = 30) 
ax2.set_ylabel('Y-axis', size = 30) 
   


#ax1.set_xticklabels(xlabels, Fontsize= 30) 

#ax1.set_xticklabels(np.arange(5), Fontsize= 30) 


fig.suptitle('Title', size=30)


fig2.suptitle('Title', size=30)
 



fig.canvas.draw()

fig2.canvas.draw()

fileList = []
  

fileList2 = []





from win32api import GetSystemMetrics



print("Screen Width =", GetSystemMetrics(0))
print("Screen Height =", GetSystemMetrics(1))

screenWidth = GetSystemMetrics(0)
screenHeight = GetSystemMetrics(1)


class MainWindow(QMainWindow):

    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.left = 10
        self.top = 10
        self.width = 1800
        self.height = 700
        self.title = 'User Interface'
        

        self.setGeometry(0, 0, self.width, self.height)
        
         
        self.initUI()
        
                
    
         
    def initUI(self):    



        self.setMinimumSize(QSize(self.width,self.height))    

 
    
        self.labelXPos = 20
        
        self.lineEditWidth = 320
        self.lineEditHeight = 32
        self.lineEditXPos = 200
        self.lineEditYPos = 20
        
        
        self.okButtonWidth = 200
        self.okButtonHeight = 32
        self.okButtonXPos = 540


      
    
        self.combo = QComboBox(self)
        self.combo.resize(self.lineEditWidth, self.lineEditHeight)
        self.combo.move(self.lineEditXPos, 20)




        spyderFiles = os.listdir("/Users/aszem/.spyder-py3/") 

        for i in range(len(spyderFiles)): 
            self.combo.addItem(spyderFiles[i])

    



        iobutton = QPushButton('Add File', self)
        iobutton.clicked.connect(self.clickMethod)
        iobutton.resize(200,32)
        iobutton.move(self.okButtonXPos, 20)


    
        self.nameLabelFileList = QLabel(self)
        self.nameLabelFileList.setText('File List:')
        self.nameLabelFileList.move(20, 20)
        self.nameLabelFileList.resize(100, 20)
        self.nameLabelFileList.adjustSize()
 

     
        self.nameLabelTitle = QLabel(self)
        self.nameLabelTitle.setText('Title:')
        self.nameLabelTitle.move(20, 70)
        self.nameLabelTitle.resize(100, 20)
        self.nameLabelTitle.adjustSize()
 
        self.lineTitle = QLineEdit(self)
        self.lineTitle.move(self.lineEditXPos, 70)
        self.lineTitle.resize(320, 32)

        iobuttonTitle = QPushButton('OK', self)
        iobuttonTitle.clicked.connect(self.changeTitle)
        iobuttonTitle.resize(200,32)
        iobuttonTitle.move(self.okButtonXPos, 70)
     
               

        
        self.nameLabelX = QLabel(self)
        self.nameLabelX.setText('X-Axis Name:')
        self.nameLabelX.move(20, 120)
        self.nameLabelX.resize(100, 20)
        self.nameLabelX.adjustSize()

 
        self.lineX = QLineEdit(self)
        self.lineX.move(self.lineEditXPos, 120)
        self.lineX.resize(self.lineEditWidth, self.lineEditHeight)


        iobuttonX = QPushButton('OK', self)
        iobuttonX.clicked.connect(self.change_Xaxis_Name)
        iobuttonX.resize(self.okButtonWidth, self.okButtonHeight)
        iobuttonX.move(self.okButtonXPos, 120)





        self.nameLabelY = QLabel(self)
        self.nameLabelY.setText('Y-Axis Name:')
        self.nameLabelY.move(20, 170)
        self.nameLabelY.resize(100, 20)
        self.nameLabelY.adjustSize()

 
        self.lineY = QLineEdit(self)
        self.lineY.move(self.lineEditXPos, 170)
        self.lineY.resize(self.lineEditWidth, self.lineEditHeight)



        iobuttonY = QPushButton('OK', self)
        iobuttonY.clicked.connect(self.change_Yaxis_Name)
        iobuttonY.resize(self.okButtonWidth, self.okButtonHeight)
        iobuttonY.move(self.okButtonXPos, 170)



        self.minXLabel = QLabel(self)
        self.minXLabel.setText('X-Min, X-Max:')
        self.minXLabel.move(20, 220)
        self.minXLabel.resize(100, 20)
        self.minXLabel.adjustSize()

 
        self.lineXMin = QLineEdit(self)
        self.lineXMin.move(self.lineEditXPos, 220)
        self.lineXMin.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight) 


          
        self.lineXMax = QLineEdit(self)
        self.lineXMax.move(self.lineEditXPos + self.lineEditWidth / 2 + 10, 220)
        self.lineXMax.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight)


        XMaxButton = QPushButton('OK', self)
        XMaxButton.clicked.connect(self.clickMethodMaxX)
        XMaxButton.resize(self.okButtonWidth, self.okButtonHeight)
        XMaxButton.move(self.okButtonXPos, 220)

        self.minYLabel = QLabel(self)
        self.minYLabel.setText('Y-Min, Y-Max:')
        self.minYLabel.move(20, 270)
        self.minYLabel.resize(100, 20)
        self.minYLabel.adjustSize()

 
        self.lineYMin = QLineEdit(self)
        self.lineYMin.move(self.lineEditXPos, 270)
        self.lineYMin.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight) 


          
        self.lineYMax = QLineEdit(self)
        self.lineYMax.move(self.lineEditXPos + self.lineEditWidth / 2 + 10, 270)
        self.lineYMax.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight)


        YMaxButton = QPushButton('OK', self)
        YMaxButton.clicked.connect(self.clickMethodMaxY)
        YMaxButton.resize(self.okButtonWidth, self.okButtonHeight)
        YMaxButton.move(self.okButtonXPos, 270)



        self.gridLabel = QLabel(self)
        self.gridLabel.setText('Grid:')
        self.gridLabel.move(20, 320)
        self.gridLabel.resize(100, 20)
        self.gridLabel.adjustSize()
 
        self.gridBox = QCheckBox(self)
        self.gridBox.stateChanged.connect(self.displayGrid)
        self.gridBox.resize(300,32)
        self.gridBox.move(self.lineEditXPos, 320)
        
 
        
        self.defaultButtonY = 370
    
        self.defaultButton = QRadioButton("Default", self)
        self.defaultButton.clicked.connect(self.default)
        self.defaultButton.move(20, self.defaultButtonY)
        self.defaultButton.adjustSize()
    
     
  
    
        self.normalButton = QRadioButton("Normalization", self)
        self.normalButton.clicked.connect(self.normalize)
        self.normalButton.move(20, self.defaultButtonY + 50)
        self.normalButton.adjustSize()
    
        

        self.staggerButton = QRadioButton("Stagger", self)
        self.staggerButton.clicked.connect(self.stagger)
        self.staggerButton.move(20, self.defaultButtonY + 100)
        self.staggerButton.adjustSize()



             
        self.defaultCheck = False        
        self.normalizeCheck = False
        self.staggerCheck = False


        self.staggerValue = 0























        self.labelXPos2 = self.labelXPos + 1000

        self.lineEditXPos2 = self.lineEditXPos + 1000

        self.okButtonXPos2 = self.okButtonXPos + 1000

 

     
        self.nameLabelTitle2 = QLabel(self)
        self.nameLabelTitle2.setText('Title:')
        self.nameLabelTitle2.move(self.labelXPos2, 70)
        self.nameLabelTitle2.resize(100, 20)
        self.nameLabelTitle2.adjustSize()
 
        self.lineTitle2 = QLineEdit(self)
        self.lineTitle2.move(self.lineEditXPos2, 70)
        self.lineTitle2.resize(320, 32)

        iobuttonTitle2 = QPushButton('OK', self)
        iobuttonTitle2.clicked.connect(self.changeTitle2)
        iobuttonTitle2.resize(200,32)
        iobuttonTitle2.move(self.okButtonXPos2, 70)
     
               

        
        self.nameLabelX2 = QLabel(self)
        self.nameLabelX2.setText('X-Axis Name:')
        self.nameLabelX2.move(self.labelXPos2, 120)
        self.nameLabelX2.resize(100, 20)
        self.nameLabelX2.adjustSize()

 
        self.lineX2 = QLineEdit(self)
        self.lineX2.move(self.lineEditXPos2, 120)
        self.lineX2.resize(self.lineEditWidth, self.lineEditHeight)


        iobuttonX2 = QPushButton('OK', self)
        iobuttonX2.clicked.connect(self.change_Xaxis_Name2)
        iobuttonX2.resize(self.okButtonWidth, self.okButtonHeight)
        iobuttonX2.move(self.okButtonXPos2, 120)





        self.nameLabelY2 = QLabel(self)
        self.nameLabelY2.setText('Y-Axis Name:')
        self.nameLabelY2.move(self.labelXPos2, 170)
        self.nameLabelY2.resize(100, 20)
        self.nameLabelY2.adjustSize()

 
        self.lineY2 = QLineEdit(self)
        self.lineY2.move(self.lineEditXPos2, 170)
        self.lineY2.resize(self.lineEditWidth, self.lineEditHeight)



        iobuttonY2 = QPushButton('OK', self)
        iobuttonY2.clicked.connect(self.change_Yaxis_Name2)
        iobuttonY2.resize(self.okButtonWidth, self.okButtonHeight)
        iobuttonY2.move(self.okButtonXPos2, 170)



        self.minXLabel2 = QLabel(self)
        self.minXLabel2.setText('X-Min, X-Max:')
        self.minXLabel2.move(self.labelXPos2, 220)
        self.minXLabel2.resize(100, 20)
        self.minXLabel2.adjustSize()

 
        self.lineXMin2 = QLineEdit(self)
        self.lineXMin2.move(self.lineEditXPos2, 220)
        self.lineXMin2.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight) 


          
        self.lineXMax2 = QLineEdit(self)
        self.lineXMax2.move(self.lineEditXPos2 + self.lineEditWidth / 2 + 10, 220)
        self.lineXMax2.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight)


        XMaxButton2 = QPushButton('OK', self)
        XMaxButton2.clicked.connect(self.clickMethodMaxX2)
        XMaxButton2.resize(self.okButtonWidth, self.okButtonHeight)
        XMaxButton2.move(self.okButtonXPos2, 220)

        self.minYLabel2 = QLabel(self)
        self.minYLabel2.setText('Y-Min, Y-Max:')
        self.minYLabel2.move(self.labelXPos2, 270)
        self.minYLabel2.resize(100, 20)
        self.minYLabel2.adjustSize()

 
        self.lineYMin2 = QLineEdit(self)
        self.lineYMin2.move(self.lineEditXPos2, 270)
        self.lineYMin2.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight) 


          
        self.lineYMax2 = QLineEdit(self)
        self.lineYMax2.move(self.lineEditXPos2 + self.lineEditWidth / 2 + 10, 270)
        self.lineYMax2.resize(self.lineEditWidth / 2 - 10, self.lineEditHeight)


        YMaxButton2 = QPushButton('OK', self)
        YMaxButton2.clicked.connect(self.clickMethodMaxY2)
        YMaxButton2.resize(self.okButtonWidth, self.okButtonHeight)
        YMaxButton2.move(self.okButtonXPos2, 270)



        self.gridLabel2 = QLabel(self)
        self.gridLabel2.setText('Grid:')
        self.gridLabel2.move(self.labelXPos2, 320)
        self.gridLabel2.resize(100, 20)
        self.gridLabel2.adjustSize()
 
        self.gridBox2 = QCheckBox(self)
        self.gridBox2.stateChanged.connect(self.displayGrid2)
        self.gridBox2.resize(300,32)
        self.gridBox2.move(self.lineEditXPos2, 320)
        



        self.defaultButton2Y = 370
    
        self.defaultButton2 = QRadioButton("Default", self)
        self.defaultButton2.clicked.connect(self.default2)
        self.defaultButton2.move(320+700, self.defaultButton2Y)
        self.defaultButton2.adjustSize()
    
     
  
    
        self.normalButton2 = QRadioButton("Normalization", self)
        self.normalButton2.clicked.connect(self.normalize2)
        self.normalButton2.move(320+700, self.defaultButton2Y + 50)
        self.normalButton2.adjustSize()
    
        

        self.staggerButton2 = QRadioButton("Stagger", self)
        self.staggerButton2.clicked.connect(self.stagger2)
        self.staggerButton2.move(320+700, self.defaultButton2Y + 100)
        self.staggerButton2.adjustSize()



             

    
        self.defaultCheck2 = False        
        self.normalizeCheck2 = False
        self.staggerCheck2 = False


        self.staggerValue2 = 0






  
 
 

        self.energyValue1 = QLineEdit(self)
        self.energyValue1.move(460, 440)
        self.energyValue1.resize(self.lineEditWidth/2, self.lineEditHeight)

        
        self.energyValue2 = QLineEdit(self)
        self.energyValue2.move(460, 480)
        self.energyValue2.resize(self.lineEditWidth/2, self.lineEditHeight)
                
        


        eValButton1 = QPushButton('Remove Values', self)
        eValButton1.clicked.connect(self.removeValues)
        eValButton1.resize(self.okButtonWidth, self.okButtonHeight)
        eValButton1.move(640, 460)



 

        correctButton = QPushButton('Save Changes, Correct Slope', self)
        correctButton.clicked.connect(self.correct)
        correctButton.resize(self.okButtonWidth+220, self.okButtonHeight+10)
        correctButton.move(self.okButtonXPos-100, 540)

    def correct(self):
        

        print("\n")
        fileList2.append(self.combo.currentText())
        
        for i in range(len(fileList2)):
                

        
            
    
            data_fname1 = self.combo.currentText()
            
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
    
    
            ax2.plot( data1[:,0] , data1[:,1]/max(data1[:,1]) - data1[0, 1]/max(data1[:,1]), label = self.combo.currentText() )



        tempx2 = float(self.energyValue2.text())
        tempx1 = float(self.energyValue1.text())

        x2 = float(min(data1.flatten(), key=lambda x:abs(x-tempx2)))
        x1 = float(min(data1.flatten(), key=lambda x:abs(x-tempx1)))

        xdata1 = data1[:,0]
        
        xdata1 = xdata1.tolist()

        yLoc2 = xdata1.index(x2)
        yLoc1 = xdata1.index(x1)
        
 

        print("y loc values")
        print(yLoc2)
        print(yLoc1)


        y2 = float(data1[yLoc2, 1])
        y1 = float(data1[yLoc1, 1])
 

        print(min(data1.flatten(), key=lambda x:abs(x-x2)))
        print(min(data1.flatten(), key=lambda x:abs(x-x1)))


        slope = (y2-y1) / (x2-x1)
  
 
        print("Values:\n")
        
        print("y2")
        print(y2)
        print("\n")

        print("y1")
        print(y1)
        print("\n")

        print("x2")
        print(x2)
        print("\n")

        print("x1")
        print(x1)
        print("\n")

        print("slope")
        print(slope)
        print("\n")
        
        b = y1 - (slope * x1)

        print("b")        
        print(b)
        print("\n")
         
        
        print("data 1 length")        
        print(len(data1))
        
        
        yline = (slope * data1[:,0]) + b
        
        ynew = data1[:,1] - yline
 

        if(self.defaultCheck == True):
            
            ax1.plot(data1[:,0] , ynew)
            fig2.canvas.draw()

        elif(self.normalizeCheck == True):
             
            ax1.plot( data1[:,0] , ynew/max(ynew), label = self.combo.currentText())
            fig2.canvas.draw()        
        
        elif(self.staggerCheck == False):
            ax1.plot(data1[:,0] , ynew + self.staggerValue, label = self.combo.currentText())
            fig2.canvas.draw()
            
            
            self.staggerValue += 0.5
        else:
            ax1.plot(data1[:,0] , ynew)
            fig2.canvas.draw()
        
         
        
        
        
        print(ynew)
        
        
        
        
        
         

    def removeValues(self):
                        

        print("\n")
        fileList.append(self.combo.currentText())
        
        for i in range(len(fileList)):
                

        
            
    
            data_fname1 = self.combo.currentText()
            
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
    
    
            ax1.plot( data1[:,0] , data1[:,1]/max(data1[:,1]) - data1[0, 1]/max(data1[:,1]), label = self.combo.currentText() )



        tempx2 = float(self.energyValue2.text())
        tempx1 = float(self.energyValue1.text())

        x2 = float(min(data1.flatten(), key=lambda x:abs(x-tempx2)))
        x1 = float(min(data1.flatten(), key=lambda x:abs(x-tempx1)))

        xdata1 = data1[:,0]
        
        xdata1 = xdata1.tolist()

        yLoc2 = xdata1.index(x2)
        yLoc1 = xdata1.index(x1)
        
 

        print("y loc values")
        print(yLoc2)
        print(yLoc1)


        

        y2 = float(data1[yLoc2, 1])
        y1 = float(data1[yLoc1, 1])
 

 

        


        print(min(data1.flatten(), key=lambda x:abs(x-x2)))
        print(min(data1.flatten(), key=lambda x:abs(x-x1)))


        slope = (y2-y1) / (x2-x1)
  
 
        print("Values:\n")
        
        print("y2")
        print(y2)
        print("\n")

        print("y1")
        print(y1)
        print("\n")

        print("x2")
        print(x2)
        print("\n")

        print("x1")
        print(x1)
        print("\n")

        print("slope")
        print(slope)
        print("\n")
        
        b = y1 - (slope * x1)

        print("b")        
        print(b)
        print("\n")
         
        
        print("data 1 length")        
        print(len(data1))
        
        
        yline = (slope * data1[:,0]) + b
        ynew = data1[:,1] - yline
        ax1.plot(data1[:,0] , ynew)
        
        
        fig.canvas.draw()
        
        
        print(ynew)
        
        
        

            
        
        



    def default(self, state):

        self.defaultCheck = True          
        self.normalizeCheck = False
        self.staggerCheck = False

        self.staggerValue = 0
                
        
                
        ax1.cla()
        
        
        for i in range(len(fileList)):
                
            data_fname1 = fileList[i]
                   
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
         
            ax1.plot( data1[:,0] , data1[:,1]/max(data1[:,1]), label = self.combo.currentText() )
            fig.canvas.draw()


 

    def normalize(self, state):


        self.defaultCheck = False          
        self.normalizeCheck = True
        self.staggerCheck = False
        
        self.staggerValue = 0
                
                
        
        ax1.cla()
        
        
        for i in range(len(fileList)):
                
            data_fname1 = fileList[i]
                   
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
                     
                
            min_data = min(data1[:,1])                   
            
            
            data1[:,1] = data1[:,1]-min_data
    
        
        
            max_data = max(data1[:,1])
        
            data1[:,1] = data1[:,1]/max_data
    
            
         
            ax1.plot( data1[:,0] , data1[:,1]/max(data1[:,1]), label = self.combo.currentText())
            fig.canvas.draw()



    def stagger(self, state):


        self.defaultCheck = False          
        self.normalizeCheck = True
        self.staggerCheck = False


         
        ax1.cla()
        
        
        for i in range(len(fileList)):
                
            data_fname1 = fileList[i]
                   
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
                     
                
            min_data = min(data1[:,1])                   
            
            
            data1[:,1] = data1[:,1]-min_data
    
        
        
            max_data = max(data1[:,1])
        
            data1[:,1] = data1[:,1]/max_data
    
            
            
            


            ax1.plot(data1[:,0] , data1[:,1] + self.staggerValue, label = self.combo.currentText())
            
            
            

            
            fig.canvas.draw()            
            
            self.staggerValue += 0.5

  







    def change_Xaxis_Name(self):                
        ax1.set_xlabel(self.lineX.text(), fontsize=30)
        fig.canvas.draw()        


    def change_Yaxis_Name(self):                
        ax1.set_ylabel(self.lineY.text(), fontsize=30)
        fig.canvas.draw()        

 




    def changeTitle(self):                
        fig.suptitle(self.lineTitle.text(), fontsize=30)
        fig.canvas.draw()




  



    def clickMethodMaxX(self):
        ax1.set_xlim(int(self.lineXMin.text()), int(self.lineXMax.text()))
        fig.canvas.draw()    


    def clickMethodMaxY(self):
        ax1.set_ylim(int(self.lineYMin.text()), int(self.lineYMax.text()))
        fig.canvas.draw() 

    def displayGrid(self, state):

        if (state == Qt.Checked):

            ax1.grid(True)
        else:
            ax1.grid(False)

        fig.canvas.draw()
 
                 
    def clickMethod(self, state):
        
        
        print(fileList)
                       
        if(self.combo.currentText() not in fileList):
            
            
            fileList.append(self.combo.currentText())

            data_fname1 = self.combo.currentText()
            
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
        
            
            print(data1)
            print(data1[0, 0])
            print(data1[0, 1])
            
            print(data1[1, 0])
            print(data1[1, 1])
            

            
    
    
            if(self.normalizeCheck == True):
                
                
                data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
        
                    
                min_data = min(data1[:,1])                   
                
                
                data1[:,1] = data1[:,1]-min_data
        
            
            
                max_data = max(data1[:,1])
            
                data1[:,1] = data1[:,1]/max_data
    
         
         
        
        
            
            
            ax1.plot( data1[:,0] , data1[:,1]/max(data1[:,1]) - data1[0, 1]/max(data1[:,1]), label = self.combo.currentText() )
            fig.canvas.draw()
            










        

            
        
        














    def change_Xaxis_Name2(self):                
        ax2.set_xlabel(self.lineX2.text(), fontsize=30)
        fig2.canvas.draw()        


    def change_Yaxis_Name2(self):                
        ax2.set_ylabel(self.lineY2.text(), fontsize=30)
        fig2.canvas.draw()        

 




    def changeTitle2(self):                
        fig2.suptitle(self.lineTitle2.text(), fontsize=30)
        fig2.canvas.draw()




  



    def clickMethodMaxX2(self):
        ax2.set_xlim(int(self.lineXMin2.text()), int(self.lineXMax2.text()))
        fig2.canvas.draw()    


    def clickMethodMaxY2(self):
        ax2.set_ylim(int(self.lineYMin2.text()), int(self.lineYMax2.text()))
        fig2.canvas.draw() 

    def displayGrid2(self, state):

        if (state == Qt.Checked):

            ax2.grid(True)
        else:
            ax2.grid(False)

        fig2.canvas.draw()
 



    def default2(self, state):

        self.defaultCheck2 = True          
        self.normalizeCheck2 = False
        self.staggerCheck2 = False

        self.staggerValue2 = 0
                
        
                
        ax2.cla()
        
        
        for i in range(len(fileList2)):
                
            data_fname1 = fileList2[i]
                   
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
         
            ax2.plot( data1[:,0] , data1[:,1]/max(data1[:,1]), label = self.combo.currentText() )
            fig2.canvas.draw()

 

    def normalize2(self, state):

        
        self.defaultCheck2 = False          
        self.normalizeCheck2 = True
        self.staggerCheck2 = False
        
        self.staggerValue2 = 0
                
                      
        
        ax2.cla()
        
        
        for i in range(len(fileList2)):
                
            data_fname1 = fileList2[i]
                   
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
                     
                
            min_data = min(data1[:,1])                   
            
            
            data1[:,1] = data1[:,1]-min_data
    
        
        
            max_data = max(data1[:,1])
        
            data1[:,1] = data1[:,1]/max_data
    
            
         
            ax2.plot( data1[:,0] , data1[:,1]/max(data1[:,1]), label = self.combo.currentText())
            fig2.canvas.draw()



 
    def stagger2(self, state):


        self.defaultCheck2 = False          
        self.normalizeCheck2 = True
        self.staggerCheck2 = False


         
        ax2.cla()
        
        
        for i in range(len(fileList2)):
                
            data_fname1 = fileList2[i]
                   
            data1 = np.genfromtxt(data_dir + data_fname1, autostrip = True)
                     
                
            min_data = min(data1[:,1])                   
            
            
            data1[:,1] = data1[:,1]-min_data
    
        
        
            max_data = max(data1[:,1])
        
            data1[:,1] = data1[:,1]/max_data
    
            
            
            


            ax2.plot(data1[:,0] , data1[:,1] + self.staggerValue2, label = self.combo.currentText())
            
            fig2.canvas.draw()            
        
        
        
        
            self.staggerValue2 += 0.5

  







    


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
    
    
    