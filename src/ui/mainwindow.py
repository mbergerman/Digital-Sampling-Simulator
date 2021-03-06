# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Python_Projects\Digital-Sampling-Simulator\designer\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1290, 707)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        MainWindow.setFont(font)
        icon = QtGui.QIcon.fromTheme("Icon")
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(10, 10, 1270, 681))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setLineWidth(4)
        self.mainFrame.setObjectName("mainFrame")
        self.groupBox_2 = QtWidgets.QGroupBox(self.mainFrame)
        self.groupBox_2.setGeometry(QtCore.QRect(640, 20, 601, 381))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(90, 210, 31, 31))
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(90, 170, 41, 31))
        self.label_13.setObjectName("label_13")
        self.sampling_dc_input = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.sampling_dc_input.setGeometry(QtCore.QRect(150, 210, 211, 31))
        self.sampling_dc_input.setDecimals(3)
        self.sampling_dc_input.setMaximum(100.0)
        self.sampling_dc_input.setObjectName("sampling_dc_input")
        self.sampling_period_input = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.sampling_period_input.setGeometry(QtCore.QRect(150, 170, 211, 31))
        self.sampling_period_input.setDecimals(3)
        self.sampling_period_input.setMaximum(99999999.99)
        self.sampling_period_input.setObjectName("sampling_period_input")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(370, 210, 31, 31))
        self.label_15.setObjectName("label_15")
        self.update_sampling = QtWidgets.QPushButton(self.groupBox_2)
        self.update_sampling.setGeometry(QtCore.QRect(400, 320, 191, 51))
        self.update_sampling.setObjectName("update_sampling")
        self.sampling_period_multiplier = QtWidgets.QComboBox(self.groupBox_2)
        self.sampling_period_multiplier.setGeometry(QtCore.QRect(370, 170, 81, 31))
        self.sampling_period_multiplier.setObjectName("sampling_period_multiplier")
        self.sampling_period_multiplier.addItem("")
        self.sampling_period_multiplier.addItem("")
        self.sampling_period_multiplier.addItem("")
        self.groupBox_3 = QtWidgets.QGroupBox(self.mainFrame)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 601, 381))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.update_input = QtWidgets.QPushButton(self.groupBox_3)
        self.update_input.setGeometry(QtCore.QRect(390, 320, 191, 51))
        self.update_input.setObjectName("update_input")
        self.input_tabs = QtWidgets.QTabWidget(self.groupBox_3)
        self.input_tabs.setGeometry(QtCore.QRect(10, 30, 581, 281))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_tabs.setFont(font)
        self.input_tabs.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_tabs.setObjectName("input_tabs")
        self.sine_tab = QtWidgets.QWidget()
        self.sine_tab.setObjectName("sine_tab")
        self.sine_vp_multiplier = QtWidgets.QComboBox(self.sine_tab)
        self.sine_vp_multiplier.setGeometry(QtCore.QRect(370, 110, 71, 31))
        self.sine_vp_multiplier.setObjectName("sine_vp_multiplier")
        self.sine_vp_multiplier.addItem("")
        self.sine_vp_multiplier.addItem("")
        self.sine_f_multiplier = QtWidgets.QComboBox(self.sine_tab)
        self.sine_f_multiplier.setGeometry(QtCore.QRect(370, 150, 71, 31))
        self.sine_f_multiplier.setObjectName("sine_f_multiplier")
        self.sine_f_multiplier.addItem("")
        self.sine_f_multiplier.addItem("")
        self.sine_f_multiplier.addItem("")
        self.sine_phase_input = QtWidgets.QDoubleSpinBox(self.sine_tab)
        self.sine_phase_input.setGeometry(QtCore.QRect(150, 190, 211, 31))
        self.sine_phase_input.setDecimals(3)
        self.sine_phase_input.setMinimum(-360.0)
        self.sine_phase_input.setMaximum(360.0)
        self.sine_phase_input.setObjectName("sine_phase_input")
        self.sine_vp_input = QtWidgets.QDoubleSpinBox(self.sine_tab)
        self.sine_vp_input.setGeometry(QtCore.QRect(150, 110, 211, 31))
        self.sine_vp_input.setDecimals(3)
        self.sine_vp_input.setObjectName("sine_vp_input")
        self.label = QtWidgets.QLabel(self.sine_tab)
        self.label.setGeometry(QtCore.QRect(90, 110, 41, 31))
        self.label.setObjectName("label")
        self.sine_phase_mod = QtWidgets.QComboBox(self.sine_tab)
        self.sine_phase_mod.setGeometry(QtCore.QRect(370, 190, 71, 31))
        self.sine_phase_mod.setObjectName("sine_phase_mod")
        self.sine_phase_mod.addItem("")
        self.sine_phase_mod.addItem("")
        self.label_4 = QtWidgets.QLabel(self.sine_tab)
        self.label_4.setGeometry(QtCore.QRect(90, 190, 31, 31))
        self.label_4.setObjectName("label_4")
        self.sine_f_input = QtWidgets.QDoubleSpinBox(self.sine_tab)
        self.sine_f_input.setGeometry(QtCore.QRect(150, 150, 211, 31))
        self.sine_f_input.setDecimals(3)
        self.sine_f_input.setMaximum(9999999.99)
        self.sine_f_input.setObjectName("sine_f_input")
        self.label_3 = QtWidgets.QLabel(self.sine_tab)
        self.label_3.setGeometry(QtCore.QRect(90, 150, 31, 31))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.sine_tab)
        self.label_5.setGeometry(QtCore.QRect(120, 30, 291, 51))
        self.label_5.setObjectName("label_5")
        self.input_tabs.addTab(self.sine_tab, "")
        self.u_sine_tab = QtWidgets.QWidget()
        self.u_sine_tab.setObjectName("u_sine_tab")
        self.u_sine_f_multiplier = QtWidgets.QComboBox(self.u_sine_tab)
        self.u_sine_f_multiplier.setGeometry(QtCore.QRect(370, 150, 71, 31))
        self.u_sine_f_multiplier.setObjectName("u_sine_f_multiplier")
        self.u_sine_f_multiplier.addItem("")
        self.u_sine_f_multiplier.addItem("")
        self.u_sine_f_multiplier.addItem("")
        self.u_sine_phase_input = QtWidgets.QDoubleSpinBox(self.u_sine_tab)
        self.u_sine_phase_input.setGeometry(QtCore.QRect(150, 190, 211, 31))
        self.u_sine_phase_input.setDecimals(3)
        self.u_sine_phase_input.setMinimum(-360.0)
        self.u_sine_phase_input.setMaximum(360.0)
        self.u_sine_phase_input.setProperty("value", 0.0)
        self.u_sine_phase_input.setObjectName("u_sine_phase_input")
        self.u_sine_vp_multiplier = QtWidgets.QComboBox(self.u_sine_tab)
        self.u_sine_vp_multiplier.setGeometry(QtCore.QRect(370, 110, 71, 31))
        self.u_sine_vp_multiplier.setObjectName("u_sine_vp_multiplier")
        self.u_sine_vp_multiplier.addItem("")
        self.u_sine_vp_multiplier.addItem("")
        self.u_sine_vp_input = QtWidgets.QDoubleSpinBox(self.u_sine_tab)
        self.u_sine_vp_input.setGeometry(QtCore.QRect(150, 110, 211, 31))
        self.u_sine_vp_input.setDecimals(3)
        self.u_sine_vp_input.setObjectName("u_sine_vp_input")
        self.label_6 = QtWidgets.QLabel(self.u_sine_tab)
        self.label_6.setGeometry(QtCore.QRect(90, 110, 41, 31))
        self.label_6.setObjectName("label_6")
        self.u_sine_phase_mod = QtWidgets.QComboBox(self.u_sine_tab)
        self.u_sine_phase_mod.setGeometry(QtCore.QRect(370, 190, 71, 31))
        self.u_sine_phase_mod.setObjectName("u_sine_phase_mod")
        self.u_sine_phase_mod.addItem("")
        self.u_sine_phase_mod.addItem("")
        self.label_7 = QtWidgets.QLabel(self.u_sine_tab)
        self.label_7.setGeometry(QtCore.QRect(90, 190, 31, 31))
        self.label_7.setObjectName("label_7")
        self.u_sine_f_input = QtWidgets.QDoubleSpinBox(self.u_sine_tab)
        self.u_sine_f_input.setGeometry(QtCore.QRect(150, 150, 211, 31))
        self.u_sine_f_input.setDecimals(3)
        self.u_sine_f_input.setMaximum(9999999.99)
        self.u_sine_f_input.setObjectName("u_sine_f_input")
        self.label_8 = QtWidgets.QLabel(self.u_sine_tab)
        self.label_8.setGeometry(QtCore.QRect(50, 30, 461, 51))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.u_sine_tab)
        self.label_9.setGeometry(QtCore.QRect(90, 150, 31, 31))
        self.label_9.setObjectName("label_9")
        self.input_tabs.addTab(self.u_sine_tab, "")
        self.am_tab = QtWidgets.QWidget()
        self.am_tab.setObjectName("am_tab")
        self.label_24 = QtWidgets.QLabel(self.am_tab)
        self.label_24.setGeometry(QtCore.QRect(90, 90, 41, 31))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.am_tab)
        self.label_25.setGeometry(QtCore.QRect(90, 170, 31, 31))
        self.label_25.setObjectName("label_25")
        self.am_vp_input = QtWidgets.QDoubleSpinBox(self.am_tab)
        self.am_vp_input.setGeometry(QtCore.QRect(150, 90, 211, 31))
        self.am_vp_input.setDecimals(3)
        self.am_vp_input.setObjectName("am_vp_input")
        self.am_vp_multiplier = QtWidgets.QComboBox(self.am_tab)
        self.am_vp_multiplier.setGeometry(QtCore.QRect(370, 90, 71, 31))
        self.am_vp_multiplier.setObjectName("am_vp_multiplier")
        self.am_vp_multiplier.addItem("")
        self.am_vp_multiplier.addItem("")
        self.am_fm_input = QtWidgets.QDoubleSpinBox(self.am_tab)
        self.am_fm_input.setGeometry(QtCore.QRect(150, 170, 211, 31))
        self.am_fm_input.setDecimals(3)
        self.am_fm_input.setMaximum(9999999.99)
        self.am_fm_input.setObjectName("am_fm_input")
        self.label_26 = QtWidgets.QLabel(self.am_tab)
        self.label_26.setGeometry(QtCore.QRect(40, 30, 501, 51))
        self.label_26.setObjectName("label_26")
        self.am_fc_input = QtWidgets.QDoubleSpinBox(self.am_tab)
        self.am_fc_input.setGeometry(QtCore.QRect(150, 130, 211, 31))
        self.am_fc_input.setDecimals(3)
        self.am_fc_input.setMaximum(9999999.99)
        self.am_fc_input.setObjectName("am_fc_input")
        self.am_fc_multiplier = QtWidgets.QComboBox(self.am_tab)
        self.am_fc_multiplier.setGeometry(QtCore.QRect(370, 130, 71, 31))
        self.am_fc_multiplier.setObjectName("am_fc_multiplier")
        self.am_fc_multiplier.addItem("")
        self.am_fc_multiplier.addItem("")
        self.am_fc_multiplier.addItem("")
        self.label_27 = QtWidgets.QLabel(self.am_tab)
        self.label_27.setGeometry(QtCore.QRect(90, 130, 31, 31))
        self.label_27.setObjectName("label_27")
        self.am_m_input = QtWidgets.QDoubleSpinBox(self.am_tab)
        self.am_m_input.setGeometry(QtCore.QRect(150, 210, 211, 31))
        self.am_m_input.setDecimals(2)
        self.am_m_input.setMaximum(1.0)
        self.am_m_input.setSingleStep(0.01)
        self.am_m_input.setObjectName("am_m_input")
        self.label_28 = QtWidgets.QLabel(self.am_tab)
        self.label_28.setGeometry(QtCore.QRect(90, 210, 31, 31))
        self.label_28.setObjectName("label_28")
        self.am_fm_multiplier = QtWidgets.QComboBox(self.am_tab)
        self.am_fm_multiplier.setGeometry(QtCore.QRect(370, 170, 71, 31))
        self.am_fm_multiplier.setObjectName("am_fm_multiplier")
        self.am_fm_multiplier.addItem("")
        self.am_fm_multiplier.addItem("")
        self.am_fm_multiplier.addItem("")
        self.input_tabs.addTab(self.am_tab, "")
        self.groupBox_4 = QtWidgets.QGroupBox(self.mainFrame)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 410, 1221, 251))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.plot_xinB = QtWidgets.QPushButton(self.groupBox_4)
        self.plot_xinB.setGeometry(QtCore.QRect(20, 80, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plot_xinB.setFont(font)
        self.plot_xinB.setObjectName("plot_xinB")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox.setGeometry(QtCore.QRect(150, 60, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.toggle_antialias = QtWidgets.QCheckBox(self.groupBox)
        self.toggle_antialias.setGeometry(QtCore.QRect(50, 40, 16, 21))
        self.toggle_antialias.setText("")
        self.toggle_antialias.setObjectName("toggle_antialias")
        self.plot_aaout = QtWidgets.QPushButton(self.groupBox_4)
        self.plot_aaout.setGeometry(QtCore.QRect(280, 80, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_aaout.setFont(font)
        self.plot_aaout.setObjectName("plot_aaout")
        self.plot_akout = QtWidgets.QPushButton(self.groupBox_4)
        self.plot_akout.setGeometry(QtCore.QRect(820, 80, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_akout.setFont(font)
        self.plot_akout.setObjectName("plot_akout")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(690, 60, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.toggle_analogkey = QtWidgets.QCheckBox(self.groupBox_5)
        self.toggle_analogkey.setGeometry(QtCore.QRect(50, 40, 16, 21))
        self.toggle_analogkey.setText("")
        self.toggle_analogkey.setObjectName("toggle_analogkey")
        self.plot_shout = QtWidgets.QPushButton(self.groupBox_4)
        self.plot_shout.setGeometry(QtCore.QRect(550, 80, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plot_shout.setFont(font)
        self.plot_shout.setObjectName("plot_shout")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setGeometry(QtCore.QRect(420, 60, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.toggle_SH = QtWidgets.QCheckBox(self.groupBox_6)
        self.toggle_SH.setGeometry(QtCore.QRect(50, 40, 16, 21))
        self.toggle_SH.setText("")
        self.toggle_SH.setObjectName("toggle_SH")
        self.plot_xoutB = QtWidgets.QPushButton(self.groupBox_4)
        self.plot_xoutB.setGeometry(QtCore.QRect(1110, 80, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plot_xoutB.setFont(font)
        self.plot_xoutB.setObjectName("plot_xoutB")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setGeometry(QtCore.QRect(950, 60, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.toggle_recovery = QtWidgets.QCheckBox(self.groupBox_7)
        self.toggle_recovery.setGeometry(QtCore.QRect(50, 40, 16, 21))
        self.toggle_recovery.setText("")
        self.toggle_recovery.setObjectName("toggle_recovery")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(110, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(260, 100, 21, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(400, 100, 21, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_4)
        self.label_20.setGeometry(QtCore.QRect(800, 100, 21, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_4)
        self.label_21.setGeometry(QtCore.QRect(670, 100, 21, 16))
        self.label_21.setObjectName("label_21")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(1070, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_22 = QtWidgets.QLabel(self.groupBox_4)
        self.label_22.setGeometry(QtCore.QRect(530, 100, 21, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(930, 100, 21, 16))
        self.label_23.setObjectName("label_23")
        self.run_sim = QtWidgets.QPushButton(self.groupBox_4)
        self.run_sim.setGeometry(QtCore.QRect(1000, 170, 191, 51))
        self.run_sim.setObjectName("run_sim")
        self.spectrum_check = QtWidgets.QCheckBox(self.groupBox_4)
        self.spectrum_check.setGeometry(QtCore.QRect(30, 180, 181, 31))
        self.spectrum_check.setObjectName("spectrum_check")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.input_tabs.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Sampling Simulator"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Sampling Control Signal"))
        self.label_14.setText(_translate("MainWindow", "DC"))
        self.label_13.setText(_translate("MainWindow", "fs"))
        self.label_15.setText(_translate("MainWindow", "%"))
        self.update_sampling.setText(_translate("MainWindow", "Update Sampling"))
        self.sampling_period_multiplier.setItemText(0, _translate("MainWindow", "mHz"))
        self.sampling_period_multiplier.setItemText(1, _translate("MainWindow", "Hz"))
        self.sampling_period_multiplier.setItemText(2, _translate("MainWindow", "kHz"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Input Signal"))
        self.update_input.setText(_translate("MainWindow", "Update Xin(t)"))
        self.sine_vp_multiplier.setItemText(0, _translate("MainWindow", "mV"))
        self.sine_vp_multiplier.setItemText(1, _translate("MainWindow", "V"))
        self.sine_f_multiplier.setItemText(0, _translate("MainWindow", "mHz"))
        self.sine_f_multiplier.setItemText(1, _translate("MainWindow", "Hz"))
        self.sine_f_multiplier.setItemText(2, _translate("MainWindow", "kHz"))
        self.label.setText(_translate("MainWindow", "Vp"))
        self.sine_phase_mod.setItemText(0, _translate("MainWindow", "??"))
        self.sine_phase_mod.setItemText(1, _translate("MainWindow", "rad"))
        self.label_4.setText(_translate("MainWindow", "??"))
        self.label_3.setText(_translate("MainWindow", "f"))
        self.label_5.setText(_translate("MainWindow", "Xin(t) = Vp * cos( 2?? * f * t + ?? )"))
        self.input_tabs.setTabText(self.input_tabs.indexOf(self.sine_tab), _translate("MainWindow", "Sine"))
        self.u_sine_f_multiplier.setItemText(0, _translate("MainWindow", "mHz"))
        self.u_sine_f_multiplier.setItemText(1, _translate("MainWindow", "Hz"))
        self.u_sine_f_multiplier.setItemText(2, _translate("MainWindow", "kHz"))
        self.u_sine_vp_multiplier.setItemText(0, _translate("MainWindow", "mV"))
        self.u_sine_vp_multiplier.setItemText(1, _translate("MainWindow", "V"))
        self.label_6.setText(_translate("MainWindow", "Vp"))
        self.u_sine_phase_mod.setItemText(0, _translate("MainWindow", "??"))
        self.u_sine_phase_mod.setItemText(1, _translate("MainWindow", "rad"))
        self.label_7.setText(_translate("MainWindow", "??"))
        self.label_8.setText(_translate("MainWindow", "Xin(t) = Vp * sin( 2?? * (f / 5) * t + ?? ),   [0, 15/(2*f)]"))
        self.label_9.setText(_translate("MainWindow", "f"))
        self.input_tabs.setTabText(self.input_tabs.indexOf(self.u_sine_tab), _translate("MainWindow", "3/2 Sine"))
        self.label_24.setText(_translate("MainWindow", "Vp"))
        self.label_25.setText(_translate("MainWindow", "fm"))
        self.am_vp_multiplier.setItemText(0, _translate("MainWindow", "mV"))
        self.am_vp_multiplier.setItemText(1, _translate("MainWindow", "V"))
        self.label_26.setText(_translate("MainWindow", "Xin(t) = Vp * cos(2?? * fc * t) * [1 + m * cos(2?? * fm * t)]"))
        self.am_fc_multiplier.setItemText(0, _translate("MainWindow", "mHz"))
        self.am_fc_multiplier.setItemText(1, _translate("MainWindow", "Hz"))
        self.am_fc_multiplier.setItemText(2, _translate("MainWindow", "kHz"))
        self.label_27.setText(_translate("MainWindow", "fc"))
        self.label_28.setText(_translate("MainWindow", "m"))
        self.am_fm_multiplier.setItemText(0, _translate("MainWindow", "mHz"))
        self.am_fm_multiplier.setItemText(1, _translate("MainWindow", "Hz"))
        self.am_fm_multiplier.setItemText(2, _translate("MainWindow", "kHz"))
        self.input_tabs.setTabText(self.input_tabs.indexOf(self.am_tab), _translate("MainWindow", "AM"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Sampling Simulator - Graphical Output"))
        self.plot_xinB.setText(_translate("MainWindow", "Xin(t)"))
        self.groupBox.setTitle(_translate("MainWindow", "Anti-Alias"))
        self.plot_aaout.setText(_translate("MainWindow", "AA output"))
        self.plot_akout.setText(_translate("MainWindow", "AK output"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Analog Key"))
        self.plot_shout.setText(_translate("MainWindow", "SH output"))
        self.groupBox_6.setTitle(_translate("MainWindow", "SH"))
        self.plot_xoutB.setText(_translate("MainWindow", "Xout(t)"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Recovery"))
        self.label_16.setText(_translate("MainWindow", "???"))
        self.label_18.setText(_translate("MainWindow", "???"))
        self.label_19.setText(_translate("MainWindow", "???"))
        self.label_20.setText(_translate("MainWindow", "???"))
        self.label_21.setText(_translate("MainWindow", "???"))
        self.label_17.setText(_translate("MainWindow", "???"))
        self.label_22.setText(_translate("MainWindow", "???"))
        self.label_23.setText(_translate("MainWindow", "???"))
        self.run_sim.setText(_translate("MainWindow", "Run Simulation"))
        self.spectrum_check.setText(_translate("MainWindow", "Plot Spectrum"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
