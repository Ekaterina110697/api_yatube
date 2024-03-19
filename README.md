# Проект «API для Yatube»
### Yatube - проект социальной сети. «API для Yatube» расширяет возможности социальной сети. Новый функционал позволяет пользователям публиковать свои посты и управлять подписками через программный интерфейс взаимодействия.

#### Реализованы возможности
- Получение, создание, обновление, удаление публикаций.
- Получение, создание, обновление, удаление комментариев к публикациям.
- Просмотр сообществ и детальной информации о них.
- Отслеживание подписок на авторов, а так же возможность подписки на интересующего автора поста.
- Получение, обновление и проверка JWT авторизации.
#### Технологии
- Python
- Django
- Django REST Framework
- Simple JWT

#### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Ekaterina110697/api_yatube.git
```
```
cd api_final_yatube
```
#### Создать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
```
#### Установить зависимости из файла requirements.txt: 
```
pip install -r requirements.txt
```
#### Выполнить миграции: 
```
python3 manage.py migrate
```
#### Запустить проект: 
```
python3 manage.py runserver
```

После запуска проекта, документация будет доступна по адресу:
```
http://localhost:port/redoc/
```
# Примеры

Для доступа к API необходимо получить JWT-токен: выполнить POST-запрос localhost:8000/api/v1/token/, передав поля username и password.

При дальнейшей отправке запросов токен передается в заголовке Authorization: Bearer <токен>

Примеры обращения к методам и ответов:

## 1)

/api/v1/posts/ (GET, POST)

ответ API на GET-запрос:


```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

POST-запрос:

```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
ответ API на POST-запрос:

```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
## 2)

/api/v1/groups/ (GET)

ответ API на GET-запрос:

```
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  }
]
```
