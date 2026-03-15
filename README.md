# kafka-lab
# Лабораторная работа №1

## Потоковая обработка данных в реальном времени с использованием Apache Kafka

---

##  Цель работы

Изучить принципы потоковой обработки данных в реальном времени и научиться разрабатывать приложения, взаимодействующие с брокером сообщений Apache Kafka с использованием Producer и Consumer.

---

##  Задачи

* развернуть Apache Kafka;
* разработать Kafka Producer;
* разработать Kafka Consumer;
* реализовать генерацию сообщений в формате JSON;
* выполнить валидацию получаемых данных;
* реализовать полный цикл передачи данных Producer → Kafka → Consumer.

---

##  Тема лабораторной работы

**Библиотека**

Producer генерирует события, связанные с работой библиотеки:

* выдача книги (`borrow`);
* возврат книги (`return`).

Consumer принимает сообщения, проверяет их корректность и выводит результат в консоль.

---

##  Архитектура приложения

```
Generator → Producer → Apache Kafka → Consumer
```

### Компоненты:

* **generator.py** — генерация сообщений (отделена от Producer согласно принципам SOLID);
* **producer.py** — отправка сообщений в Kafka;
* **consumer.py** — получение и валидация сообщений;
* **Kafka Topic:** `library`.

---

##  Формат сообщения

Сообщения передаются в формате JSON:

```json
{
  "user": "Ivan",
  "book": "1984",
  "action": "borrow",
  "time": "2026-03-15 19:10:32"
}
```

### Поля сообщения

| Поле   | Описание                   |
| ------ | -------------------------- |
| user   | имя пользователя           |
| book   | название книги             |
| action | действие (borrow / return) |
| time   | время события              |

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
bin/kafka-topics.sh --create \
--topic library \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1
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

##  Ожидаемый результат

Producer генерирует сообщения и отправляет их в Kafka.

Consumer получает сообщения:

```
VALID: {'user': 'Ivan', 'book': '1984', 'action': 'borrow', 'time': '2026-03-15 19:10:32'}
```

Если сообщение некорректно:

```
NOT VALID: <message>
```

---

## 📁 Структура проекта

```
kafka_lab1/
│
├── generator.py
├── producer.py
├── consumer.py
└── README.md
```

---

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
