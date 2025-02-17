
# Cat Breeder API

## Описание
SUPERUSER: admin:admin
Это простое приложение на Django с использованием Django Rest Framework (DRF) для управления котами и их владельцами (заводчиками). Оно включает в себя базовые операции CRUD для работы с котами и авторизацию пользователей с использованием токенов.

Приложение упаковано в Docker и использует SQLite в качестве базы данных.

## Технологии
- Python 3.10
- Django
- Django Rest Framework
- Docker
- SQLite (дефолтная база данных)

## Установка и запуск

### Шаг 1: Клонирование репозитория
Клонируйте этот репозиторий на свой локальный компьютер

### Шаг 2: Создание Docker-контейнера

Приложение настроено для работы в Docker-контейнере.

#### Соберите Docker-образ:
```bash
docker build -t my_django_app .
```

#### Запустите контейнер:
```bash
docker run -p 8000:8000 my_django_app
```

### Шаг 3: Доступ к приложению

Откройте браузер и перейдите по адресу `http://localhost:8000`, чтобы увидеть ваше приложение.

## Использование

### Получение токена аутентификации
Чтобы работать с API, сначала получите токен для пользователя. Выполните запрос для получения токена:

```
POST /api/auth/
```
Пример запроса с использованием `curl`:

```bash
curl -X POST http://localhost:8000/api/auth/ -d "username=<your_username>&password=<your_password>"
```

### Пример использования API (CRUD операции с котами)

#### Получить список котов (только свои коты):
```
GET /api/cats/
```

Пример запроса с использованием токена:

```bash
curl -X GET http://localhost:8000/api/cats/ -H "Authorization: Token <your_token>"
```

#### Создать нового кота:
```
POST /api/cats/
```

Пример запроса с использованием `curl`:

```bash
curl -X POST http://localhost:8000/api/cats/ -H "Authorization: Token <your_token>" -H "Content-Type: application/json" -d '{
  "name": "Барсик",
  "age": 3,
  "breed": "Сиамский",
  "is_furry": true
}'
```

#### Редактировать данные кота:
```
PUT /api/cats/<id>/
```

#### Удалить кота:
```
DELETE /api/cats/<id>/
```

## Документация API

Swagger-документация доступна по адресу:

```
http://localhost:8000/swagger/
```

## Контейнеризация с Docker

- `Dockerfile` — файл с инструкциями для сборки образа приложения.
- База данных SQLite используется по умолчанию и хранится внутри контейнера.

Для сохранения базы данных между перезапусками контейнера используйте volume:

```bash
docker run -p 8000:8000 -v $(pwd)/db.sqlite3:/app/db.sqlite3 my_django_app
```


