# kafka-lab
# Лабораторная работа №1

## Потоковая обработка данных в реальном времени с использованием Apache Kafka

---

##  Цель работы

Научиться разрабатывать приложения для потоковой обработки данных в реальном времени с использованием Apache Kafka. Реализовать полный цикл: генерация события → Producer → Kafka → Consumer → валидация.

---

##  Задачи

- развернуть Apache Kafka на локальной машине;  
- разработать Kafka Producer для генерации событий каршеринга;  
- разработать Kafka Consumer для получения и проверки сообщений;  
- реализовать генерацию сообщений в формате JSON;  
- проверить корректность передачи данных в реальном времени.  

---

##  Тема лабораторной работы

**Каршеринг**

Producer генерирует события, связанные с арендой автомобилей:

- начало поездки (`start_ride`);  
- завершение поездки (`end_ride`).  

Consumer принимает сообщения, валидирует их и выводит результат в консоль.
---

##  Архитектура приложения

```
Generator → Producer → Apache Kafka → Consumer
```

### Компоненты:

- **generator.py** — генерация сообщений (отделена от Producer согласно принципам SOLID);  
- **producer.py** — отправка сообщений в Kafka;  
- **consumer.py** — получение и проверка сообщений;  
- **Kafka Topic:** `carsharing`.  

---

##  Формат сообщения

Сообщения передаются в формате JSON:

```json
{
  "user": "Anna",
  "car": "Tesla Model 3",
  "action": "start_ride",
  "time": "2026-03-15 19:50:12"
}
```
### Поля сообщения

| Поле   | Описание                         |
| ------ | -------------------------------- |
| user   | имя пользователя                 |
| car    | марка автомобиля                 |
| action | действие (start_ride / end_ride) |
| time   | время события                    |


---

##  Требования

* Python 3.9+
* Apache Kafka
* kafka-python

---

##  Установка зависимостей

```bash
pip install kafka-python
```

---

##  Запуск проекта

### 1. Запуск Zookeeper

```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
```

### 2. Запуск Kafka

```bash
bin/kafka-server-start.sh config/server.properties
```

### 3. Создание топика

```bash
cd C:\Users\ozerova\Downloads\kafka_2.13-4.2.0\bin\windows
kafka-topics.bat --create --topic carsharing --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

---

### 4. Запуск Consumer

```bash
python consumer.py
```

---

### 5. Запуск Producer

```bash
python producer.py
```

---


##  Структура проекта

```
kafka_lab1/
│
├── generator.py
├── producer.py
├── consumer.py
└── README.md
```

---

##  Результат выполнения лабораторной работы

В ходе выполнения лабораторной работы реализована система потоковой обработки данных в реальном времени на основе Apache Kafka.

##  Работа Producer

Producer генерирует события системы каршеринга каждые несколько секунд.

Каждое событие содержит данные о пользователе, автомобиле, действии (start_ride или end_ride) и времени события.

Сообщения выводятся в консоль Producer и отправляются в Kafka-топик carsharing.

## Пример вывода Producer:

Produced: {"user": "Anna", "car": "Tesla Model 3", "action": "start_ride", "time": "2026-03-15 19:50:12"}
Produced: {"user": "Ivan", "car": "BMW i3", "action": "end_ride", "time": "2026-03-15 19:50:14"}
Produced: {"user": "Maria", "car": "Audi e-tron", "action": "start_ride", "time": "2026-03-15 19:50:16"}
##  Работа Consumer

-Consumer принимает сообщения из Kafka-топика carsharing.

-Каждое сообщение проверяется на корректность (валидацию JSON-полей и значения действия).

-В консоль выводятся либо VALID (валидное сообщение), либо NOT VALID (сообщение некорректное).

## Пример вывода Consumer (валидные сообщения):

VALID: {'user': 'Anna', 'car': 'Tesla Model 3', 'action': 'start_ride', 'time': '2026-03-15 19:50:12'}
VALID: {'user': 'Ivan', 'car': 'BMW i3', 'action': 'end_ride', 'time': '2026-03-15 19:50:14'}
VALID: {'user': 'Maria', 'car': 'Audi e-tron', 'action': 'start_ride', 'time': '2026-03-15 19:50:16'}

## Пример вывода Consumer (невалидное сообщение):

NOT VALID: {"user":"Ivan","car":"BMW i3"}

-Такое сообщение считается некорректным, так как отсутствует поле action или time.

## Итоговый результат

-Apache Kafka успешно развернута и работает локально.

-Producer и Consumer корректно обмениваются сообщениями в реальном времени.

-Сообщения валидируются, и некорректные сообщения отсекаются.

-Реализована цепочка Generator → Producer → Kafka → Consumer, демонстрирующая полный цикл потоковой обработки данных.

-Проверено, что система может обрабатывать последовательность событий каршеринга без потерь данных.

##  Используемые технологии

* Apache Kafka — брокер сообщений
* Python — язык программирования
* kafka-python — клиент Kafka для Python
* JSON — формат обмена данными

---

##  Дополнительные материалы

* https://kafka.apache.org
* https://habr.com/ru/companies/otus/articles/789896/
* https://stepik.org/course/258122

---

##  Вывод

В ходе лабораторной работы был изучен принцип потоковой передачи данных с использованием Apache Kafka. Реализованы Producer и Consumer приложения, обеспечивающие генерацию, передачу и проверку сообщений в режиме реального времени.
