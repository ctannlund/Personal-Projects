//www.elegoo.com
//2016.12.8

// Define Pins
#define BLUE 5
#define GREEN 3
#define RED 6
int redValue;
int greenValue;
int blueValue;
int thermistor = A1;
int value;

void setup()
{
Serial.begin(9600);
pinMode(RED, OUTPUT);
pinMode(GREEN, OUTPUT);
pinMode(BLUE, OUTPUT);
pinMode(A1, INPUT);
digitalWrite(RED, HIGH);
digitalWrite(GREEN, LOW);
digitalWrite(BLUE, LOW);
}


// main loop
void loop()
{
  value = analogRead(thermistor);
  Serial.println(value);
  if (value >= 525) {
    redValue = 255;
    blueValue = 0;
    greenValue = 0;
    analogWrite(RED, redValue);
    analogWrite(GREEN, greenValue);
    analogWrite(BLUE, blueValue);
  }
  else if (value <= 485){
    redValue = 129;
    blueValue = 247;
    greenValue = 245;
    analogWrite(RED, redValue);
    analogWrite(GREEN, greenValue);
    analogWrite(BLUE, blueValue);
  }
  else{
    redValue = 5;
    blueValue = 5;
    greenValue = 5;
    analogWrite(RED, redValue);
    analogWrite(GREEN, greenValue);
    analogWrite(BLUE, blueValue);
  }
  delay(500);
}
