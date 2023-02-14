# Test stripe backend
Бекенд интегрированный с Stripe Api. Ветка с выполненными дополнительными заданиями, базовое задание можно найти в ветке base_task.
### Функционал
- Пользователь может получить инофрмацию о Item и добавлять их в Order
- Пользователь может получить session id для оплаты Order в stripe
- Пользователь может менять количество/удалять Item в Order
- Кнопка Buy перенаправляет на оплату заказа с помощью JS скрипта
- Админ может добавлять новые Item через django admin
### Запуск
Для запуска заполните .env в соответствии с env.example, после чего
```bash
docker compose up --build app -d
```
Для создания суперпользователя
```bash
docker exec -it <containter id> python manage.py createsuperuser
```
