# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManagerLandingPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1240, 936)
        MainWindow.setStyleSheet("margin:0;\n"
"padding:0;\n"
"background:#FFFFFF;")
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setStyleSheet("background:#202D31;\n"
"margin:0;\n"
"padding:0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(230, 150))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("text-align:center;\n"
"padding:10px;\n"
"color:white;\n"
"border:none;\n"
"margin-top:20px;")
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(5)
        self.label.setMidLineWidth(1)
        self.label.setIndent(-3)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_3.setStyleSheet("color:white;\n"
"padding:0px;\n"
"border:none;\n"
"text-align:cneter;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboardBtn = QtWidgets.QPushButton(self.frame_4)
        self.dashboardBtn.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dashboardBtn.setFont(font)
        self.dashboardBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dashboardBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    padding: 15px;\n"
"    border: none;\n"
"    text-align: center;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0C8C4C;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Images/Images/icons8-dashboard-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboardBtn.setIcon(icon)
        self.dashboardBtn.setIconSize(QtCore.QSize(50, 50))
        self.dashboardBtn.setObjectName("dashboardBtn")
        self.verticalLayout.addWidget(self.dashboardBtn, 0, QtCore.Qt.AlignLeft)
        self.QuestionaryPageBtn = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QuestionaryPageBtn.setFont(font)
        self.QuestionaryPageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QuestionaryPageBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    padding: 15px;\n"
"    border: none;\n"
"    text-align: center;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0C8C4C;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Images/Images/icons8-result-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QuestionaryPageBtn.setIcon(icon1)
        self.QuestionaryPageBtn.setIconSize(QtCore.QSize(40, 40))
        self.QuestionaryPageBtn.setObjectName("QuestionaryPageBtn")
        self.verticalLayout.addWidget(self.QuestionaryPageBtn)
        self.ResultsPageBtn = QtWidgets.QPushButton(self.frame_4)
        self.ResultsPageBtn.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ResultsPageBtn.setFont(font)
        self.ResultsPageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ResultsPageBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    padding: 15px;\n"
"    border: none;\n"
"    text-align: center;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0C8C4C;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Images/Images/icons8-improvement-100 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ResultsPageBtn.setIcon(icon2)
        self.ResultsPageBtn.setIconSize(QtCore.QSize(50, 50))
        self.ResultsPageBtn.setObjectName("ResultsPageBtn")
        self.verticalLayout.addWidget(self.ResultsPageBtn, 0, QtCore.Qt.AlignLeft)
        self.SettingsPageBtn = QtWidgets.QPushButton(self.frame_4)
        self.SettingsPageBtn.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SettingsPageBtn.setFont(font)
        self.SettingsPageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SettingsPageBtn.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    padding: 15px;\n"
"    border: none;\n"
"    text-align: center;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #0C8C4C;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Images/Images/icons8-gear-100.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SettingsPageBtn.setIcon(icon3)
        self.SettingsPageBtn.setIconSize(QtCore.QSize(50, 50))
        self.SettingsPageBtn.setObjectName("SettingsPageBtn")
        self.verticalLayout.addWidget(self.SettingsPageBtn, 0, QtCore.Qt.AlignLeft)
        self.frame_12 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout.addWidget(self.frame_12)
        self.gridLayout.addWidget(self.frame_4, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background:#fff;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.Dashboard = QtWidgets.QWidget()
        self.Dashboard.setObjectName("Dashboard")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.Dashboard)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.LineGraphBtn = QtWidgets.QFrame(self.Dashboard)
        self.LineGraphBtn.setMinimumSize(QtCore.QSize(0, 350))
        self.LineGraphBtn.setMaximumSize(QtCore.QSize(16777215, 355))
        self.LineGraphBtn.setStyleSheet("\n"
"\n"
"border-radius:15px;")
        self.LineGraphBtn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LineGraphBtn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LineGraphBtn.setObjectName("LineGraphBtn")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.LineGraphBtn)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.PieGraphLabel = QtWidgets.QLabel(self.LineGraphBtn)
        self.PieGraphLabel.setStyleSheet("text-align:center;")
        self.PieGraphLabel.setText("")
        self.PieGraphLabel.setObjectName("PieGraphLabel")
        self.gridLayout_8.addWidget(self.PieGraphLabel, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.LineGraphBtn, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.Dashboard)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("padding:10px;\n"
"background:#F2F2F2;\n"
"border-radius:10px;\n"
"color:black;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_11.addWidget(self.label_3, 0, 0, 1, 2)
        self.frame_15 = QtWidgets.QFrame(self.Dashboard)
        self.frame_15.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.frame_15)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(180, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_5.setStyleSheet("\n"
"background:#F2F2F2;\n"
"border-radius:15px;\n"
"color:black;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.totalScoreLable = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.totalScoreLable.setFont(font)
        self.totalScoreLable.setStyleSheet("text-align:center;\n"
"color:black;")
        self.totalScoreLable.setObjectName("totalScoreLable")
        self.gridLayout_4.addWidget(self.totalScoreLable, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("text-align:center;\n"
"color:black;")
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_5, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.frame_15, 1, 0, 1, 2)
        self.frame_65 = QtWidgets.QFrame(self.Dashboard)
        self.frame_65.setMinimumSize(QtCore.QSize(0, 350))
        self.frame_65.setMaximumSize(QtCore.QSize(16777215, 355))
        self.frame_65.setStyleSheet("\n"
"border-radius:15px;")
        self.frame_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_65.setObjectName("frame_65")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_65)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lineGraphLabel = QtWidgets.QLabel(self.frame_65)
        self.lineGraphLabel.setText("")
        self.lineGraphLabel.setObjectName("lineGraphLabel")
        self.gridLayout_9.addWidget(self.lineGraphLabel, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.frame_65, 3, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.Dashboard)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_66 = QtWidgets.QFrame(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy)
        self.frame_66.setStyleSheet("\n"
"background:#f5f5f5;\n"
"border-radius:15px;")
        self.frame_66.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_66.setObjectName("frame_66")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_66)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.category1Graph = QtWidgets.QLabel(self.frame_66)
        self.category1Graph.setStyleSheet("text-align:center;")
        self.category1Graph.setText("")
        self.category1Graph.setObjectName("category1Graph")
        self.gridLayout_10.addWidget(self.category1Graph, 0, 0, 1, 1)
        self.category3Graph = QtWidgets.QLabel(self.frame_66)
        self.category3Graph.setStyleSheet("text-align:center;")
        self.category3Graph.setText("")
        self.category3Graph.setObjectName("category3Graph")
        self.gridLayout_10.addWidget(self.category3Graph, 0, 2, 1, 1)
        self.category6Graph = QtWidgets.QLabel(self.frame_66)
        self.category6Graph.setStyleSheet("text-align:center;")
        self.category6Graph.setText("")
        self.category6Graph.setObjectName("category6Graph")
        self.gridLayout_10.addWidget(self.category6Graph, 1, 2, 1, 1)
        self.category4Graph = QtWidgets.QLabel(self.frame_66)
        self.category4Graph.setStyleSheet("text-align:center;")
        self.category4Graph.setText("")
        self.category4Graph.setObjectName("category4Graph")
        self.gridLayout_10.addWidget(self.category4Graph, 1, 0, 1, 1)
        self.category5Graph = QtWidgets.QLabel(self.frame_66)
        self.category5Graph.setStyleSheet("text-align:center;")
        self.category5Graph.setText("")
        self.category5Graph.setObjectName("category5Graph")
        self.gridLayout_10.addWidget(self.category5Graph, 1, 1, 1, 1)
        self.category2Graph = QtWidgets.QLabel(self.frame_66)
        self.category2Graph.setStyleSheet("text-align:center;")
        self.category2Graph.setText("")
        self.category2Graph.setObjectName("category2Graph")
        self.gridLayout_10.addWidget(self.category2Graph, 0, 1, 1, 1)
        self.gridLayout_14.addWidget(self.frame_66, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.frame_7, 4, 0, 1, 2)
        self.stackedWidget.addWidget(self.Dashboard)
        self.QuestionariesPage = QtWidgets.QWidget()
        self.QuestionariesPage.setObjectName("QuestionariesPage")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.QuestionariesPage)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem = QtWidgets.QSpacerItem(629, 270, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem, 2, 1, 1, 1)
        self.QuestionOneLabel = QtWidgets.QLabel(self.QuestionariesPage)
        self.QuestionOneLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.QuestionOneLabel.setFont(font)
        self.QuestionOneLabel.setObjectName("QuestionOneLabel")
        self.gridLayout_12.addWidget(self.QuestionOneLabel, 1, 0, 1, 2)
        self.Question2Lable = QtWidgets.QLabel(self.QuestionariesPage)
        self.Question2Lable.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Question2Lable.setFont(font)
        self.Question2Lable.setObjectName("Question2Lable")
        self.gridLayout_12.addWidget(self.Question2Lable, 3, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(629, 269, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem1, 4, 1, 1, 1)
        self.previousPageBtn = QtWidgets.QPushButton(self.QuestionariesPage)
        self.previousPageBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.previousPageBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.previousPageBtn.setFont(font)
        self.previousPageBtn.setStyleSheet("/* Normal state styling */\n"
"QPushButton {\n"
"    color: white;\n"
"    background: #0C8C4C;\n"
"    border: 2px solid #eee;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"/* Hover state styling */\n"
"QPushButton:hover {\n"
"    background: #08A79D; /* Change the color for hover effect */\n"
"}\n"
"\n"
"/* Advanced styling */\n"
"QPushButton:pressed {\n"
"    background: #067267; /* Change the color for pressed effect */\n"
"    border: 2px solid #067267;\n"
"}\n"
"\n"
"/* Add any other advanced styling here */\n"
"\n"
"")
        self.previousPageBtn.setObjectName("previousPageBtn")
        self.gridLayout_12.addWidget(self.previousPageBtn, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.QuestionariesPage)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("padding:10px;\n"
"background:#F2F2F2;\n"
"border-radius:10px;\n"
"color:black;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_12.addWidget(self.label_5, 0, 0, 1, 2)
        self.frame_2 = QtWidgets.QFrame(self.QuestionariesPage)
        self.frame_2.setMinimumSize(QtCore.QSize(700, 0))
        self.frame_2.setStyleSheet("padding-left:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.QoneOpt1 = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QoneOpt1.setFont(font)
        self.QoneOpt1.setStyleSheet("QCheckBox {\n"
"    spacing: 5px; /* space between checkbox and text */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"    border: 2px solid #5A5A5A; /* border color */\n"
"    background-color: #FFFFFF; /* background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5A5A5A; /* background color when checked */\n"
"    border: 2px solid #5A5A5A; /* border color when checked */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #E0E0E0; /* background color when disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when disabled */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    background-color: #A0A0A0; /* background color when checked and disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when checked and disabled */\n"
"}\n"
"")
        self.QoneOpt1.setObjectName("QoneOpt1")
        self.verticalLayout_2.addWidget(self.QoneOpt1)
        self.QoneOpt2 = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QoneOpt2.setFont(font)
        self.QoneOpt2.setStyleSheet("QCheckBox {\n"
"    spacing: 5px; /* space between checkbox and text */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"    border: 2px solid #5A5A5A; /* border color */\n"
"    background-color: #FFFFFF; /* background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5A5A5A; /* background color when checked */\n"
"    border: 2px solid #5A5A5A; /* border color when checked */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #E0E0E0; /* background color when disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when disabled */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    background-color: #A0A0A0; /* background color when checked and disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when checked and disabled */\n"
"}\n"
"")
        self.QoneOpt2.setObjectName("QoneOpt2")
        self.verticalLayout_2.addWidget(self.QoneOpt2)
        self.QoneOpt3 = QtWidgets.QCheckBox(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QoneOpt3.setFont(font)
        self.QoneOpt3.setStyleSheet("QCheckBox {\n"
"    spacing: 5px; /* space between checkbox and text */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"    border: 2px solid #5A5A5A; /* border color */\n"
"    background-color: #FFFFFF; /* background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5A5A5A; /* background color when checked */\n"
"    border: 2px solid #5A5A5A; /* border color when checked */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #E0E0E0; /* background color when disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when disabled */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    background-color: #A0A0A0; /* background color when checked and disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when checked and disabled */\n"
"}\n"
"")
        self.QoneOpt3.setObjectName("QoneOpt3")
        self.verticalLayout_2.addWidget(self.QoneOpt3)
        self.gridLayout_12.addWidget(self.frame_2, 2, 0, 1, 1)
        self.frame_16 = QtWidgets.QFrame(self.QuestionariesPage)
        self.frame_16.setStyleSheet("padding-left:10px;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_16)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.QtwoOpt1 = QtWidgets.QCheckBox(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QtwoOpt1.setFont(font)
        self.QtwoOpt1.setStyleSheet("QCheckBox {\n"
"    spacing: 5px; /* space between checkbox and text */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"    border: 2px solid #5A5A5A; /* border color */\n"
"    background-color: #FFFFFF; /* background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5A5A5A; /* background color when checked */\n"
"    border: 2px solid #5A5A5A; /* border color when checked */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #E0E0E0; /* background color when disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when disabled */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    background-color: #A0A0A0; /* background color when checked and disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when checked and disabled */\n"
"}\n"
"")
        self.QtwoOpt1.setObjectName("QtwoOpt1")
        self.gridLayout_17.addWidget(self.QtwoOpt1, 0, 0, 1, 1)
        self.QtwoOpt2 = QtWidgets.QCheckBox(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QtwoOpt2.setFont(font)
        self.QtwoOpt2.setStyleSheet("QCheckBox {\n"
"    spacing: 5px; /* space between checkbox and text */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"    border: 2px solid #5A5A5A; /* border color */\n"
"    background-color: #FFFFFF; /* background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5A5A5A; /* background color when checked */\n"
"    border: 2px solid #5A5A5A; /* border color when checked */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #E0E0E0; /* background color when disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when disabled */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    background-color: #A0A0A0; /* background color when checked and disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when checked and disabled */\n"
"}\n"
"")
        self.QtwoOpt2.setObjectName("QtwoOpt2")
        self.gridLayout_17.addWidget(self.QtwoOpt2, 1, 0, 1, 1)
        self.QtwoOpt3 = QtWidgets.QCheckBox(self.frame_16)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.QtwoOpt3.setFont(font)
        self.QtwoOpt3.setStyleSheet("QCheckBox {\n"
"    spacing: 5px; /* space between checkbox and text */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 4px;\n"
"    border: 2px solid #5A5A5A; /* border color */\n"
"    background-color: #FFFFFF; /* background color */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5A5A5A; /* background color when checked */\n"
"    border: 2px solid #5A5A5A; /* border color when checked */\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #E0E0E0; /* background color when disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when disabled */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:disabled {\n"
"    background-color: #A0A0A0; /* background color when checked and disabled */\n"
"    border: 2px solid #A0A0A0; /* border color when checked and disabled */\n"
"}\n"
"")
        self.QtwoOpt3.setObjectName("QtwoOpt3")
        self.gridLayout_17.addWidget(self.QtwoOpt3, 2, 0, 1, 1)
        self.gridLayout_12.addWidget(self.frame_16, 4, 0, 1, 1)
        self.nextPageBtn = QtWidgets.QPushButton(self.QuestionariesPage)
        self.nextPageBtn.setMinimumSize(QtCore.QSize(200, 60))
        self.nextPageBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nextPageBtn.setFont(font)
        self.nextPageBtn.setStyleSheet("/* Normal state styling */\n"
"QPushButton {\n"
"    color: white;\n"
"    background: #0C8C4C;\n"
"    border: 2px solid #eee;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"/* Hover state styling */\n"
"QPushButton:hover {\n"
"    background: #08A79D; /* Change the color for hover effect */\n"
"}\n"
"\n"
"/* Advanced styling */\n"
"QPushButton:pressed {\n"
"    background: #067267; /* Change the color for pressed effect */\n"
"    border: 2px solid #067267;\n"
"}\n"
"\n"
"/* Add any other advanced styling here */\n"
"\n"
"")
        self.nextPageBtn.setObjectName("nextPageBtn")
        self.gridLayout_12.addWidget(self.nextPageBtn, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.stackedWidget.addWidget(self.QuestionariesPage)
        self.ResultsPage = QtWidgets.QWidget()
        self.ResultsPage.setObjectName("ResultsPage")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.ResultsPage)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.label_4 = QtWidgets.QLabel(self.ResultsPage)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("padding:10px;\n"
"background:#F2F2F2;\n"
"border-radius:10px;\n"
"color:black;")
        self.label_4.setObjectName("label_4")
        self.gridLayout_24.addWidget(self.label_4, 0, 0, 1, 1)
        self.scoreGainedLabel = QtWidgets.QLabel(self.ResultsPage)
        self.scoreGainedLabel.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.scoreGainedLabel.setFont(font)
        self.scoreGainedLabel.setStyleSheet("text-align:center;\n"
"color:black;")
        self.scoreGainedLabel.setObjectName("scoreGainedLabel")
        self.gridLayout_24.addWidget(self.scoreGainedLabel, 1, 0, 1, 1)
        self.frame_17 = QtWidgets.QFrame(self.ResultsPage)
        self.frame_17.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_17.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        self.frame_17.setFont(font)
        self.frame_17.setStyleSheet("color:white;")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.category1 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category1.sizePolicy().hasHeightForWidth())
        self.category1.setSizePolicy(sizePolicy)
        self.category1.setMinimumSize(QtCore.QSize(180, 60))
        self.category1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.category1.setStyleSheet(" color: white;\n"
"    background: #0C8C4C;\n"
"border-radius: 10px;\n"
"border:2px solid #eee;")
        self.category1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category1.setObjectName("category1")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.category1)
        self.gridLayout_15.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_15 = QtWidgets.QLabel(self.category1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border:none;")
        self.label_15.setObjectName("label_15")
        self.gridLayout_15.addWidget(self.label_15, 1, 0, 1, 1)
        self.category1Score = QtWidgets.QLabel(self.category1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category1Score.setFont(font)
        self.category1Score.setStyleSheet("border:none;")
        self.category1Score.setObjectName("category1Score")
        self.gridLayout_15.addWidget(self.category1Score, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_13.addWidget(self.category1, 0, 0, 1, 1)
        self.category4 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category4.sizePolicy().hasHeightForWidth())
        self.category4.setSizePolicy(sizePolicy)
        self.category4.setMinimumSize(QtCore.QSize(180, 60))
        self.category4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.category4.setStyleSheet(" color: white;\n"
"    background: #0C8C4C;\n"
"    border-radius: 10px;\n"
"border:2px solid #eee;")
        self.category4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category4.setObjectName("category4")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.category4)
        self.gridLayout_27.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.label_19 = QtWidgets.QLabel(self.category4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("border:none;")
        self.label_19.setObjectName("label_19")
        self.gridLayout_27.addWidget(self.label_19, 1, 0, 1, 1)
        self.category4Score = QtWidgets.QLabel(self.category4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category4Score.setFont(font)
        self.category4Score.setStyleSheet("border:none;")
        self.category4Score.setObjectName("category4Score")
        self.gridLayout_27.addWidget(self.category4Score, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_13.addWidget(self.category4, 0, 1, 1, 1)
        self.category2 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category2.sizePolicy().hasHeightForWidth())
        self.category2.setSizePolicy(sizePolicy)
        self.category2.setMinimumSize(QtCore.QSize(180, 60))
        self.category2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.category2.setStyleSheet(" color: white;\n"
"    background: #0C8C4C;\n"
"    border-radius: 10px;\n"
"border:2px solid #eee;")
        self.category2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category2.setObjectName("category2")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.category2)
        self.gridLayout_22.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.category2Label = QtWidgets.QLabel(self.category2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.category2Label.setFont(font)
        self.category2Label.setStyleSheet("border:none;")
        self.category2Label.setObjectName("category2Label")
        self.gridLayout_22.addWidget(self.category2Label, 1, 0, 1, 1)
        self.category2Score = QtWidgets.QLabel(self.category2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category2Score.setFont(font)
        self.category2Score.setStyleSheet("border:none;")
        self.category2Score.setObjectName("category2Score")
        self.gridLayout_22.addWidget(self.category2Score, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_13.addWidget(self.category2, 1, 0, 1, 1)
        self.category5 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category5.sizePolicy().hasHeightForWidth())
        self.category5.setSizePolicy(sizePolicy)
        self.category5.setMinimumSize(QtCore.QSize(180, 60))
        self.category5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.category5.setStyleSheet(" color: white;\n"
"    background: #0C8C4C;\n"
"    border-radius: 10px;\n"
"border:2px solid #eee;")
        self.category5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category5.setObjectName("category5")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.category5)
        self.gridLayout_28.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.label_21 = QtWidgets.QLabel(self.category5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("border:none;")
        self.label_21.setObjectName("label_21")
        self.gridLayout_28.addWidget(self.label_21, 1, 0, 1, 1)
        self.category5Score = QtWidgets.QLabel(self.category5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category5Score.setFont(font)
        self.category5Score.setStyleSheet("border:none;")
        self.category5Score.setObjectName("category5Score")
        self.gridLayout_28.addWidget(self.category5Score, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_13.addWidget(self.category5, 1, 1, 1, 1)
        self.category3 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category3.sizePolicy().hasHeightForWidth())
        self.category3.setSizePolicy(sizePolicy)
        self.category3.setMinimumSize(QtCore.QSize(180, 60))
        self.category3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.category3.setStyleSheet(" color: white;\n"
"    background: #0C8C4C;\n"
"    border-radius: 10px;\n"
"border:2px solid #eee;")
        self.category3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category3.setObjectName("category3")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.category3)
        self.gridLayout_23.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_18 = QtWidgets.QLabel(self.category3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border:none;")
        self.label_18.setObjectName("label_18")
        self.gridLayout_23.addWidget(self.label_18, 1, 0, 1, 1)
        self.category3Score = QtWidgets.QLabel(self.category3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category3Score.setFont(font)
        self.category3Score.setStyleSheet("border:none;")
        self.category3Score.setObjectName("category3Score")
        self.gridLayout_23.addWidget(self.category3Score, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_13.addWidget(self.category3, 2, 0, 1, 1)
        self.category6 = QtWidgets.QFrame(self.frame_17)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.category6.sizePolicy().hasHeightForWidth())
        self.category6.setSizePolicy(sizePolicy)
        self.category6.setMinimumSize(QtCore.QSize(180, 60))
        self.category6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.category6.setStyleSheet(" color: white;\n"
"    background: #0C8C4C;\n"
"    border-radius: 10px;\n"
"border:2px solid #eee;")
        self.category6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.category6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.category6.setObjectName("category6")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.category6)
        self.gridLayout_29.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_27 = QtWidgets.QLabel(self.category6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("border:none;")
        self.label_27.setObjectName("label_27")
        self.gridLayout_29.addWidget(self.label_27, 1, 0, 1, 1)
        self.category6Score = QtWidgets.QLabel(self.category6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.category6Score.setFont(font)
        self.category6Score.setStyleSheet("border:none;")
        self.category6Score.setObjectName("category6Score")
        self.gridLayout_29.addWidget(self.category6Score, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_13.addWidget(self.category6, 2, 1, 1, 1)
        self.gridLayout_24.addWidget(self.frame_17, 2, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.ResultsPage)
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("text-align:center;\n"
"color:black;")
        self.label_23.setObjectName("label_23")
        self.gridLayout_24.addWidget(self.label_23, 3, 0, 1, 1)
        self.frame_67 = QtWidgets.QFrame(self.ResultsPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy)
        self.frame_67.setStyleSheet("padding:10px;\n"
"background:#f5f5f5;\n"
"border-radius:15px;")
        self.frame_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_67.setObjectName("frame_67")
        self.label_43 = QtWidgets.QLabel(self.frame_67)
        self.label_43.setGeometry(QtCore.QRect(866, 177, 28, 39))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color:#48ACAC;\n"
"image: url(:/Icons/Icons/icons8-scroll-down-50.png);")
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_67)
        self.label_44.setGeometry(QtCore.QRect(866, 43, 28, 39))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color:#48ACAC;\n"
"image: url(:/Icons/Icons/icons8-scroll-up-50.png);")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.label_22 = QtWidgets.QLabel(self.frame_67)
        self.label_22.setGeometry(QtCore.QRect(21, 21, 838, 15))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: #48ACAC;")
        self.label_22.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_22.setObjectName("label_22")
        self.textEdit = QtWidgets.QTextEdit(self.frame_67)
        self.textEdit.setGeometry(QtCore.QRect(21, 43, 838, 331))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_24.addWidget(self.frame_67, 4, 0, 1, 1)
        self.stackedWidget.addWidget(self.ResultsPage)
        self.SettingsPage = QtWidgets.QWidget()
        self.SettingsPage.setObjectName("SettingsPage")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.SettingsPage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_14 = QtWidgets.QFrame(self.SettingsPage)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_6.addWidget(self.frame_14, 1, 0, 1, 3)
        self.frame_13 = QtWidgets.QFrame(self.SettingsPage)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_17 = QtWidgets.QLabel(self.frame_13)
        self.label_17.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("text-align:center;\n"
"color:black;")
        self.label_17.setObjectName("label_17")
        self.gridLayout_16.addWidget(self.label_17, 0, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_13)
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("text-align:center;\n"
"color:black;")
        self.label_24.setObjectName("label_24")
        self.gridLayout_16.addWidget(self.label_24, 2, 0, 1, 1)
        self.excelFileInput = QtWidgets.QLineEdit(self.frame_13)
        self.excelFileInput.setMinimumSize(QtCore.QSize(400, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.excelFileInput.setFont(font)
        self.excelFileInput.setStyleSheet("padding:10px;\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.excelFileInput.setObjectName("excelFileInput")
        self.gridLayout_16.addWidget(self.excelFileInput, 1, 0, 1, 1)
        self.nextPageBtn_3 = QtWidgets.QPushButton(self.frame_13)
        self.nextPageBtn_3.setMinimumSize(QtCore.QSize(200, 60))
        self.nextPageBtn_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nextPageBtn_3.setFont(font)
        self.nextPageBtn_3.setStyleSheet("/* Normal state styling */\n"
"QPushButton {\n"
"    color: white;\n"
"    background: #0C8C4C;\n"
"    border: 2px solid #eee;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"/* Hover state styling */\n"
"QPushButton:hover {\n"
"    background: #08A79D; /* Change the color for hover effect */\n"
"}\n"
"\n"
"/* Advanced styling */\n"
"QPushButton:pressed {\n"
"    background: #067267; /* Change the color for pressed effect */\n"
"    border: 2px solid #067267;\n"
"}\n"
"\n"
"/* Add any other advanced styling here */\n"
"\n"
"")
        self.nextPageBtn_3.setObjectName("nextPageBtn_3")
        self.gridLayout_16.addWidget(self.nextPageBtn_3, 4, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame_13)
        self.dateEdit.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("padding:10px;\n"
"border-radius:10px;\n"
"border:2px solid black;")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_16.addWidget(self.dateEdit, 4, 0, 1, 1)
        self.changeFileBtn = QtWidgets.QPushButton(self.frame_13)
        self.changeFileBtn.setMinimumSize(QtCore.QSize(200, 60))
        self.changeFileBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.changeFileBtn.setFont(font)
        self.changeFileBtn.setStyleSheet("/* Normal state styling */\n"
"QPushButton {\n"
"    color: white;\n"
"    background: #0C8C4C;\n"
"    border: 2px solid #eee;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"/* Hover state styling */\n"
"QPushButton:hover {\n"
"    background: #08A79D; /* Change the color for hover effect */\n"
"}\n"
"\n"
"/* Advanced styling */\n"
"QPushButton:pressed {\n"
"    background: #067267; /* Change the color for pressed effect */\n"
"    border: 2px solid #067267;\n"
"}\n"
"\n"
"/* Add any other advanced styling here */\n"
"\n"
"")
        self.changeFileBtn.setObjectName("changeFileBtn")
        self.gridLayout_16.addWidget(self.changeFileBtn, 1, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_13, 2, 0, 2, 3)
        self.label_8 = QtWidgets.QLabel(self.SettingsPage)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("padding:10px;\n"
"background:#F2F2F2;\n"
"border-radius:10px;\n"
"color:black;")
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.SettingsPage)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.saveResultsBtn = QtWidgets.QPushButton(self.frame_6)
        self.saveResultsBtn.setMinimumSize(QtCore.QSize(200, 60))
        self.saveResultsBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.saveResultsBtn.setFont(font)
        self.saveResultsBtn.setStyleSheet("/* Normal state styling */\n"
"QPushButton {\n"
"    color: white;\n"
"    background: #0C8C4C;\n"
"    border: 2px solid #eee;\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"/* Hover state styling */\n"
"QPushButton:hover {\n"
"    background: #08A79D; /* Change the color for hover effect */\n"
"}\n"
"\n"
"/* Advanced styling */\n"
"QPushButton:pressed {\n"
"    background: #067267; /* Change the color for pressed effect */\n"
"    border: 2px solid #067267;\n"
"}\n"
"\n"
"/* Add any other advanced styling here */\n"
"\n"
"")
        self.saveResultsBtn.setObjectName("saveResultsBtn")
        self.gridLayout_5.addWidget(self.saveResultsBtn, 0, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame_6)
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("text-align:center;\n"
"color:black;")
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 580, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame_6, 4, 0, 1, 3)
        self.stackedWidget.addWidget(self.SettingsPage)
        self.managePaymentsPage = QtWidgets.QWidget()
        self.managePaymentsPage.setObjectName("managePaymentsPage")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.managePaymentsPage)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.stackedWidget.addWidget(self.managePaymentsPage)
        self.userProfile = QtWidgets.QWidget()
        self.userProfile.setObjectName("userProfile")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.userProfile)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.stackedWidget.addWidget(self.userProfile)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Threat \n"
"Interlligence"))
        self.dashboardBtn.setText(_translate("MainWindow", " Dashboard   "))
        self.QuestionaryPageBtn.setText(_translate("MainWindow", " Questionaries  "))
        self.ResultsPageBtn.setText(_translate("MainWindow", " Results         "))
        self.SettingsPageBtn.setText(_translate("MainWindow", " Settings       "))
        self.PieGraphLabel.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "Dashboard"))
        self.totalScoreLable.setText(_translate("MainWindow", "100"))
        self.label_9.setText(_translate("MainWindow", "Total Questions"))
        self.lineGraphLabel.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.category1Graph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.category3Graph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.category6Graph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.category4Graph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.category5Graph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.category2Graph.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.QuestionOneLabel.setText(_translate("MainWindow", "Question No 1: How often does your organization update its privacy policy?"))
        self.Question2Lable.setText(_translate("MainWindow", "Question No 2: How often does your organization update its privacy policy?"))
        self.previousPageBtn.setText(_translate("MainWindow", "Previous Page"))
        self.label_5.setText(_translate("MainWindow", "Questionaries"))
        self.QoneOpt1.setText(_translate("MainWindow", "QoneOpt1"))
        self.QoneOpt2.setText(_translate("MainWindow", "CheckBox"))
        self.QoneOpt3.setText(_translate("MainWindow", "CheckBox"))
        self.QtwoOpt1.setText(_translate("MainWindow", "CheckBox"))
        self.QtwoOpt2.setText(_translate("MainWindow", "CheckBox"))
        self.QtwoOpt3.setText(_translate("MainWindow", "CheckBox"))
        self.nextPageBtn.setText(_translate("MainWindow", "Next Page"))
        self.label_4.setText(_translate("MainWindow", "Results"))
        self.scoreGainedLabel.setText(_translate("MainWindow", "   Score Gained:  67"))
        self.label_15.setText(_translate("MainWindow", "Understanding and Implemention"))
        self.category1Score.setText(_translate("MainWindow", "10"))
        self.label_19.setText(_translate("MainWindow", "Documentation and Policy Management:"))
        self.category4Score.setText(_translate("MainWindow", "7"))
        self.category2Label.setText(_translate("MainWindow", "Information Security Management:"))
        self.category2Score.setText(_translate("MainWindow", "8"))
        self.label_21.setText(_translate("MainWindow", "Technical and Organizational Measures:"))
        self.category5Score.setText(_translate("MainWindow", "4"))
        self.label_18.setText(_translate("MainWindow", "Training and Awareness:"))
        self.category3Score.setText(_translate("MainWindow", "7"))
        self.label_27.setText(_translate("MainWindow", "Compliance and Audit:"))
        self.category6Score.setText(_translate("MainWindow", "2"))
        self.label_23.setText(_translate("MainWindow", "   Recommendations:"))
        self.label_22.setText(_translate("MainWindow", "Calculated in last 7 days"))
        self.label_17.setText(_translate("MainWindow", "Excel File Address:"))
        self.label_24.setText(_translate("MainWindow", "Recommendation Date:"))
        self.nextPageBtn_3.setText(_translate("MainWindow", "Change Date"))
        self.changeFileBtn.setText(_translate("MainWindow", "Change File"))
        self.label_8.setText(_translate("MainWindow", "Settings"))
        self.saveResultsBtn.setText(_translate("MainWindow", "Save Results"))
        self.label_20.setText(_translate("MainWindow", "   Save Results as PDF: "))
import resource_rc
