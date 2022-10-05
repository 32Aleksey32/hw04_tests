# hw04_tests, спринт №5 в Яндекс.Практикум
### Покрытие проекта Yatube тестами
Использованный стек:
- django-debug-toolbar==2.2
- django==2.2.16
- pytest-django==3.8.0
- pytest-pythonpath==0.7.3
- pytest==5.3.5
- requests==2.22.0
- six==1.14.0
- sorl-thumbnail==12.6.3
- mixer==7.1.2
- Faker==12.0.1

## Настройка и запуск на компьютере
Клонируем проект:
```
https://github.com/32Aleksey32/hw04_tests.git
```
Переходим в папку с проектом:
```
cd hw04_tests
```
Устанавливаем виртуальное окружение:
```
python -m venv venv
```
Активируем виртуальное окружение:
```
source venv/Scripts/activate
```
Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
Применяем миграции:
```
python yatube/manage.py makemigrations
python yatube/manage.py migrate
```
Создаем супер пользователя:
```
python yatube/manage.py createsuperuser
```
Запускаем проект:
```
python yatube/manage.py runserver
```
После чего проект будет доступен по адресу http://127.0.0.1/

Заходим в http://127.0.0.1/admin и создаем группы и записи. После чего записи и группы появятся на главной странице.
