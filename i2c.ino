

// Includin the Wire library for I2C
#include <Wire.h>

// LED position
const int red = 11;  
const int green = 13;  
const int yellow = 16;   

void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  
  // Setup pin 13 as output and turn LED off
  pinMode(red, OUTPUT);  
  digitalWrite(red, LOW); 
  pinMode(green, OUTPUT);
  digitalWrite(green, LOW);
  pinMode(yellow, OUTPUT);
  digitalWrite(yellow, LOW);
}

// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); 
    
    if(c == 0)
    {
      digitalWrite(red, 0); 
      digitalWrite(green, 0); 
      digitalWrite(yellow, 0); 
    }
    
    else if(c == 1)
    {
      digitalWrite(red, 1); 
      digitalWrite(green, 0); 
      digitalWrite(yellow, 0);  
    }
    
    else if(c == 2)
    {
      digitalWrite(red, 0);  
      digitalWrite(green, 1); 
      digitalWrite(yellow, 0); 
    }

    else if(c == 3)
    {
      digitalWrite(red, 0);  
      digitalWrite(green, 0);  
      digitalWrite(yellow, 1);   
    }
  }
}


void loop() {
  delay(100);
}
