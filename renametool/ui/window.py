# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'renametool/ui/window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(857, 779)
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Window)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.aspectsBox = QtWidgets.QGroupBox(self.groupBox)
        self.aspectsBox.setObjectName("aspectsBox")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.aspectsBox)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_15.setObjectName("checkBox_15")
        self.gridLayout_14.addWidget(self.checkBox_15, 1, 0, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_16.setObjectName("checkBox_16")
        self.gridLayout_14.addWidget(self.checkBox_16, 2, 0, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_19.setObjectName("checkBox_19")
        self.gridLayout_14.addWidget(self.checkBox_19, 5, 0, 1, 1)
        self.checkBox_18 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_18.setObjectName("checkBox_18")
        self.gridLayout_14.addWidget(self.checkBox_18, 4, 0, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_20.setObjectName("checkBox_20")
        self.gridLayout_14.addWidget(self.checkBox_20, 6, 0, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_17.setObjectName("checkBox_17")
        self.gridLayout_14.addWidget(self.checkBox_17, 3, 0, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_14.setObjectName("checkBox_14")
        self.gridLayout_14.addWidget(self.checkBox_14, 0, 0, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.aspectsBox)
        self.checkBox_21.setObjectName("checkBox_21")
        self.gridLayout_14.addWidget(self.checkBox_21, 7, 0, 1, 1)
        self.gridLayout_3.addWidget(self.aspectsBox, 0, 0, 1, 1)
        self.uncheckAllTagsButton = QtWidgets.QPushButton(self.groupBox)
        self.uncheckAllTagsButton.setObjectName("uncheckAllTagsButton")
        self.gridLayout_3.addWidget(self.uncheckAllTagsButton, 7, 0, 1, 1)
        self.newTagsBox = QtWidgets.QGroupBox(self.groupBox)
        self.newTagsBox.setEnabled(True)
        self.newTagsBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.newTagsBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.newTagsBox.setCheckable(False)
        self.newTagsBox.setObjectName("newTagsBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.newTagsBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_3.addWidget(self.newTagsBox, 4, 0, 1, 1)
        self.addTagButton = QtWidgets.QPushButton(self.groupBox)
        self.addTagButton.setObjectName("addTagButton")
        self.gridLayout_3.addWidget(self.addTagButton, 6, 0, 1, 1)
        self.inspiringBox = QtWidgets.QGroupBox(self.groupBox)
        self.inspiringBox.setObjectName("inspiringBox")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.inspiringBox)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.checkBox_23 = QtWidgets.QCheckBox(self.inspiringBox)
        self.checkBox_23.setObjectName("checkBox_23")
        self.gridLayout_16.addWidget(self.checkBox_23, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.inspiringBox, 2, 0, 1, 1)
        self.newTagName = QtWidgets.QLineEdit(self.groupBox)
        self.newTagName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.newTagName.setObjectName("newTagName")
        self.gridLayout_3.addWidget(self.newTagName, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 9, 0, 1, 1)
        self.creatorsBox = QtWidgets.QGroupBox(self.groupBox)
        self.creatorsBox.setObjectName("creatorsBox")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.creatorsBox)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.checkBox_24 = QtWidgets.QCheckBox(self.creatorsBox)
        self.checkBox_24.setObjectName("checkBox_24")
        self.gridLayout_17.addWidget(self.checkBox_24, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.creatorsBox, 1, 0, 1, 1)
        self.nsfwBox = QtWidgets.QGroupBox(self.groupBox)
        self.nsfwBox.setObjectName("nsfwBox")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.nsfwBox)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.checkBox_22 = QtWidgets.QCheckBox(self.nsfwBox)
        self.checkBox_22.setObjectName("checkBox_22")
        self.gridLayout_15.addWidget(self.checkBox_22, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.nsfwBox, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(Window)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.creatorsName = QtWidgets.QLineEdit(self.groupBox_5)
        self.creatorsName.setObjectName("creatorsName")
        self.gridLayout_6.addWidget(self.creatorsName, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 15))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 1)
        self.imageFrame = QtWidgets.QFrame(self.groupBox_5)
        self.imageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageFrame.setObjectName("imageFrame")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.imageFrame)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.imageFrameLabel = QtWidgets.QLabel(self.imageFrame)
        self.imageFrameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageFrameLabel.setObjectName("imageFrameLabel")
        self.gridLayout_11.addWidget(self.imageFrameLabel, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.imageFrame, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.sourceDirectory = QtWidgets.QLineEdit(self.groupBox_6)
        self.sourceDirectory.setMinimumSize(QtCore.QSize(0, 30))
        self.sourceDirectory.setMaximumSize(QtCore.QSize(16777215, 30))
        self.sourceDirectory.setObjectName("sourceDirectory")
        self.gridLayout_7.addWidget(self.sourceDirectory, 1, 0, 1, 1)
        self.loadFilesButton = QtWidgets.QPushButton(self.groupBox_6)
        self.loadFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.gridLayout_7.addWidget(self.loadFilesButton, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_6, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 15))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.currentFileName = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.currentFileName.setFont(font)
        self.currentFileName.setStyleSheet("color: rgb(255, 105, 140);")
        self.currentFileName.setAlignment(QtCore.Qt.AlignCenter)
        self.currentFileName.setObjectName("currentFileName")
        self.gridLayout_2.addWidget(self.currentFileName, 4, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setMinimumSize(QtCore.QSize(0, 15))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.newFileName = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.newFileName.setFont(font)
        self.newFileName.setStyleSheet("color: rgb(46, 107, 80);")
        self.newFileName.setAlignment(QtCore.Qt.AlignCenter)
        self.newFileName.setObjectName("newFileName")
        self.gridLayout_2.addWidget(self.newFileName, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 110))
        self.groupBox_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.previousImageButton = QtWidgets.QPushButton(self.groupBox_4)
        self.previousImageButton.setMinimumSize(QtCore.QSize(0, 30))
        self.previousImageButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.previousImageButton.setObjectName("previousImageButton")
        self.gridLayout_5.addWidget(self.previousImageButton, 0, 0, 1, 1)
        self.nextImageButton = QtWidgets.QPushButton(self.groupBox_4)
        self.nextImageButton.setMinimumSize(QtCore.QSize(0, 30))
        self.nextImageButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.nextImageButton.setObjectName("nextImageButton")
        self.gridLayout_5.addWidget(self.nextImageButton, 0, 1, 1, 1)
        self.renameButton = QtWidgets.QPushButton(self.groupBox_4)
        self.renameButton.setMinimumSize(QtCore.QSize(0, 30))
        self.renameButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.renameButton.setObjectName("renameButton")
        self.gridLayout_5.addWidget(self.renameButton, 1, 0, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 2, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(Window)
        self.groupBox_9.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_9.setMaximumSize(QtCore.QSize(170, 16777215))
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.mediumsBox = QtWidgets.QGroupBox(self.groupBox_9)
        self.mediumsBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mediumsBox.setObjectName("mediumsBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.mediumsBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.tag_2D = QtWidgets.QCheckBox(self.mediumsBox)
        self.tag_2D.setObjectName("tag_2D")
        self.gridLayout_8.addWidget(self.tag_2D, 0, 0, 1, 1)
        self.tag_3D = QtWidgets.QCheckBox(self.mediumsBox)
        self.tag_3D.setObjectName("tag_3D")
        self.gridLayout_8.addWidget(self.tag_3D, 1, 0, 1, 1)
        self.tag_Traditional = QtWidgets.QCheckBox(self.mediumsBox)
        self.tag_Traditional.setObjectName("tag_Traditional")
        self.gridLayout_8.addWidget(self.tag_Traditional, 2, 0, 1, 1)
        self.tag_Photograph = QtWidgets.QCheckBox(self.mediumsBox)
        self.tag_Photograph.setObjectName("tag_Photograph")
        self.gridLayout_8.addWidget(self.tag_Photograph, 3, 0, 1, 1)
        self.gridLayout_12.addWidget(self.mediumsBox, 0, 0, 1, 1)
        self.stylesBox = QtWidgets.QGroupBox(self.groupBox_9)
        self.stylesBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.stylesBox.setFont(font)
        self.stylesBox.setObjectName("stylesBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.stylesBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tag_SemiRealistic = QtWidgets.QCheckBox(self.stylesBox)
        self.tag_SemiRealistic.setObjectName("tag_SemiRealistic")
        self.gridLayout_10.addWidget(self.tag_SemiRealistic, 2, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.stylesBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_10.addWidget(self.checkBox_3, 4, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.stylesBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_10.addWidget(self.checkBox_2, 3, 0, 1, 1)
        self.tag_Realistic = QtWidgets.QCheckBox(self.stylesBox)
        self.tag_Realistic.setObjectName("tag_Realistic")
        self.gridLayout_10.addWidget(self.tag_Realistic, 1, 0, 1, 1)
        self.tag_HyperRealistic = QtWidgets.QCheckBox(self.stylesBox)
        self.tag_HyperRealistic.setObjectName("tag_HyperRealistic")
        self.gridLayout_10.addWidget(self.tag_HyperRealistic, 0, 0, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.stylesBox)
        self.checkBox_13.setObjectName("checkBox_13")
        self.gridLayout_10.addWidget(self.checkBox_13, 5, 0, 1, 1)
        self.gridLayout_12.addWidget(self.stylesBox, 1, 0, 1, 1)
        self.subjectsBox = QtWidgets.QGroupBox(self.groupBox_9)
        self.subjectsBox.setObjectName("subjectsBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.subjectsBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.checkBox_7 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout_13.addWidget(self.checkBox_7, 4, 0, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_11.setObjectName("checkBox_11")
        self.gridLayout_13.addWidget(self.checkBox_11, 8, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_13.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_13.addWidget(self.checkBox_10, 7, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_9.setObjectName("checkBox_9")
        self.gridLayout_13.addWidget(self.checkBox_9, 6, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_13.addWidget(self.checkBox_6, 3, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_13.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_8.setObjectName("checkBox_8")
        self.gridLayout_13.addWidget(self.checkBox_8, 5, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_13.addWidget(self.checkBox_5, 2, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.subjectsBox)
        self.checkBox_12.setObjectName("checkBox_12")
        self.gridLayout_13.addWidget(self.checkBox_12, 9, 0, 1, 1)
        self.gridLayout_12.addWidget(self.subjectsBox, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem1, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_9, 0, 0, 1, 1)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MyMaterialRenamer"))
        self.groupBox.setTitle(_translate("Window", "Tags"))
        self.aspectsBox.setTitle(_translate("Window", "Aspects"))
        self.checkBox_15.setText(_translate("Window", "&Form"))
        self.checkBox_16.setText(_translate("Window", "&Composition"))
        self.checkBox_19.setText(_translate("Window", "&Brushwork"))
        self.checkBox_18.setText(_translate("Window", "&Texture"))
        self.checkBox_20.setText(_translate("Window", "&Matte"))
        self.checkBox_17.setText(_translate("Window", "&Expression"))
        self.checkBox_14.setText(_translate("Window", "&Color"))
        self.checkBox_21.setText(_translate("Window", "&GraphicDesign"))
        self.uncheckAllTagsButton.setText(_translate("Window", "&Uncheck all tags"))
        self.newTagsBox.setTitle(_translate("Window", "New tags"))
        self.addTagButton.setText(_translate("Window", "&Add tag"))
        self.inspiringBox.setTitle(_translate("Window", "INSPIRING"))
        self.checkBox_23.setText(_translate("Window", "&Inspiring"))
        self.newTagName.setPlaceholderText(_translate("Window", "New tag name"))
        self.creatorsBox.setTitle(_translate("Window", "Creators"))
        self.checkBox_24.setText(_translate("Window", "&Studios"))
        self.nsfwBox.setTitle(_translate("Window", "NSFW"))
        self.checkBox_22.setText(_translate("Window", "&NSFW"))
        self.groupBox_3.setTitle(_translate("Window", "Renamer"))
        self.groupBox_5.setTitle(_translate("Window", "Image"))
        self.creatorsName.setPlaceholderText(_translate("Window", "John Smith"))
        self.label_2.setText(_translate("Window", "Creator\'s name:"))
        self.imageFrameLabel.setText(_translate("Window", "Image goes here"))
        self.groupBox_6.setTitle(_translate("Window", "Directories"))
        self.loadFilesButton.setText(_translate("Window", "&Load files"))
        self.label.setText(_translate("Window", "Source directory"))
        self.groupBox_2.setTitle(_translate("Window", "Files"))
        self.label_5.setText(_translate("Window", "New filename:"))
        self.currentFileName.setText(_translate("Window", "[Load in the images first]"))
        self.label_4.setText(_translate("Window", "Current filename:"))
        self.newFileName.setText(_translate("Window", "[New filename goes here]"))
        self.groupBox_4.setTitle(_translate("Window", "Navigation/Submit"))
        self.previousImageButton.setText(_translate("Window", "&Previous Image"))
        self.nextImageButton.setText(_translate("Window", "&Next Image"))
        self.renameButton.setText(_translate("Window", "&Rename"))
        self.groupBox_9.setTitle(_translate("Window", "Tags"))
        self.mediumsBox.setTitle(_translate("Window", "Mediums"))
        self.tag_2D.setText(_translate("Window", "&2D"))
        self.tag_3D.setText(_translate("Window", "&3D"))
        self.tag_Traditional.setText(_translate("Window", "&Traditional"))
        self.tag_Photograph.setText(_translate("Window", "&Photograph"))
        self.stylesBox.setTitle(_translate("Window", "Styles"))
        self.tag_SemiRealistic.setText(_translate("Window", "&SemiRealistic"))
        self.checkBox_3.setText(_translate("Window", "&VeryStylized"))
        self.checkBox_2.setText(_translate("Window", "&Stylized"))
        self.tag_Realistic.setText(_translate("Window", "&Realistic"))
        self.tag_HyperRealistic.setText(_translate("Window", "&HyperRealistic"))
        self.checkBox_13.setText(_translate("Window", "&Abstract"))
        self.subjectsBox.setTitle(_translate("Window", "Subjects"))
        self.checkBox_7.setText(_translate("Window", "&Nature"))
        self.checkBox_11.setText(_translate("Window", "&Buildings"))
        self.checkBox_4.setText(_translate("Window", "&Vehicles"))
        self.checkBox_10.setText(_translate("Window", "&Robots"))
        self.checkBox_9.setText(_translate("Window", "&Weapons"))
        self.checkBox_6.setText(_translate("Window", "&Objects"))
        self.checkBox.setText(_translate("Window", "&Characters"))
        self.checkBox_8.setText(_translate("Window", "&Technology"))
        self.checkBox_5.setText(_translate("Window", "&Landscapes"))
        self.checkBox_12.setText(_translate("Window", "&Caricatures"))
