int bluePin = 9;   // Синий
int greenPin = 10; // Зеленый
int redPin = 11;   // Красный

int brightness = 100; // Максимальная яркость (0-255, но можно уменьшить до 100)

void setup() {
  pinMode(bluePin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(redPin, OUTPUT);
}

void loop() {
  // Плавный переход от синего к зеленому
  fadeColors(brightness, 0, 0, 0, brightness, 0, 3);
  // Плавный переход от зеленого к красному
  fadeColors(0, brightness, 0, 0, 0, brightness, 3);
  // Плавный переход от красного к синему
  fadeColors(0, 0, brightness, brightness, 0, 0, 3);
}

// Функция плавного переливания между двумя цветами
void fadeColors(int b1, int g1, int r1, int b2, int g2, int r2, int speed) {
  for (int i = 0; i <= 255; i++) {
    int b = map(i, 0, 255, b1, b2);
    int g = map(i, 0, 255, g1, g2);
    int r = map(i, 0, 255, r1, r2);
    setColor(b, g, r);
    delay(speed);
  }
}

// Функция управления цветом (BGR)
void setColor(int b, int g, int r) {
  analogWrite(bluePin, b);
  analogWrite(greenPin, g);
  analogWrite(redPin, r);
}
