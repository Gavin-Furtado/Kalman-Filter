#include <Arduino.h>
#define onboard 13

// put function declarations here:
// int myFunction(int, int);

void setup() {
  // put your setup code here, to run once:
  pinMode(onboard, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(onboard,LOW);
  delay(1000);
  digitalWrite(onboard,HIGH);
  delay(1000);
}

// put function definitions here:
// int myFunction(int x, int y) {
//   return x + y;
// }