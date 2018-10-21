import time

class PID:
    def __init__(self, P, I, D):

        self.Kp = P
        self.Ki = I
        self.Kd = D

        self.sampleTime = 0.00
        self.current_time = time.time()
        self.last_time = self.current_time

        self.clear()

    def clear(self):
        self.setPoint = 0.0

        self.PTerm = 0.0
        self.ITerm = 0.0
        self.DTerm = 0.0
        self.last_error = 0.0

        # Anti Windup
        self.antiWindup = 20.0

        self.output = 0.0

    def setKp(self, proportional):
        self.Kp = proportional

    def setKi(self, integral):
        self.Ki = integral

    def setKd(self, derivative):
        self.Kd = derivative

    def setWindup(self, windup):
        self.antiWindup = windup

    def setSampleTime(self, sampleTime):
        self.sampleTime = sampleTime

    def update(self, feedback_value):
        error = self.setPoint - feedback_value

        self.current_time = time.time()
        dTime = self.current_time - self.last_time
        dError = error - self.last_error

        if (dTime >= self.sampleTime):
            self.PTerm = self.Kp * error
            self.ITerm += error * dTime

            if (self.ITerm < self.antiWindup * -1):
                self.ITerm = self.antiWindup * -1
            elif (self.ITerm > self.antiWindup):
                self.ITerm = self.antiWindup

            self.DTerm = 0.0
            if dTime > 0:
                self.DTerm = dError / dTime

            # Store time and error for the next update
            self.last_time = self.current_time
            self.last_error = error
pi
            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)
