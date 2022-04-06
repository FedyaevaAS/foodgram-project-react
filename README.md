# Проект «Продуктовый помощник»
### Описание
На этом сервисе пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.
### Данные для входа в админ-зону
- username: admin
- password: admin

### Адрес сервера 
- 51.250.13.21

### Шаблон наполнения env-файла
```
DB_ENGINE=
DB_NAME=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=
SECRET_KE=
```

### Команды для запуска приложения в контейнерах
Собрать и запустить контейнеры:
```
docker-compose up -d --build
```
Выполнить миграции:
```
docker-compose exec backend python manage.py migrate
```
Создать суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```
Собрать статику:
```
docker-compose exec backend python manage.py collectstatic --no-input
```
Загрузить данные в БД:
```
docker-compose exec backend python manage.py datatodb
```
Остановить контейнеры:
```
docker-compose down -v 
```
### Автор
Федяева Анастасия

![example workflow](https://github.com/FedyaevaAS/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)