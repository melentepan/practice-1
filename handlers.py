from telegram import Update
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    MessageHandler,
    filters,
)

import config
import messages
import keyboards


async def start_command(update: Update, context: CallbackContext) -> None:
    """Обработчик /start."""
    await update.message.reply_text(
        messages.WELCOME,
        reply_markup=keyboards.main_menu_keyboard(),
        disable_web_page_preview=True,
    )


async def help_command(update: Update, context: CallbackContext) -> None:
    """Команда /help."""
    await update.message.reply_text(
        "Используй /start, чтобы открыть главное меню.\n"
        "Нажимай на кнопки и получай информацию о проекте Smart Parking."
    )


async def button_handler(update: Update, context: CallbackContext) -> None:
    """Обработка нажатий на Inline-кнопки."""
    query = update.callback_query
    data = query.data
    await query.answer()  # Закрываем «часики» у пользователя

    # Выбираем нужный текст
    if data == "about":
        text = messages.ABOUT
    elif data == "goals":
        text = messages.GOALS
    elif data == "tech":
        text = messages.TECHNOLOGIES
    elif data == "ui":
        text = messages.INTERFACE
    elif data == "testing":
        text = messages.TESTING
    elif data == "results":
        text = messages.RESULTS
    elif data == "team":
        text = config.TEAM_INFO
    elif data == "docs":
        text = messages.documentation(
            config.DOCUMENTATION_LINKS["presentation"],
            config.DOCUMENTATION_LINKS["report"],
        )
    elif data == "menu":
        # Вернуться к главному меню
        await query.edit_message_text(
            messages.WELCOME,
            reply_markup=keyboards.main_menu_keyboard(),
            disable_web_page_preview=True,
        )
        return

    # Отображаем выбранный раздел + 1 кнопка «Назад»
    await query.edit_message_text(
        text,
        reply_markup=keyboards.back_to_menu_keyboard(),
        parse_mode="HTML",
        disable_web_page_preview=True,
    )


async def unknown_command(update: Update, context: CallbackContext) -> None:
    """Ответ на неизвестные команды."""
    await update.message.reply_text(
        "Неизвестная команда. Используйте /start для возврата в меню."
    )


def get_handlers() -> list:
    """Возвращает список всех обработчиков для регистрации в приложении."""
    return [
        CommandHandler("start", start_command),
        CommandHandler("help", help_command),
        CallbackQueryHandler(button_handler),
        MessageHandler(filters.COMMAND, unknown_command),  # перехват неизвестных команд
    ]
