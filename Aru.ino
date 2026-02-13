int ledPin = 7;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command == "ON") {
      digitalWrite(ledPin, HIGH);
    }

    if (command == "OFF") {
      digitalWrite(ledPin, LOW);
    }
  }
}
