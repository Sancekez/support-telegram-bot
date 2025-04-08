1. Установите Python
Убедитесь, что у вас установлен Python 3. Проверьте, введя команду:

python --version или python3 --version



2. Создайте и активируйте виртуальное окружение (по желанию)
Рекомендуется использовать виртуальное окружение:

python -m venv venv
source venv/bin/activate  # для macOS/Linux
venv\Scripts\activate     # для Windows



3. Установите зависимости
Установите библиотеку python-telegram-bot:

pip install python-telegram-bot --upgrade



4. Получите токен бота

Откройте Telegram и найдите бота @BotFather.
Отправьте команду /newbot и следуйте инструкциям.
Скопируйте полученный API Token.



5. Добавьте токен в код
Откройте файл с кодом и замените:

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

на ваш реальный токен.



6. Запустите бота
В терминале запустите скрипт:

python main.py или python3 main.py



7. Протестируйте бота
Откройте Telegram.

Найдите своего бота (по имени или юзернейму).
Начните чат и отправьте команду /start.
Проверьте ответы на сообщения.
