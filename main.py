import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.types import CallbackQuery, FSInputFile, Message

from button import (
    menu,
    samsung_menu,
    iphone_menu,
    xiaomi_menu,
    pixel_menu,
)

# Token comes from an environment variable (never hard-code it)
TOKEN = "8425777888:AAGLs-byCn-1PaBqk0l37in3Aac_aTbri0A"
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set!")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()


# MODEL DATA
models = {

    "model_samsung_1": {
        "name": "Samsung Galaxy S25 Ultra",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwjlrKDfooKYAxU3mIMHHVZAHu4YACICCAEQHxoCZWY&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdLhL9GkMfvxM_R7f7ZOIZup0ZqOtJ7imgJf4D0l7DjP1yJq8JrB2vUaAp6qEALw_wcB&ei=fpv1aqrbG-LGzMsPzrHM-QY&cid=CAASuwHkaL-9LQHy6mafo5-DTYMrOwzBFHTvsqlg8rxPlfEsUZiRhkmnu6Nu0WLVsaT4P8FVvk7JBpaevngWckWOVGlIYjVXv5aYjXxH1pGoKKyx0r-xLYrBK8IRmPmfP8sm8cVmm4HhpDDIXfrM-3n5-pS2O37S91BZPZ2Z1foLTWvqu_x5v_1goWXOuKs-RmmADpBaJ9Az-lqlrbkiM9u-IcHBpRmElrS3JvAQez6wZREMg-PilGIoaPzf2iAl&cce=2&category=acrcp_v1_32&sig=AOD64_0tQsmBO3mzRcMFEN3P4dAq5GzHQw&ctype=5&q=&nis=4&sqi=2&ved=2ahUKEwiqkpnfooKYAxViI3MDHc4YM28Q8w4oAHoFCM0BEAE&adurl="
    },

    "model_samsung_2": {
        "name": "Samsung Galaxy S25+",
        "photo": "https://openshop.uz/shop/product/82723-samsung-galaxy-s25-5g-12-256-gb-silver-shadow-kumush-rang-365-gb-internet-3-oy-bepul-tv-com?lang=ru&srsltid=AYCX9vKY9DqVKuYlhvsOzt_CN2vTkuixoCe-wFTsThFCa5zGvgdBWtzR"
    },

    "model_samsung_3": {
        "name": "Samsung Galaxy Z Fold7",
        "photo": "https://www.google.com/imgres?q=samsung%20galaxy%20z%20fold%207&imgurl=https%3A%2F%2Fasset.openshop.uz%2Fuploads%2Fproducts%2Fphotos%2F202603%2FQ7Gslqs2f7grjW5F32LSYKvXiBSHV4Hw.jpg&imgrefurl=https%3A%2F%2Fopenshop.uz%2Fshop%2Fproduct%2F111562-samsung-galaxy-z-fold-7-12-256-gb-blue-shadow-365-gb-internet-3-oy-bepul-tv-com%3Flang%3Dru%26srsltid%3DAYCX9vKltRE6Wf4tRdretGugY1waE07RGBfuxpa78paCzeIUc4ik4r9k&docid=Zd5uKDb9zxfzHM&tbnid=yJLA6AJkb5pkhM&vet=12ahUKEwiZ7MGWo4KYAxVrc7AFHauNPaAQnPAOegQIJxAA..i&w=1000&h=1000&hcb=2&ved=2ahUKEwiZ7MGWo4KYAxVrc7AFHauNPaAQnPAOegQIJxAA"
    },

    "model_samsung_4": {
        "name": "Samsung Galaxy A56",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwi0xcCoo4KYAxXqgoMHHaKpBREYACICCAEQTxoCZWY&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdLZetkTjfoW288pmVmjZdt70xqA1OfLix6t1hgukkruRhefgmRW7kgaAs6HEALw_wcB&cid=CAASuwHkaLPHw9o5BI4HYOJnhAHdQ57o9vVOeuGEQbLp0AyXuMVcMui7-wXVo0AVeZkdlatt5FqNrsIgzzw64QOeVdiJY4wUcCGX9yKKQEWckegasiLnX2evmzXTH8dBZyCgtfRdhXTMi8B6fGi8VqOgcFXvYkniKXIqVu2hrAhVO_2ZMa3_clC0gttccAwvdNipqyFlTia9zsbPnzppSSGC8usqU8DnNbWNr93WeMxL8JQeDgo0kEGtkmtMJ_dM&cce=2&category=acrcp_v1_32&sig=AOD64_1Yj_4u3BSBcLK8y3z0JSVON-GRlQ&ctype=5&q=&nis=4&ved=2ahUKEwiCmLmoo4KYAxU3frAFHQMuKh8Q8w4oAHoFCJwBEAE&adurl="
    },

    "model_iphone_1": {
        "name": "iPhone 17 Pro Max",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwiQnKXKo4KYAxVfk4MHHYwFBUkYACICCAEQTRoCZWY&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdLNGXGN2DVXx8ujeroMYDRlBYt8M9H2wbqocST6ZqL1aa389MpVBH8aAmHlEALw_wcB&cid=CAASuwHkaM6T3cpKWdhxlUcME33rtTSVVBywNHZvvGz6f1ZPEnC14VwrOjl_QKS_liIAwt9qOhdbpREpCmoeFsReUimaLWqL4KOqlM5uJdiQoGOgOcd1EyAzcYvSN9FWTNS4Ont8mNO9PqH8EC7JnV9-SqvhTsoB31pQ6pnsS_mo0njjsVDkF0LrsSS0FzpC1Wm_01KLI5pgffTVZDUY882m9-JWB-KwITKPWo12ZWqxw2-liST-OQHZtkyFTda8&cce=2&category=acrcp_v1_32&sig=AOD64_3wrqkGw_z2l2l4bqT4d8QtDUqdqw&ctype=5&q=&nis=4&ved=2ahUKEwip9p7Ko4KYAxWxd7AFHRRlHfkQ8w4oAHoFCJkBEAE&adurl="
    },

    "model_iphone_2": {
        "name": "iPhone 17 Pro",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwj3xNTXo4KYAxXNkYMHHTgvAPsYACICCAEQTRoCZWY&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJBmVOtpSFk5-734PPXXGQzriBPgFDZ9VqiIosng3Ry3xpiKW41zuQaAsjFEALw_wcB&cid=CAASuwHkaEVT-OTv8x6Cl5Hys3zkqhnDP49aP2gxOPcQMkd_g7d8kTLWqRh9GHvqdU9_YGmjG6DiczdQ-l0I_0B0S3wOcAyfN8akXdVKlNvJOFtHssilGyj9bZx9GqovxNFX4I0ukny95lxIuymvQoJ48hAceo8TgnGQHcvuMr2TcnNLU0dw3TsbLTd1iJzlSIwQqPq9riHlPKBb-n3gLNUh9hQ-Z_LRdma3VEbRmxZ6OhwTeGKn4M3xTE10vaJq&cce=2&category=acrcp_v1_32&sig=AOD64_0eGf0iOFyE0e1xUptIdv-_whpuig&ctype=5&q=&nis=4&ved=2ahUKEwiM6szXo4KYAxVwdrAFHUr6MEwQ8w4oAHoFCIEBEAE&adurl="
    },

    "model_iphone_3": {
        "name": "iPhone 17 Air",
        "photo": "https://ispace.uz/product/iphone-air-512-gb-sky-blue-mg2v4hx-a?srsltid=AYCX9vJFSeUc_CN4FVIfulyoZyHe2rfI_mB_AE0pctI5B6n0n4YfNwmM"
    },

    "model_iphone_4": {
        "name": "iPhone 17",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwi74aDqo4KYAxVCaEECHWECJV0YACICCAEQTRoCd3M&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdLDVTdIRR_jPsAbr6bScUU3-8DXEFmRBLh0_srldSM4HBEkpQT4DWgaAmqQEALw_wcB&cid=CAASuwHkaGgbFg7PiFCOppZTFcRYqLZzmmd9ssylYfyLkUU60pCQuVWhKTDS0peV__L_HmF0jUt_9R16ljunTP7e7VFHKHlyHdqfnviE7K9RjjSUrt3pCwzdiR1k0b_DodE-NQHF_bTlfbS-0aHtlG5SBUuGFYr6rm9JAFuAdBje-caBgpkFsIbASm-6rz0zrpJJp_Ffh1mX7jb4HbCB2iorFOA3fYkX1I7EhqWnHEYmDARDe_MjWWAAd0hHOfKP&cce=2&category=acrcp_v1_32&sig=AOD64_2yKQJBJqo9FwN1QTUJX6mNVJ5ZuQ&ctype=5&q=&nis=4&ved=2ahUKEwix4Zvqo4KYAxWOKvsDHZTUBNAQ8w4oAHoFCIcBEAE&adurl="
    },

    "model_xiaomi_1": {
        "name": "Xiaomi 15 Ultra",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwj2oPz_o4KYAxVzk3wGHVjhJHYYACICCAEQFRoCd3M&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJskmVHX9DuyvKg_wiNu8sESO0whYdczOMAyABwyrMXyoMhBJnobosaAjhxEALw_wcB&cid=CAASuwHkaEKcp-aiZ0H7by8QUkhLMNV8ksHFEonDLKXymsPfOGcbuHsZOf7MhjvFDxqNw_NudxMp7PSx70kCy2HJP_M2MXvGIqvN4LbXj5UoNg5BSDLEUMCRPHpn3GfF94tIjKN8Lti21PLkO41WvJJajC1Y-hxudlj4OgGDS3-kFkoGxM3_jjhJLb0w3Mk2AUtRVJNUKri9ncBHVttVbBVrw1KC-Hntt8rGrlebFRGReNcDOiE3y2jY1XyEIUVy&cce=2&category=acrcp_v1_32&sig=AOD64_1HU9DrLjKeUZMCCnmRhImkVZiF1g&ctype=5&q=&nis=4&ved=2ahUKEwitmPf_o4KYAxWRV6QEHcrrEgMQ8w4oAHoFCIoBEAE&adurl="
    },

    "model_xiaomi_2": {
        "name": "Xiaomi 15 Pro",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwj2oPz_o4KYAxVzk3wGHVjhJHYYACICCAEQFRoCd3M&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJskmVHX9DuyvKg_wiNu8sESO0whYdczOMAyABwyrMXyoMhBJnobosaAjhxEALw_wcB&cid=CAASuwHkaEKcp-aiZ0H7by8QUkhLMNV8ksHFEonDLKXymsPfOGcbuHsZOf7MhjvFDxqNw_NudxMp7PSx70kCy2HJP_M2MXvGIqvN4LbXj5UoNg5BSDLEUMCRPHpn3GfF94tIjKN8Lti21PLkO41WvJJajC1Y-hxudlj4OgGDS3-kFkoGxM3_jjhJLb0w3Mk2AUtRVJNUKri9ncBHVttVbBVrw1KC-Hntt8rGrlebFRGReNcDOiE3y2jY1XyEIUVy&cce=2&category=acrcp_v1_32&sig=AOD64_1HU9DrLjKeUZMCCnmRhImkVZiF1g&ctype=5&q=&nis=4&ved=2ahUKEwitmPf_o4KYAxWRV6QEHcrrEgMQ8w4oAHoFCIoBEAE&adurl="
    },

    "model_xiaomi_3": {
        "name": "Xiaomi 15",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwj2oPz_o4KYAxVzk3wGHVjhJHYYACICCAEQFRoCd3M&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJskmVHX9DuyvKg_wiNu8sESO0whYdczOMAyABwyrMXyoMhBJnobosaAjhxEALw_wcB&cid=CAASuwHkaEKcp-aiZ0H7by8QUkhLMNV8ksHFEonDLKXymsPfOGcbuHsZOf7MhjvFDxqNw_NudxMp7PSx70kCy2HJP_M2MXvGIqvN4LbXj5UoNg5BSDLEUMCRPHpn3GfF94tIjKN8Lti21PLkO41WvJJajC1Y-hxudlj4OgGDS3-kFkoGxM3_jjhJLb0w3Mk2AUtRVJNUKri9ncBHVttVbBVrw1KC-Hntt8rGrlebFRGReNcDOiE3y2jY1XyEIUVy&cce=2&category=acrcp_v1_32&sig=AOD64_1HU9DrLjKeUZMCCnmRhImkVZiF1g&ctype=5&q=&nis=4&ved=2ahUKEwitmPf_o4KYAxWRV6QEHcrrEgMQ8w4oAHoFCIoBEAE&adurl="

    },

    "model_xiaomi_4": {
        "name": "Redmi Note 14 Pro",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwj2oPz_o4KYAxVzk3wGHVjhJHYYACICCAEQFRoCd3M&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJskmVHX9DuyvKg_wiNu8sESO0whYdczOMAyABwyrMXyoMhBJnobosaAjhxEALw_wcB&cid=CAASuwHkaEKcp-aiZ0H7by8QUkhLMNV8ksHFEonDLKXymsPfOGcbuHsZOf7MhjvFDxqNw_NudxMp7PSx70kCy2HJP_M2MXvGIqvN4LbXj5UoNg5BSDLEUMCRPHpn3GfF94tIjKN8Lti21PLkO41WvJJajC1Y-hxudlj4OgGDS3-kFkoGxM3_jjhJLb0w3Mk2AUtRVJNUKri9ncBHVttVbBVrw1KC-Hntt8rGrlebFRGReNcDOiE3y2jY1XyEIUVy&cce=2&category=acrcp_v1_32&sig=AOD64_1HU9DrLjKeUZMCCnmRhImkVZiF1g&ctype=5&q=&nis=4&ved=2ahUKEwitmPf_o4KYAxWRV6QEHcrrEgMQ8w4oAHoFCIoBEAE&adurl="
    },

    "model_pixel_1": {
        "name": "Google Pixel 10 Pro XL",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwj2oPz_o4KYAxVzk3wGHVjhJHYYACICCAEQFRoCd3M&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJskmVHX9DuyvKg_wiNu8sESO0whYdczOMAyABwyrMXyoMhBJnobosaAjhxEALw_wcB&cid=CAASuwHkaEKcp-aiZ0H7by8QUkhLMNV8ksHFEonDLKXymsPfOGcbuHsZOf7MhjvFDxqNw_NudxMp7PSx70kCy2HJP_M2MXvGIqvN4LbXj5UoNg5BSDLEUMCRPHpn3GfF94tIjKN8Lti21PLkO41WvJJajC1Y-hxudlj4OgGDS3-kFkoGxM3_jjhJLb0w3Mk2AUtRVJNUKri9ncBHVttVbBVrw1KC-Hntt8rGrlebFRGReNcDOiE3y2jY1XyEIUVy&cce=2&category=acrcp_v1_32&sig=AOD64_1HU9DrLjKeUZMCCnmRhImkVZiF1g&ctype=5&q=&nis=4&ved=2ahUKEwitmPf_o4KYAxWRV6QEHcrrEgMQ8w4oAHoFCIoBEAE&adurl="
    },

    "model_pixel_2": {
        "name": "Google Pixel 10 Pro",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwj2oPz_o4KYAxVzk3wGHVjhJHYYACICCAEQFRoCd3M&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJskmVHX9DuyvKg_wiNu8sESO0whYdczOMAyABwyrMXyoMhBJnobosaAjhxEALw_wcB&cid=CAASuwHkaEKcp-aiZ0H7by8QUkhLMNV8ksHFEonDLKXymsPfOGcbuHsZOf7MhjvFDxqNw_NudxMp7PSx70kCy2HJP_M2MXvGIqvN4LbXj5UoNg5BSDLEUMCRPHpn3GfF94tIjKN8Lti21PLkO41WvJJajC1Y-hxudlj4OgGDS3-kFkoGxM3_jjhJLb0w3Mk2AUtRVJNUKri9ncBHVttVbBVrw1KC-Hntt8rGrlebFRGReNcDOiE3y2jY1XyEIUVy&cce=2&category=acrcp_v1_32&sig=AOD64_1HU9DrLjKeUZMCCnmRhImkVZiF1g&ctype=5&q=&nis=4&ved=2ahUKEwitmPf_o4KYAxWRV6QEHcrrEgMQ8w4oAHoFCIoBEAE&adurl="
    },

    "model_pixel_3": {
        "name": "Google Pixel 10",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwiKruOipIKYAxX2hv0FHcBgLGQYACICCAEQTRoCd2Y&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJR8oCdPaOpG4EgKRCwhpYeBXq2OMlkvqm6ZEkybi6yZD1F586EwzYaArEpEALw_wcB&cid=CAASuwHkaOIfp1AmckUxX9CfkgIm2Nsh5bF2iFjGwczJ5LsWxCPBernCUqX9wN65x5f3VgkbqW-EYZmOUtMNr7osB__E1uirD3uptFQl_qnXIfNsKdG_JPrRjnx8t4zNDlRUvuJLOMzBiFc2cYQ5OY4eAAzdvQEj97yZPiT4cgpeBSUp58beXKIjHO2I4kOmrSU02AJ2o6u3EH0QTy0NMAMxVo08xGhvegOfMJaXU9Dd4yRjrvWaGPpdZT-AO9iW&cce=2&category=acrcp_v1_32&sig=AOD64_3eohFjsuMbKjg6Be_5_4LLxNTRtA&ctype=5&q=&nis=4&ved=2ahUKEwiBl9uipIKYAxU9brAFHaRLAGgQ8w4oAHoFCNgBEAE&adurl="
    },

    "model_pixel_4": {
        "name": "Google Pixel 9a",
        "photo": "https://www.google.com/aclk?sa=L&ai=DChsSEwiKruOipIKYAxX2hv0FHcBgLGQYACICCAEQTRoCd2Y&co=1&ase=2&gclid=Cj0KCQiA5NXXBhDEARIsABAJhdJR8oCdPaOpG4EgKRCwhpYeBXq2OMlkvqm6ZEkybi6yZD1F586EwzYaArEpEALw_wcB&cid=CAASuwHkaOIfp1AmckUxX9CfkgIm2Nsh5bF2iFjGwczJ5LsWxCPBernCUqX9wN65x5f3VgkbqW-EYZmOUtMNr7osB__E1uirD3uptFQl_qnXIfNsKdG_JPrRjnx8t4zNDlRUvuJLOMzBiFc2cYQ5OY4eAAzdvQEj97yZPiT4cgpeBSUp58beXKIjHO2I4kOmrSU02AJ2o6u3EH0QTy0NMAMxVo08xGhvegOfMJaXU9Dd4yRjrvWaGPpdZT-AO9iW&cce=2&category=acrcp_v1_32&sig=AOD64_3eohFjsuMbKjg6Be_5_4LLxNTRtA&ctype=5&q=&nis=4&ved=2ahUKEwiBl9uipIKYAxU9brAFHaRLAGgQ8w4oAHoFCNgBEAE&adurl="
    }
}


# START
@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "📱 <b>SMARTPHONE STORE</b>\n\n"
        "Welcome! Choose your favourite brand:",
        reply_markup=menu,
    )


# BRAND BUTTONS
@dp.callback_query(F.data == "brand_samsung")
async def samsung(call: CallbackQuery):
    await call.message.edit_text(
        "📱 <b>Samsung Models</b>\n\nChoose your smartphone:",
        reply_markup=samsung_menu,
    )
    await call.answer()


@dp.callback_query(F.data == "brand_iphone")
async def iphone(call: CallbackQuery):
    await call.message.edit_text(
        "🍎 <b>iPhone Models</b>\n\nChoose your smartphone:",
        reply_markup=iphone_menu,
    )
    await call.answer()


@dp.callback_query(F.data == "brand_xiaomi")
async def xiaomi(call: CallbackQuery):
    await call.message.edit_text(
        "📱 <b>Xiaomi Models</b>\n\nChoose your smartphone:",
        reply_markup=xiaomi_menu,
    )
    await call.answer()


@dp.callback_query(F.data == "brand_pixel")
async def pixel(call: CallbackQuery):
    await call.message.edit_text(
        "✨ <b>Google Pixel Models</b>\n\nChoose your smartphone:",
        reply_markup=pixel_menu,
    )
    await call.answer()


# BACK BUTTON
@dp.callback_query(F.data == "back")
async def back(call: CallbackQuery):
    # If the current message is a photo, it can't be edited into text,
    # so send a fresh menu instead.
    try:
        await call.message.edit_text(
            "📱 <b>SMARTPHONE STORE</b>\n\nChoose your favourite brand:",
            reply_markup=menu,
        )
    except TelegramBadRequest:
        await call.message.answer(
            "📱 <b>SMARTPHONE STORE</b>\n\nChoose your favourite brand:",
            reply_markup=menu,
        )
    await call.answer()


# MODEL BUTTONS
@dp.callback_query(F.data.startswith("model_"))
async def show_model(call: CallbackQuery):
    model = models.get(call.data)

    if model is None:
        await call.answer("Model not found!", show_alert=True)
        return

    await call.answer()

    caption = f"📱 <b>{model['name']}</b>"
    photo_src = model["photo"]

    try:
        if photo_src.startswith(("http://", "https://")):
            photo = photo_src  # direct image URL
        else:
            if not os.path.isfile(photo_src):
                raise FileNotFoundError(photo_src)
            photo = FSInputFile(photo_src)  # local file

        await call.message.answer_photo(photo=photo, caption=caption)

    except (FileNotFoundError, TelegramBadRequest):
        await call.message.answer(
            f"📷 Photo for <b>{model['name']}</b> has not been added yet."
        )


# RUN BOT
async def main():
    print("1. Starting bot...", flush=True)

    try:
        await bot.get_me()
        print("2. Telegram connection successful! ✅", flush=True)
        await dp.start_polling(bot)

    except Exception as e:
        print(f"BOT ERROR: {e!r}", flush=True)
        raise

    finally:
        await bot.session.close()


if __name__ == "__main__":
    print("3. Running Python...", flush=True)
    asyncio.run(main())






























































