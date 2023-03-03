
## Music app

API-сервис для управления каталогом исполнителей, композиций и альбомов

### Стек технологий
`Python 3.8`
`Django 4.1.7`
`Django REST Framework 3.14.0`


## Установка и запуск

1. Cклонировать репозиторий `https://github.com/master-of-puppetsss/nested-menu.git`

2. Создать и заполнить .env файл по аналогии с .env.example

3. Создать и заполнить .env.db файл по аналогии с env.db.example

4. Запустить контейнер с сервисами

  ```
  sudo docker-compose up -d --build
  ```


  При первом запуске выполните следующие команды:

  ```
  sudo docker-compose exec web python manage.py migrate
  sudo docker-compose exec web python manage.py createsuperuser
  sudo docker-compose exec web python manage.py collectstatic --no-input
  ```

## Переменные окружения

Чтобы запустить этот проект, вам нужно будет добавить следующие переменные окружения в ваш файл .env

`DEBUG` `SECRET_KEY` `DJANGO_ALLOWED_HOSTS` `DATABASE_NAME` `DATABASE_USER` `DATABASE_PASSWORD` `DATABASE_HOST` `DATABASE_PORT`

Также в .env.db добавить следующие переменные:

`POSTGRES_DB` `POSTGRES_USER` `POSTGRES_PASSWORD`

