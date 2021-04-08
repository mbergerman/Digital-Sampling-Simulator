from src.ui.mainwindow import *
import numpy as np
from numpy import linspace
import sys
import os
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QApplication, QWidget, QPushButton, QAction, QLineEdit, \
    QMessageBox, QRadioButton, QInputDialog

from src.sampling_data import *
from src.backend import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Init
        self.setFixedSize(1290, 700)
        self.input_tabs.setCurrentIndex(0)
        self.plot_aa = False
        self.plot_Xin = True
        self.plot_Xout = True
        self.plot_sh = False
        self.plot_ak = False
        self.sampling_data = sampling_data()
        self.type = self.input_tabs.currentWidget().objectName()
        self.xin = []
        self.xout = []
        self.xaa = []
        self.xsh = []
        self.xak = []
        self.N = 50000  # cantidad de muestras
        self.t = []
        self.fd = 0
        self.t_steady = []
        self.x_steady = []

        # BOTONES
        self.update_input.clicked.connect(self.update_xin)
        self.update_sampling.clicked.connect(self.update_sample)
        self.run_sim.clicked.connect(self.run_simulation)
        self.plot_xinB.clicked.connect(self.plot_xin)
        self.plot_xoutB.clicked.connect(self.plot_xout)
        self.plot_aaout.clicked.connect(self.plot_AAout)
        self.plot_shout.clicked.connect(self.plot_SHout)
        self.plot_akout.clicked.connect(self.plot_AKout)

    def update_xin(self):
        self.type = str(self.input_tabs.currentWidget().objectName())

        if self.type == "sine_tab":
            # Vp
            k = 1
            if str(self.sine_vp_multiplier.currentText()) == "mV":
                k = 1e-3
            self.sampling_data.Vp = k * self.sine_vp_input.value()
            # f
            c = 1
            if str(self.sine_f_multiplier.currentText()) == "mHz":
                c = 1e-3
            elif str(self.sine_f_multiplier.currentText()) == "kHz":
                c = 1e3
            self.sampling_data.f = c * self.sine_f_input.value()
            # phi
            n = 1
            if str(self.sine_phase_mod.currentText()) != "rad":
                self.sampling_data.phi = np.rad2deg(self.sine_phase_input.value())
            else:
                self.sampling_data.phi = self.sine_phase_input.value()

        elif self.type == "u_sine_tab":
            # Vp
            k = 1
            if str(self.u_sine_vp_multiplier.currentText()) == "mV":
                k = 1e-3
            self.sampling_data.Vp = k * self.u_sine_vp_input.value()
            # f
            c = 1
            if str(self.u_sine_f_multiplier.currentText()) == "mHz":
                c = 1e-3
            elif str(self.u_sine_f_multiplier.currentText()) == "kHz":
                c = 1e3
            self.sampling_data.f = c * self.u_sine_f_input.value()
            # phi
            n = 1
            if str(self.u_sine_phase_mod.currentText()) != "rad":
                self.sampling_data.phi = np.rad2deg(self.u_sine_phase_input.value())
            else:
                self.sampling_data.phi = self.u_sine_phase_input.value()

        elif self.type == "am_tab":
            # Vp
            k = 1
            if str(self.am_vp_multiplier.currentText()) == "mV":
                k = 1e-3
            self.sampling_data.Vp = k * self.am_vp_input.value()
            # fc
            c = 1
            if str(self.am_fc_multiplier.currentText()) == "mHz":
                c = 1e-3
            elif str(self.am_fc_multiplier.currentText()) == "kHz":
                c = 1e3
            self.sampling_data.fc = c * self.am_fc_input.value()
            # fm
            m = 1
            if str(self.am_fm_multiplier.currentText()) == "mHz":
                m = 1e-3
            elif str(self.am_fm_multiplier.currentText()) == "kHz":
                m = 1e3
            self.sampling_data.fm = m * self.am_fm_input.value()
            # m
            self.sampling_data.m = self.am_m_input.value()

    def update_sample(self):
        c = 1
        if str(self.sampling_period_multiplier.currentText()) == "mHz":
            c = 1e-3
        elif str(self.sampling_period_multiplier.currentText()) == "kHz":
            c = 1e3
        self.sampling_data.T = c * self.sampling_period_input.value()

        self.sampling_data.dc = self.sampling_dc_input.value() / 100

    def run_simulation(self):
        if plt.get_fignums():
            plt.close()

        # Error messages
        if not self.warnings():
            return False

        # Define Xin
        if self.type == "sine_tab":
            self.t = linspace(0, 10 * (1 / self.sampling_data.f), self.N, endpoint=False)
            self.xin = [self.sampling_data.sine(i) for i in self.t]
            self.fd = self.N / 10 * (1 / self.sampling_data.f)
        elif self.type == "u_sine_tab":
            self.t = linspace(0, 100 * (1 / self.sampling_data.f), self.N, endpoint=False)
            self.xin = [self.sampling_data.u_sine(i) for i in self.t]
            self.fd = self.N / 10 * (1 / self.sampling_data.f)
        elif self.type == "am_tab":
            self.t = linspace(0, 10 * (1 / (min(self.sampling_data.fc, self.sampling_data.fm))), self.N, endpoint=False)
            self.xin = [self.sampling_data.AM(i) for i in self.t]
            self.fd = self.N / 10 * (1 / (min(self.sampling_data.fc, self.sampling_data.fm)))

        # X after anti alias filter
        if self.toggle_antialias.isChecked():
            self.xaa = FiltroAntiAlias(self.xin, self.t)
        else:
            self.xaa = self.xin
        self.t_steady = self.t[len(self.t) // 3: -1]
        self.x_steady = self.xaa[len(self.xaa) // 3: -1]

        # X after Sample & Hold
        if self.toggle_SH.isChecked():
            self.xsh = SampleAndHold(self.t_steady, self.x_steady, self.sampling_data.T, self.sampling_data.dc)
        else:
            self.xsh = self.x_steady

        # X after Analog key
        if self.toggle_analogkey.isChecked():
            self.xak = LlaveAnalogica(self.t_steady, self.xsh, self.sampling_data.T, self.sampling_data.dc)
        else:
            self.xak = self.xsh

        # X after Recovery Filter
        if self.toggle_recovery.isChecked():
            self.xout = FiltroRecuperador(self.xak, self.t_steady)
        else:
            self.xout = self.xak

        self.plot_curves()
        return True

    def plot_curves(self):

        self.plot_spectrum()
        self.plot_time()

        plt.show()

    def plot_time(self):

        plt.figure(1)
        if self.plot_aa and self.toggle_antialias.isChecked():
            plt.plot(self.t_steady, self.x_steady, label="Salida del Filtro Anti-Alias")
        if self.plot_ak and self.toggle_analogkey.isChecked():
            plt.plot(self.t_steady, self.xak, label="Salida de la Llave Analogica")
        if self.plot_sh and self.toggle_SH.isChecked():
            plt.plot(self.t_steady, self.xsh, label="Salida del Sample & Hold")
        if self.plot_Xin:
            xin = self.xin[len(self.xin) // 3: -1]
            plt.plot(self.t_steady, xin, label="Señal de Entrada")
        if self.plot_Xout:
            plt.plot(self.t_steady, self.xout, label="Señal de Salida")

        plt.legend()

    def plot_spectrum(self):

        plt.figure(2)
        if self.plot_aa and self.toggle_antialias.isChecked():
            plt.semilogy(rfftfreq(len(self.x_steady), 1 / self.fd), 1 / len(self.x_steady) * np.abs(rfft(self.x_steady)), label="Salida del Filtro Anti-Alias")
        if self.plot_ak and self.toggle_analogkey.isChecked():
            plt.semilogy(rfftfreq(len(self.xak), 1 / self.fd), 1 / len(self.xak) * np.abs(rfft(self.xak)), label="Salida de la Llave Analogica")
        if self.plot_sh and self.toggle_SH.isChecked():
            plt.semilogy(rfftfreq(len(self.xsh), 1 / self.fd), 1 / len(self.xsh) * np.abs(rfft(self.xsh)), label="Salida del Sample & Hold")
        if self.plot_Xin:
            xin = self.xin[len(self.xin) // 3: -1]
            plt.semilogy(rfftfreq(len(xin), 1 / self.fd), 1 / len(xin) * np.abs(rfft(xin)), label="Señal de Entrada")
        if self.plot_Xout:
            plt.semilogy(rfftfreq(len(self.xout), 1 / self.fd), 1 / len(self.xout) * np.abs(rfft(self.xout)), label="Señal de Salida")

        plt.legend()

    def plot_xin(self):
        # Error messages
        if not self.warnings():
            return False
        self.plot_Xin = not self.plot_Xin
        self.run_simulation()

    def plot_xout(self):
        # Error messages
        if not self.warnings():
            return False
        self.plot_Xout = not self.plot_Xout
        self.run_simulation()

    def plot_AAout(self):
        # Error messages
        if not self.warnings():
            return False
        self.plot_aa = not self.plot_aa
        self.run_simulation()

    def plot_SHout(self):
        # Error messages
        if not self.warnings():
            return False
        self.plot_sh = not self.plot_sh
        self.run_simulation()

    def plot_AKout(self):
        # Error messages
        if not self.warnings():
            return False
        self.plot_ak = not self.plot_ak
        self.run_simulation()

    def warnings(self):
        out = True
        if (self.sampling_data.dc == 0) or (self.sampling_data.T == 0):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error!")
            msg.setText("Error! Actualice los valores de la señal de sampleo!")
            msg.exec_()
            out = False
        if self.type == "sine_tab" or self.type == "u_sine_tab":
            if (self.sampling_data.Vp == 0) or (self.sampling_data.f == 0):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error!")
                msg.setText("Error! Actualice los valores de la señal de entrada!")
                msg.exec_()
                out = False
        elif self.type == "am_tab":
            if (self.sampling_data.Vp == 0) or (self.sampling_data.fm == 0) or (self.sampling_data.fc == 0) or (self.sampling_data.m == 0):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error!")
                msg.setText("Error! Actualice los valores de la señal de entrada!")
                msg.exec_()
                out = False

        return out
