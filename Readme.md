# Test stripe backend
Бекенд интегрированный с Stripe Api
### Функционал
- Пользователь может получить инофрмацию о Item и перейти на страницу оплаты в stripe
- Пользователь может получить session id для оплаты Item в stripe
- Пользователь может добавлять новые Item через django admin
### Запуск
Для запуска заполните .env в соответствии с env.example, после чего
```bash
docker compose up --build app -d
```