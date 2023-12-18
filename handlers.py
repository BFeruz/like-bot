from telegram.ext import CallbackContext
from telegram import Update
from keyboards import keyboard, inline_keyboard
from db import (
    is_user,
    add_user,
    get_user,
)


def start(update: Update, context: CallbackContext):
    user = update.effective_user

    if not is_user(chat_id=str(user.id)):
        add_user(chat_id=str(user.id))
        
        update.message.reply_html(
            text=f'Hello, {user.full_name}! Press one of the buttons.',
            reply_markup=keyboard
        )
        update.message.reply_html(
            text=f'Press one of the buttons.',
            reply_markup=inline_keyboard
        )

    user_data = get_user(chat_id=str(user.id))

    update.message.reply_html(
        text=f'<b>likes:</b> {user_data["likes"]}\n<b>dislikes:</b> {user_data["dislikes"]}',
        reply_markup=keyboard
    )
    update.message.reply_html(
        text=f'<b>inline likes:</b> {user_data["inline_likes"]}\n<b>inline dislikes:</b> {user_data["inline_dislikes"]}',
        reply_markup=inline_keyboard
    )

def like(update: Update, context: CallbackContext):

    update.message.reply_html(text=f'likes: {LIKES}\ndislikes: {DISLIKES}')


def dislike(update: Update, context: CallbackContext):

    update.message.reply_html(text=f'likes: {LIKES}\ndislikes: {DISLIKES}')
