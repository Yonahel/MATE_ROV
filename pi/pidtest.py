# WORK IN PROGRESS

from pid import PID
import time
import scipy.interpolate
import matplotlib.pyplot as plt
import numpy as np

def test_pid(P, I, D, sampleTime):
    pidControl = PID(P, I, D)

    pidControl.setPoint = 0.0
    pidControl.setSampleTime(0.01)
