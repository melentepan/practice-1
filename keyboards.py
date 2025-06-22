from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu_keyboard() -> InlineKeyboardMarkup:
    """Главное меню с разделами."""
    buttons = [
        [
            InlineKeyboardButton("🔍 О проекте", callback_data="about"),
            InlineKeyboardButton("🎯 Цели и задачи", callback_data="goals"),
        ],
        [
            InlineKeyboardButton("⚙️ Технологии", callback_data="tech"),
            InlineKeyboardButton("📱 Интерфейс", callback_data="ui"),
        ],
        [
            InlineKeyboardButton("🧪 Тестирование", callback_data="testing"),
            InlineKeyboardButton("📊 Результаты и польза", callback_data="results"),
        ],
        [
            InlineKeyboardButton("👥 Команда", callback_data="team"),
            InlineKeyboardButton("📂 Документация", callback_data="docs"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)


def back_to_menu_keyboard() -> InlineKeyboardMarkup:
    """Кнопка возврата на главное меню."""
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("⬅️ Назад к меню", callback_data="menu")]]
    )
