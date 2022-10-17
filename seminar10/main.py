import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Updater, CallbackContext, \
    CallbackQueryHandler
from logger import log_info


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f'Hello {update.effective_user.first_name}. '
        f'To work with rational numbers use /ratio command. '
        f'To work with complex numbers use /complex command.')


async def ratio(update: Update, context: CallbackContext):
    button_r_sum = telegram.InlineKeyboardButton('Сложение', callback_data='button_r_sum')
    button_r_diff = telegram.InlineKeyboardButton('Вычитание', callback_data='button_r_diff')
    button_r_mult = telegram.InlineKeyboardButton('Умножение', callback_data='button_r_mult')
    button_r_div = telegram.InlineKeyboardButton('Деление', callback_data='button_r_div')
    markup = telegram.InlineKeyboardMarkup(
        inline_keyboard=[[button_r_sum], [button_r_diff], [button_r_mult], [button_r_div]])
    await update.message.reply_text('Пожалуйста, выберите операцию с рациональными числами:', reply_markup=markup)
    return callback


async def compl(update: Update, context: CallbackContext):
    button_c_sum = telegram.InlineKeyboardButton('Сложение', callback_data='button_c_sum')
    button_c_diff = telegram.InlineKeyboardButton('Вычитание', callback_data='button_c_diff')
    button_c_mult = telegram.InlineKeyboardButton('Умножение', callback_data='button_c_mult')
    button_c_div = telegram.InlineKeyboardButton('Деление', callback_data='button_c_div')
    markup = telegram.InlineKeyboardMarkup(
        inline_keyboard=[[button_c_sum], [button_c_diff], [button_c_mult], [button_c_div]])
    await update.message.reply_text('Пожалуйста, выберите операцию с комплексными числами:', reply_markup=markup)
    return callback


async def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'button_r_sum':
        await query.answer()
        await query.edit_message_text(text='Для сложения рациональных чисел введите \'/sum число число\'')
    elif variant == 'button_r_diff':
        await query.answer()
        await query.edit_message_text(text='Для вычитания рациональных чисел введите \'/diff число число\'')
    elif variant == 'button_r_mult':
        await query.answer()
        await query.edit_message_text(text='Для умножения рациональных чисел введите \'/mult число число\'')
    elif variant == 'button_r_div':
        await query.answer()
        await query.edit_message_text(text='Для делкния рациональных чисел введите \'/div число число\'')
    elif variant == 'button_c_sum':
        await query.answer()
        await query.edit_message_text(text='Для сложения комплексных чисел введите \'/ksum число число\'')
    elif variant == 'button_c_diff':
        await query.answer()
        await query.edit_message_text(text='Для вычитания комплексных чисел введите \'/kdiff число число\'')
    elif variant == 'button_c_mult':
        await query.answer()
        await query.edit_message_text(text='Для умножения комплексных чисел введите \'/kmult число число\'')
    elif variant == 'button_c_div':
        await query.answer()
        await query.edit_message_text(text='Для делкния комплексных чисел введите \'/kdiv число число\'')


async def sum_ratio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = float(data[1])
    b = float(data[2])
    log_info(update.effective_user.first_name, f'Сложение рациональных чисел {a} и {b}')
    await update.message.reply_text(f'{a} + {b} = {a + b}')


async def diff_ratio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = float(data[1])
    b = float(data[2])
    log_info(update.effective_user.first_name, f'Вычитание рациональных чисел {a} и {b}')
    await update.message.reply_text(f'{a} - {b} = {a - b}')


async def mult_ratio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = float(data[1])
    b = float(data[2])
    log_info(update.effective_user.first_name, f'Умножение рациональных чисел {a} и {b}')
    await update.message.reply_text(f'{a} * {b} = {a * b}')


async def div_ratio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = float(data[1])
    b = float(data[2])
    log_info(update.effective_user.first_name, f'Деление рациональных чисел {a} и {b}')
    if b == 0:
        await update.message.reply_text('Деление на 0 недопустимо')
    else:
        await update.message.reply_text(f'{a} / {b} = {a / b}')


async def sum_complex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = complex(data[1])
    b = complex(data[2])
    log_info(update.effective_user.first_name, f'Сложение комплексных чисел {a} и {b}')
    await update.message.reply_text(f'{a} + {b} = {a + b}')


async def diff_complex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = complex(data[1])
    b = complex(data[2])
    log_info(update.effective_user.first_name, f'Вычитание комплексных чисел {a} и {b}')
    await update.message.reply_text(f'{a} - {b} = {a - b}')


async def mult_complex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = complex(data[1])
    b = complex(data[2])
    log_info(update.effective_user.first_name, f'Умножение комплексных чисел {a} и {b}')
    await update.message.reply_text(f'{a} * {b} = {a * b}')


async def div_complex(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text.split()
    a = complex(data[1])
    b = complex(data[2])
    log_info(update.effective_user.first_name, f'Деление комплексных чисел {a} и {b}')
    if b == 0:
        await update.message.reply_text('Деление на 0 недопустимо')
    else:
        await update.message.reply_text(f'{a} / {b} = {a / b}')


app = ApplicationBuilder().token("...").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ratio", ratio))
app.add_handler(CommandHandler("complex", compl))
app.add_handler(CallbackQueryHandler(callback=callback, pattern=None))
app.add_handler(CommandHandler("sum", sum_ratio))
app.add_handler(CommandHandler("diff", diff_ratio))
app.add_handler(CommandHandler("mult", mult_ratio))
app.add_handler(CommandHandler("div", div_ratio))
app.add_handler(CommandHandler("ksum", sum_complex))
app.add_handler(CommandHandler("kdiff", diff_complex))
app.add_handler(CommandHandler("kmult", mult_complex))
app.add_handler(CommandHandler("kdiv", div_complex))

print("server started")
app.run_polling()
