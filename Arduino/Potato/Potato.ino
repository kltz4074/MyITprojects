void setup() {
    Serial.begin(9600); // Запуск Serial с 9600 бод
}

void loop() {
    int sensorValue = analogRead(A0); // Читаем напряжение с картошки
    float voltage = sensorValue * (5.0 / 1023.0); // Преобразование в Вольты
    
    Serial.println(voltage); // Отправка данных в COM-порт
    delay(1000); // Пауза 1 секунда
}
