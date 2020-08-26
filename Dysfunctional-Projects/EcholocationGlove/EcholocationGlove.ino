#include <NewPing.h>

#define TRIGGER_PIN 10
#define ECHO_PIN 13
#define MAX_DISTANCE 400
#define VIBE_PIN 12

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

float duration, distance;

void setup() {
  Serial.begin(9600);
  pinMode(VIBE_PIN, OUTPUT);
}

void loop() {

  duration = sonar.ping();

  distance = ( duration / 2 ) * 0.0343;

  Serial.print("Distance = ");
  if (distance >= 400 || distance <=2) {
    Serial.println("Out of range");
    digitalWrite(VIBE_PIN, LOW);
  }
  else{
    Serial.print(distance);
    Serial.println(" cm");
    delay(500);
    digitalWrite(VIBE_PIN, HIGH);
  }
  delay(500);
}
