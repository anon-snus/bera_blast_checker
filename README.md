# Bera Blast Checker

Этот скрипт проверяет дроп на сайте [Blast Bera](https://www.blastbera.fun/).

## Как использовать

1. **Заполните файл `addresses`**:
   Добавьте публичные адреса кошельков в файл `addresses`, каждый адрес на новой строке.

2. **Настройте конфигурацию**:
   Откройте файл `config` и настройте параметры:
   - `proxy_use = False` — установите `True`, если хотите использовать мобильные прокси.
   - `PROXY = 'http://'` — укажите адрес прокси, если `proxy_use = True`.
   - `CHANGE_IP_LINK = 'https://changeip.mobileproxy.space/?proxy_key&format=json'` — укажите ссылку для смены IP, если используете мобильные прокси.

2. **Запустите скрипт**:
   python main.py
