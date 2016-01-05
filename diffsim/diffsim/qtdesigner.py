# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created: Mon Jan 23 22:32:03 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName(_fromUtf8("MplMainWindow"))
        MplMainWindow.resize(690, 431)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MplMainWindow.sizePolicy().hasHeightForWidth())
        MplMainWindow.setSizePolicy(sizePolicy)
        MplMainWindow.setWindowTitle(QtGui.QApplication.translate("MplMainWindow", "Diffusion Simulator", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MplMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mpl = MplWidget(self.centralwidget)
        self.mpl.setObjectName(_fromUtf8("mpl"))
        self.horizontalLayout.addWidget(self.mpl)
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_7 = QtGui.QLabel(self.frame_4)
        self.label_7.setText(QtGui.QApplication.translate("MplMainWindow", "Physical parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_5.addWidget(self.label_7)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_8 = QtGui.QLabel(self.frame_4)
        self.label_8.setText(QtGui.QApplication.translate("MplMainWindow", "Box size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_L = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_L.setText(QtGui.QApplication.translate("MplMainWindow", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_L.setObjectName(_fromUtf8("lineEdit_L"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_L)
        self.label_9 = QtGui.QLabel(self.frame_4)
        self.label_9.setText(QtGui.QApplication.translate("MplMainWindow", "Diffusion coefficient", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_D = QtGui.QLineEdit(self.frame_4)
        self.lineEdit_D.setText(QtGui.QApplication.translate("MplMainWindow", "1.", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_D.setObjectName(_fromUtf8("lineEdit_D"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_D)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_3 = QtGui.QFrame(self.frame)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setText(QtGui.QApplication.translate("MplMainWindow", "Run parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_4.addWidget(self.label_5)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setText(QtGui.QApplication.translate("MplMainWindow", "Simulation time", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_timemax = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_timemax.setText(QtGui.QApplication.translate("MplMainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_timemax.setObjectName(_fromUtf8("lineEdit_timemax"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_timemax)
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setText(QtGui.QApplication.translate("MplMainWindow", "nx", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setText(QtGui.QApplication.translate("MplMainWindow", "ny", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_nx = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_nx.setText(QtGui.QApplication.translate("MplMainWindow", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_nx.setObjectName(_fromUtf8("lineEdit_nx"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_nx)
        self.lineEdit_ny = QtGui.QLineEdit(self.frame_3)
        self.lineEdit_ny.setText(QtGui.QApplication.translate("MplMainWindow", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_ny.setObjectName(_fromUtf8("lineEdit_ny"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_ny)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setText(QtGui.QApplication.translate("MplMainWindow", "Initialization", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.radioButton_pointsource = QtGui.QRadioButton(self.frame_2)
        self.radioButton_pointsource.setText(QtGui.QApplication.translate("MplMainWindow", "Point source", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_pointsource.setChecked(True)
        self.radioButton_pointsource.setObjectName(_fromUtf8("radioButton_pointsource"))
        self.verticalLayout_3.addWidget(self.radioButton_pointsource)
        self.radioButton_step = QtGui.QRadioButton(self.frame_2)
        self.radioButton_step.setText(QtGui.QApplication.translate("MplMainWindow", "Step", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_step.setObjectName(_fromUtf8("radioButton_step"))
        self.verticalLayout_3.addWidget(self.radioButton_step)
        self.radioButton_cross = QtGui.QRadioButton(self.frame_2)
        self.radioButton_cross.setText(QtGui.QApplication.translate("MplMainWindow", "Cross", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_cross.setObjectName(_fromUtf8("radioButton_cross"))
        self.verticalLayout_3.addWidget(self.radioButton_cross)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_run = QtGui.QPushButton(self.frame)
        self.pushButton_run.setText(QtGui.QApplication.translate("MplMainWindow", "Run Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.gridLayout.addWidget(self.pushButton_run, 0, 0, 1, 1)
        self.pushButton_close = QtGui.QPushButton(self.frame)
        self.pushButton_close.setText(QtGui.QApplication.translate("MplMainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setObjectName(_fromUtf8("pushButton_close"))
        self.gridLayout.addWidget(self.pushButton_close, 1, 1, 1, 1)
        self.pushButton_stop = QtGui.QPushButton(self.frame)
        self.pushButton_stop.setText(QtGui.QApplication.translate("MplMainWindow", "Stop Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.gridLayout.addWidget(self.pushButton_stop, 0, 1, 1, 1)
        self.pushButton_clear = QtGui.QPushButton(self.frame)
        self.pushButton_clear.setText(QtGui.QApplication.translate("MplMainWindow", "Clear graph", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_clear.setObjectName(_fromUtf8("pushButton_clear"))
        self.gridLayout.addWidget(self.pushButton_clear, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("MplMainWindow", "Copyleft Yannick Hallez, Chemical Engineering Laboratory (LGC) and University of Toulouse", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        MplMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MplMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MplMainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MplMainWindow)
        QtCore.QObject.connect(self.pushButton_close, QtCore.SIGNAL(_fromUtf8("clicked()")), MplMainWindow.close)
        QtCore.QObject.connect(self.pushButton_run, QtCore.SIGNAL(_fromUtf8("clicked()")), MplMainWindow.run)
        QtCore.QObject.connect(self.pushButton_stop, QtCore.SIGNAL(_fromUtf8("clicked()")), MplMainWindow.stop)
        QtCore.QObject.connect(self.pushButton_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), MplMainWindow.clear)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        pass

from mplwidget import MplWidget