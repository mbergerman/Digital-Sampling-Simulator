import matplotlib.pyplot as plt
import numpy as np


class sampling_data:

    def __init__(self, Vp=0, f=0, fc=0, fm=0, m=0, dc=0, T=0, sigma=0, phi=0):
        self.Vp = Vp  # Tension maxima
        self.f = f  # frecuencia de la señal
        self.fc = fc  # frecuencia de la portadora (AM)
        self.fm = fm  # frecuencia de la modulante (AM)
        self.m = m  # coeficiente de modulación (AM)
        self.sigma = sigma  # constante de tiempo de la exponencial
        self.phi = phi  # desfasaje de la señal (sine & 3/2sine)
        self.dc = dc  # duty cycle de la señal de sampleo
        self.T = T  # Periodo de la señal de sampleo

    def sine(self, t):
        return self.Vp * np.cos(2 * np.pi * self.f * t + self.phi)

    def u_sine(self, t):
        fu = self.f / 5
        Tu = 15 / (2 * self.f)
        if t > Tu:
            n = np.floor(t / Tu)
            t = t - n * Tu
        return self.Vp * np.sin(2 * np.pi * fu * t + self.phi)

    def AM(self, t):
        return self.Vp * np.cos(2 * np.pi * self.fc * t) * (1 + self.m * np.cos(2 * np.pi * self.fm * t))
