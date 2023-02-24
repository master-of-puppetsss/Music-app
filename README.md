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

- /swagger/ - Документация
- /api/singers/ - Получить список всех певцов или создать нового
- /api/v1/singers/{id}/ - Получить(обновить, удалить) исполнителя по id
- /api/albums/ - Получить список всех альбомов или создать новый
- /api/v1/albums/{id}/ - Получить(обновить, удалить) альбом по id
- /api/songs/ - Получить список всех песен или создать новую
- /api/v1/songs/{id}/ - Получить(обновить, удалить) песню по id
- /api/singers/ - Получить список всех певцов или создать нового
- /api/v1/singers/{id}/ - Получить(обновить, удалить) исполнителя по id
- /api/songs_in_albums/ - Получить список песен в альбомах
- /api/v1/singers/{id}/ - Получить(обновить, удалить) песню в альбоме по id
