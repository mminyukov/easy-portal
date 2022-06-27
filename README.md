# Простой портал для агрегации ссылок

Основная задача этого приложения - объеденить все ссылки на множество сервисов в одном месте.

## Интерфейс

![image](/images/interface.png)

## settings.conf

Для настройки приложения используется файл [settings.conf](app/settings.conf)

Для перечисления всех сервисов используется секция [card.N], где N - порядковый номер карточки

| Секция | Параметр | Тип | Описание |
|-----------|------|----|----------|
| main | titleSite | string | Заголовок страницы |
| main | header | string | Заголовок шапки сайта |
| questionbutton | enable | boolean | Включение кнопки вопроса |
| questionbutton | title | string | Заголовок сообщения кнопки |
| questionbutton | content | string | Сообщение кнопки |
| banner | enable | boolean | Включение баннера с сообщением |
| banner | title | string | Заголовок банера |
| banner | content | string | Сообщение банера |
| card.N | title | string | Заголовок карточки сервиса |
| card.N | description | string | Описание карточки сервиса |
| card.N | link | string | Ссылка на сервис |

## Запуск

Для запуска приложения требуется python3 и flask

Установка flask

```bash
pip3 install flask
```

Запуск приложения
```bash
python3 main.py
```

## Docker образ

Сборка docker образа
```bash
docker build -t simple-portal:1.0 .
```

Запуск docker образа
```bash
docker run -d -p5000:5000 simple-portal:1.0
```

Запуск docker образа через docker-compose
```bash
docker-compose up --build
```