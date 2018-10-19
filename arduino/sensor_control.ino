#include <Wire.h>

const int MPU_ADDRESS = 0x68;

int16_t accelerometer_x, accelerometer_y, accelerometer_z;

int16_t gyroscope_x, gyroscope_y, gyroscope_z;

void setup() {
  
 Serial.begin(9600);
 
 Wire.begin();
 
 Wire.beginTransmission(MPU_ADDRESS);//Begins transmission to GY-521 board
 
 Wire.write(0x6B);//PWR_MGMT_1 register
 
 Wire.write(0); //Set to 0 (Wakes up MPU)
 
 Wire.endTransmission(true);
 
}

void loop() {

 Serial.write(0);//writes 0 to serial port to indicate to ROS code that nothing is being transmitted

 Wire.beginTransmission(MPU_ADDRESS);
 
 Wire.write(0x3B);//requests to read the 0x3B register (ACCEL_XOUT_H)
 
 Wire.endTransmission(false);//Indicates that the Arduino will send a restart, so the connection is kept active

 Wire.requestFrom(MPU_ADDRESS, 7*2, true);//Requets a total of 14 registers (2 for each of acceleration x, y and z, gyro x, y and z, and temperature)

 readImuData();
  
 Serial.write(1);//Indicates to ROS that transmission will begin
  
 sendImuData();
 
}

void readImuData() {

 //Wire.read()<<8 | Wire.read() reads two registers at a time and stores them in the same variable
 //<<8 shifts the bites by 8 positions left and | copies a bit in each operand (fist 8 bits is one register and the last 8 bits are the second one)
 
 accelerometer_x = Wire.read()<<8 | Wire.read();//reads regitser 0x3B (ACCEL_XOUT_H) and 0x3C (ACCEL_XOUT_L)

 accelerometer_y = Wire.read()<<8 | Wire.read();//reads regitser 0x3D (ACCEL_YOUT_H) and 0x3E (ACCEL_YOUT_L)

 accelerometer_z = Wire.read()<<8 | Wire.read();//reads regitser 0x3F (ACCEL_ZOUT_H) and 0x40 (ACCEL_ZOUT_L)
 
 Wire.write(0x43);//Skips registers 0x41 and 0x42 which store temperature and goes to register 0x43 (GYRO_XOUT_H)

 gyroscope_x = Wire.read()<<8 | Wire.read();//reads regitser 0x43 (GYRO_XOUT_H) and 0x44 (GYRO_XOUT_L)

 gyroscope_y = Wire.read()<<8 | Wire.read();//reads regitser 0x45 (GYRO_YOUT_H) and 0x46 (GYRO_YOUT_L)

 gyroscope_x = Wire.read()<<8 | Wire.read();//reads regitser 0x47 (GYRO_ZOUT_H) and 0x48 (GYRO_ZOUT_L)
  
}

void sendImuData() {

 Serial.write(accelerometer_x);
 Serial.write(accelerometer_y);
 Serial.write(accelerometer_z);
 Serial.write(gyroscope_x);
 Serial.write(gyroscope_y);
 Serial.write(gyroscope_z);
  
}
