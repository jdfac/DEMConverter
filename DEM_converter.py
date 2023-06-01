# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DEM_converter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.OutputFolderTB = QtWidgets.QToolButton(self.groupBox)
        self.OutputFolderTB.setObjectName("OutputFolderTB")
        self.gridLayout_2.addWidget(self.OutputFolderTB, 1, 3, 1, 1)
        self.DEMFolderTB = QtWidgets.QToolButton(self.groupBox)
        self.DEMFolderTB.setObjectName("DEMFolderTB")
        self.gridLayout_2.addWidget(self.DEMFolderTB, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.OutputFolderLE = QtWidgets.QLineEdit(self.groupBox)
        self.OutputFolderLE.setObjectName("OutputFolderLE")
        self.gridLayout_2.addWidget(self.OutputFolderLE, 1, 2, 1, 1)
        self.DEMfolderLE = QtWidgets.QLineEdit(self.groupBox)
        self.DEMfolderLE.setObjectName("DEMfolderLE")
        self.gridLayout_2.addWidget(self.DEMfolderLE, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.StateCB = QtWidgets.QComboBox(self.groupBox_2)
        self.StateCB.setObjectName("StateCB")
        self.gridLayout.addWidget(self.StateCB, 0, 1, 1, 1)
        self.YearCB = QtWidgets.QComboBox(self.groupBox_2)
        self.YearCB.setObjectName("YearCB")
        self.gridLayout.addWidget(self.YearCB, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.RunPB = QtWidgets.QPushButton(Form)
        self.RunPB.setObjectName("RunPB")
        self.verticalLayout.addWidget(self.RunPB)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DEM Processor"))
        self.groupBox.setTitle(_translate("Form", "Folder Inputs"))
        self.label.setText(_translate("Form", "DEM Folder:"))
        self.OutputFolderTB.setToolTip(_translate("Form", "Select the folder to save converted DEMs."))
        self.OutputFolderTB.setText(_translate("Form", "..."))
        self.DEMFolderTB.setToolTip(_translate("Form", "Select the folder containing all DEMs."))
        self.DEMFolderTB.setText(_translate("Form", "..."))
        self.label_2.setText(_translate("Form", "Output Folder:"))
        self.OutputFolderLE.setToolTip(_translate("Form", "Select or enter the folder to save processed DEMs."))
        self.OutputFolderLE.setPlaceholderText(_translate("Form", "Select output folder..."))
        self.DEMfolderLE.setToolTip(_translate("Form", "Enter or select the folder containing the DEMs to be processed. "))
        self.DEMfolderLE.setPlaceholderText(_translate("Form", "Select DEM folder..."))
        self.groupBox_2.setTitle(_translate("Form", "Selection"))
        self.label_4.setText(_translate("Form", "Year:"))
        self.label_3.setText(_translate("Form", "State:"))
        self.StateCB.setToolTip(_translate("Form", "Select the state of DEMs you would like to process."))
        self.YearCB.setToolTip(_translate("Form", "Select the year of DEMs you would like to process."))
        self.RunPB.setToolTip(_translate("Form", "Click to process DEMs. "))
        self.RunPB.setText(_translate("Form", "Run"))

