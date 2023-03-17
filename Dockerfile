# базовый образ для Python
FROM python:3.11

# устанавливаем зависимости, используемые в Django проекте
RUN pip install --upgrade pip

# создаём директорию для нашего приложения
RUN mkdir /code

# задаём рабочую директорию
WORKDIR /code

# копируем содержимое нашего приложения в рабочую директорию контейнера
COPY . /code/

# устанавливаем файлы зависимостей
RUN pip install -r requirements.txt

# устанавливаем переменную окружения
ENV PYTHONUNBUFFERED 1
