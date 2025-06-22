"""
Точка входа. Запускает Telegram-бота (polling).
"""

from telegram.ext import ApplicationBuilder
import config
from handlers import get_handlers


def main() -> None:
    # Создаём приложение python-telegram-bot
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()

    # Регистрируем обработчики
    for handler in get_handlers():
        app.add_handler(handler)

    # Запускаем бесконечный polling
    print("Bot started. Press Ctrl+C to stop.")
    app.run_polling(allowed_updates=["message", "callback_query"])


if __name__ == "__main__":
    main()
