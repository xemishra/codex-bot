from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from models import User
from aiogram import html

async def dashboard(user_id, message):
    student = await User.get_or_none(telegram_id=user_id)
    student_name = student.student_name
    roll_number = student.roll_number
    branch = student.branch
    session = student.session
    created_at = student.created_at
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Resources', callback_data='btn_resources'),
                InlineKeyboardButton(text='Jobs', callback_data='btn_jobs'),
            ],
            [
                InlineKeyboardButton(text='Project Idea', callback_data='btn_project_idea'),
                InlineKeyboardButton(text='Start-Ups', callback_data='btn_startup'),
            ],
            [
                InlineKeyboardButton(text='Weekly Tests', callback_data='btn_weekly_tests'),
            ],
            [
                InlineKeyboardButton(text='Logout', callback_data='btn_logout'),
            ]
        ]
    )
    await message.reply(
        text=f"""
Hey, {student_name}

Welcome to your dashboard!

{html.bold("Profile:")}
Roll Number: {roll_number}
Branch: {branch}
Session: {session}
Profile Created On: {created_at}

Manage your activities and stay connected with the club effortlessly.
        """,
        reply_markup=btn,
        parse_mode="html",
        disable_web_page_preview=True,
    )
