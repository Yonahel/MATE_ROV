//Script for controlling thrusters 
#include <Servo.h>

//Looking top-down, we'll orient servos as follows
/*		O1======O2
*		||I1  I2||
*		||      ||
*		||I3  I4||	
*		O3======O4
*/

byte pinO1 = 2;
byte pinO2 = 3;
byte pinO3 = 4;
byte pinO4 = 5;
byte pinI1 = 6;
byte pinI2 = 7;
byte pinI3 = 8;
byte pinI4 = 9;


Servo O1;
Servo O2; 
Servo O3; 
Servo O4; 

Servo I1; 
Servo I2; 
Servo I3; 
Servo I4; 

char EOL = '\n';
String buffer;
int motorSpeed = 0;

void setup(){
 Serial.begin(115200);

 O1.attach(pinO1);
 O1.writeMicroseconds(1300);
 O2.attach(pinO2);
 O2.writeMicroseconds(1300);
 O3.attach(pinO3);
 O3.writeMicroseconds(1300);
 O4.writeMicroseconds(1300);
 O4.attach(pinO4);

 I1.attach(pinI1);
 I1.writeMicroseconds(1300);
 I2.attach(pinI2);
 I2.writeMicroseconds(1300);
 I3.attach(pinI3);
 I3.writeMicroseconds(1300);
 I4.attach(pinI4);
 I4.writeMicroseconds(1300); 

}


void loop(){
 //Read the pi command
 buffer = Serial.readStringUntil(EOL);

 //Check for I or O motor
 if(buffer.charAt(0) == 'I'){
	//Read the speed from the command
	motorSpeed = buffer.substring(2,6).toInt();

	//Send the corresponding motor the speed
	switch(buffer.charAt(1).toInt()){
		case 1:
			I1.writeMicroseconds(motorSpeed);
			break;
		case 2:
			I2.writeMicroseconds(motorSpeed);
			break;
		case 3:
			I3.writeMicroseconds(motorSpeed);
			break;
		case 4:
			I4.writeMicroseconds(motorSpeed);
			break;
	}
 }
 
 if(buffer.charAt(0) == 'O'){
	//Read the speed from the command
	motorSpeed = buffer.substring(3,7).toInt();

	//Send the corresponding motor the speed
	switch(buffer.charAt(1).toInt()){
		case 1:
			O1.writeMicroseconds(motorSpeed);
			break;
		case 2:
			O2.writeMicroseconds(motorSpeed);
			break;
		case 3:
			O3.writeMicroseconds(motorSpeed);
			break;
		case 4:
			O4.writeMicroseconds(motorSpeed);
			break;
	}
 }

}
