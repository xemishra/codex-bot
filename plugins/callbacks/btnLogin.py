from aiogram import types, html, Router, F
from models import User
from plugins.functions.dashBoard import dashboard

in_process = {}

router = Router()

@router.callback_query(F.data == "btn_login")
async def login_btn(callback: types.CallbackQuery):
    user_id = callback.message.from_user.id
    student = await User.filter(telegram_id=user_id).exists()
    if student:
        await dashboard(callback.message)
        return
    in_process[user_id] = {'step': 'username'}
    await callback.message.answer(
        text=f"Please enter your {html.bold("username")} to proceed with **ERP** authentication...",
        parse_mode='html'
    )