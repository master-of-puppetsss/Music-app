
## Music app

API-сервис для управления каталогом исполнителей, композиций и альбомов

### Стек технологий
`Python 3.8`
`Django 4.1.7`
`Django REST Framework 3.14.0`


## Установка и запуск

1. Cклонировать репозиторий `git@github.com:iricshkin/singers-drf-project.git`

2. Создать и заполнить .env файл по аналогии с .env.example

3. Запустить контейнер с сервисами

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
## Описание API

- `/swagger/` - документация
- `/api/singers/` - Список всех исполнителей или создание нового
- `/api/singers/{id}/` - Получить(обновить, удалить) исполнителя по id
- `/api/albums/` - Список всех альбомов или создание нового
- `/api/albums/{id}/` - Получить(обновить, удалить) альбом по id
- `/api/songs/` - Список всех композиций или создание новой
- `/api/songs/{id}/` - Получить(обновить, удалить) композицию по id
- `/api/songs_in_albums/` - Список песен в альбомах или создание новой
- `/api/songs_in_albums/{id}/` - Получить(обновить, удалить) песню в альбоме по id

