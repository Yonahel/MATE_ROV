def pidControl(sensor_r, sensor_y, sensor_p, rP, rI, rD, pP, pI, pD, yP, yI, yD, setPoint=0.0, sampleTime=0.1):
    roll_pid = PID(rP, rI, rD)
    pitch_pid = PID(pP, pI, pD)
    yaw_pid = PID(yP, yI, yD)

    roll_pid.setPoint = setPoint
    pitch_pid.setPoint = setPoint
    yaw_pid.setPoint = setPoint

    roll_pid.setSampleTime(sampleTime)
    pitch_pid.setSampleTime(sampleTime)
    yaw_pid.setSampleTime(sampleTime)

    # WORK IN PROGRESS
