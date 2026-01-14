from models import User
from aiogram import Router, F, types, html
from plugins.functions.onLogin import loginBtn
from internal import logger

router = Router()

@router.callback_query(F.data == "btn_logout")
async def logout_btn(callback: types.CallbackQuery):
    """Callback handler for btn_logout"""
    if callback.message.chat.type != "private":
        return  # Ignore the command in groups or channels
    msg = await callback.message.answer(
        text="Processing your request...",
        parse_mode="html",
    )
    user_id = callback.from_user.id
    user = await User.get_or_none(telegram_id=user_id)
    if user:
        await user.delete()
        await callback.message.answer(
            text=f"You have successfully {html.bold('logged out!')}",
            reply_markup=loginBtn,
            parse_mode="html",
        )
        logger.info(f"User - {user_id} has been logged out successfully.")
        await msg.delete()
        return
    await callback.message.answer(
        text=f"You must {html.bold('Login')} before attempting to log out!",
        reply_markup=loginBtn,
        parse_mode="html",
    )
    await msg.delete()
    await callback.answer()
