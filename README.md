## Music app
### Стек технологий
- Python 3.8
- Django 4.1.7
- Django REST Framework 3.14.0

### Установка и запуск

1. Cклонировать репозиторий `https://github.com/master-of-puppetsss/music_app.git`

2. Создать и заполнить .env и .env.db файлы по аналогии

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

### Описание API:
`Документация` -/swagger/
`Список всех исполнителей или создание нового` - /api/singers/ 
`Получить(обновить, удалить) исполнителя по id` - /api/v1/singers/{id}/
`Список всех альбомов или создание нового` - /api/albums/
`Получить(обновить, удалить) альбом по id` - /api/v1/albums/{id}/
`Список всех композиций или создание новой` - /api/songs/
`Получить(обновить, удалить) композицию по id` - /api/v1/songs/{id}/
`Список песен в альбомах или создание новой` - /api/songs_in_albums/
`Получить(обновить, удалить) песню в альбоме по id` - /api/v1/singers/{id}/
