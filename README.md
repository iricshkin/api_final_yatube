# api_final

[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)

## Описание

### API для социальной сети YaTube

**_Реализован функционал, дающий возможность:_**

- Подписываться на пользователя.
- Просматривать, создавать новые, удалять и изменять посты.
- Просматривать и создавать группы.
- Комментировать, смотреть, удалять и обновлять комментарии.
- Фильтровать по полям.

---

## Установка

**Склонировать проект:**

```
git clone https://github.com/iricshkin/api_final_yatube.git
```

**Cоздать и активировать виртуальное окружение:**

```
python -m venv venv
```

```
source venv/Scripts/activate
```

**Установить зависимости из файла requirements.txt:**

```
pip install -r requirements.txt
```

**Выполнить миграции:**

```
python manage.py migrate
```

**Запустить проект:**

```
python3 manage.py runserver
```

## Примеры

**_Примеры обращения к API:_**

- /redoc/ - Документация
- /jwt/create/ - Получить JWT-токен
- /jwt/refresh/ - Обновить JWT-токен
- /jwt/verify/ - Проверить JWT-токен
- /posts/ - Получить список всех публикаций / Создать новую публикацию
- /posts/{id}/ - Получить публикацию по id / Обновить по id / Удалить по id
- /posts/{post_id}/comments/ - Получить список комментариев
- /posts/{post_id}/comments/{comment_id}/ - Получить комментарий по id / Создать комментарий / Обновить / Удалить комментарий
- /follow/ - Получить список подписок / Создать подписку
- /groups/ - Получить список всех групп
- /groups/{id}/ - Получение информации о сообществе по id
