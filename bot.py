from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN = "8080099715:AAGSAHS7SBuXKgutDA9P6E9VCmbyaKLhcgg"

async def calculate(update, context):
    text = update.message.text.strip()

    try:
        yen = float(text.replace(",", "."))
        rub = int((yen * 0.58) + 600) // 100 * 100  # целое число

        await update.message.reply_text(str(rub))

    except ValueError:
        await update.message.reply_text("Введите число")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
