from aiogram import Router, F, types, html
from models import User
from plugins.functions.dashBoard import dashboard
from plugins.functions.onLogin import login

router = Router()

in_process: dict[int, dict] = {}

@router.callback_query(F.data == "btn_login")
async def login_btn(callback: types.CallbackQuery):
    """Callback handler for btn_login"""
    user_id = callback.from_user.id
    if await User.filter(telegram_id=user_id).exists():
        await dashboard(user_id, callback.message)
        await callback.answer()
        return
    in_process[user_id] = {"step": "username"}
    await callback.message.answer(
        text=f"Please enter your {html.bold('username')} to proceed with authentication...",
        parse_mode="html"
    )
    await callback.answer()

@router.message(F.text & ~F.command)
async def handle_text(message: types.Message):
    """callback handler for user login"""
    user_id = message.from_user.id
    text = message.text.strip()
    if user_id not in in_process:
        await message.answer(
            text=f"{html.bold('Invalid command.')} Please use /start to begin.",
            parse_mode="html"
        )
        return
    step = in_process[user_id]["step"]
    if step == "username":
        in_process[user_id]["username"] = text
        in_process[user_id]["step"] = "password"
        await message.answer(
            text=f"Kindly enter your {html.bold('password')} to continue with the authentication process...",
            parse_mode="html"
        )
    elif step == "password":
        username = in_process[user_id]["username"]
        password = text
        msg = await message.answer(
            text="Processing your request...",
            parse_mode="html",
        )
        await login(username, password, message)
        await msg.delete()
        in_process.pop(user_id, None)