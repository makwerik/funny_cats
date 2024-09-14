# Используем базовый образ Python 3
FROM python:3.10-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1  # Не записывать файлы .pyc
ENV PYTHONUNBUFFERED 1         # Обеспечить вывод в режиме реального времени

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем всё содержимое проекта в контейнер
COPY . /app/

# Открываем порт для доступа к серверу Django (по умолчанию 8000)
EXPOSE 8000

# Запускаем команду миграции и сервер
CMD ["python", "manage.py", "migrate"] && \
    ["python", "manage.py", "runserver", "0.0.0.0:8000"]
