from aiogram import types
from aiogram import Router, html, F
from plugins.notify import in_bcast
from plugins.callbacks.btnLogin import in_process
from plugins.functions.onLogin import login
from plugins.functions.sendEmail import sendmail

router = Router()

@router.message(F.text & ~F.command)
async def handle_text(message: types.Message):
    """callback handler for text inputs"""
    if message.chat.type != "private":
        return  # Ignore the command in groups or channels
    user_id = message.from_user.id
    text = message.text.strip()
    if user_id in in_process:
        step = in_process[user_id]["step"]
        if step == "username":
            in_process[user_id]["username"] = text
            in_process[user_id]["step"] = "password"
            await message.answer(
                text=f"Kindly enter your {html.bold('password')} to continue with the authentication process:",
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
    if user_id in in_bcast:
        step = in_bcast[user_id]["step"]
        if step == "subject":
            in_bcast[user_id]["subject"] = text
            in_bcast[user_id]["step"] = "mail"
            await message.answer(
                text=f"Now, enter the mail {html.bold('message')} to be broadcast:",
                parse_mode="html"
            )
        elif step == "mail":
            subject = in_bcast[user_id]["subject"]
            mail = text
            await sendmail(subject, mail, message)
            in_bcast.pop(user_id, None)