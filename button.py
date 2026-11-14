from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def make_menu(rows):
    return InlineKeyboardMarkup(inline_keyboard=rows)


# MAIN MENU
menu = make_menu([
    [
        InlineKeyboardButton(text="📱 Samsung", callback_data="brand_samsung"),
        InlineKeyboardButton(text="🍎 iPhone", callback_data="brand_iphone"),
    ],
    [
        InlineKeyboardButton(text="📱 Xiaomi", callback_data="brand_xiaomi"),
        InlineKeyboardButton(text="✨ Google Pixel", callback_data="brand_pixel"),
    ],
])

# SAMSUNG
samsung_menu = make_menu([
    [InlineKeyboardButton(text="Galaxy S25 Ultra", callback_data="model_samsung_1")],
    [InlineKeyboardButton(text="Galaxy S25+", callback_data="model_samsung_2")],
    [InlineKeyboardButton(text="Galaxy Z Fold7", callback_data="model_samsung_3")],
    [InlineKeyboardButton(text="Galaxy A56", callback_data="model_samsung_4")],
    [InlineKeyboardButton(text="⬅️ Back", callback_data="back")],
])

# IPHONE
iphone_menu = make_menu([
    [InlineKeyboardButton(text="iPhone 17 Pro Max", callback_data="model_iphone_1")],
    [InlineKeyboardButton(text="iPhone 17 Pro", callback_data="model_iphone_2")],
    [InlineKeyboardButton(text="iPhone Air", callback_data="model_iphone_3")],
    [InlineKeyboardButton(text="iPhone 17", callback_data="model_iphone_4")],
    [InlineKeyboardButton(text="⬅️ Back", callback_data="back")],
])

# XIAOMI
xiaomi_menu = make_menu([
    [InlineKeyboardButton(text="Xiaomi 15 Ultra", callback_data="model_xiaomi_1")],
    [InlineKeyboardButton(text="Xiaomi 15 Pro", callback_data="model_xiaomi_2")],
    [InlineKeyboardButton(text="Xiaomi 15", callback_data="model_xiaomi_3")],
    [InlineKeyboardButton(text="Redmi Note 14 Pro", callback_data="model_xiaomi_4")],
    [InlineKeyboardButton(text="⬅️ Back", callback_data="back")],
])

# PIXEL
pixel_menu = make_menu([
    [InlineKeyboardButton(text="Pixel 10 Pro XL", callback_data="model_pixel_1")],
    [InlineKeyboardButton(text="Pixel 10 Pro", callback_data="model_pixel_2")],
    [InlineKeyboardButton(text="Pixel 10", callback_data="model_pixel_3")],
    [InlineKeyboardButton(text="Pixel 9a", callback_data="model_pixel_4")],
    [InlineKeyboardButton(text="⬅️ Back", callback_data="back")],
])
















































