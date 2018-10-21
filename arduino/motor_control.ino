//Script for controlling thrusters 
//Fill in below:

Servo FL; //front left servo
Servo FR; //front right servo
Servo BL; //back left servo
Servo BR; //back right servo

Servo F; //Front servo (N)
Servo B; //Back servo (B)
Servo L; //Left servo (L)
Servo R; //Right servo (R)

void setup(){
 Serial.begin(9600);

 FL.attach(1);
 BL.attach(2);
 FR.attach(3);
 BR.attach(4);
  
 F.attach(5);
 B.attach(6);
 L.attach(7);
 R.attach(8);
}

void loop(){

}
