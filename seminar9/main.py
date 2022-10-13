from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from exchanges import get_exchange
from exchanges import get_currencies


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def ex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'{get_exchange(items[1])}')


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    curs_list_msg = get_currencies()
    msg1 = 'Use command /ex and a currency name.\n'
    msg2 = 'For example: /ex USD.\n'
    msg3 = f'List of available currencies: {get_currencies()}'
    await update.message.reply_text(f'{msg1} {msg2} {msg3}')


app = ApplicationBuilder().token("...").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("ex", ex))

print("server started")
app.run_polling()
