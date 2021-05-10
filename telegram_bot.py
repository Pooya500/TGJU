from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, \
    CallbackQueryHandler, ConversationHandler
from telegram.error import BadRequest
from nice import PriceCollector
from telegram import constants, ParseMode

gold18 = []

started_users = []
started_users_gold18 = []
started_users_goldcoin = []
started_users_currency = []
started_users_cryptocurrency = []

admin_id = "ADMIN ID"

ONE, TWO, THREE, FOUR, FIVE, SIX = range(6)


def sender(text, update: Update):
    query = update.callback_query
    try:
        update.message.reply_text(text, parse_mode=ParseMode.HTML)

    except BadRequest:
        parts = []
        while len(text) > 0:
            part = text[:constants.MAX_MESSAGE_LENGTH]
            first_lnbr = part.rfind('\n')
            if first_lnbr != -1:
                parts.append(part[:first_lnbr])
                text = text[(first_lnbr + 1):]
            else:
                parts.append(part)
                text = text[constants.MAX_MESSAGE_LENGTH:]

        for part in parts:
            update.message.reply_text(part, parse_mode=ParseMode.HTML)


class MainApp:
    def __init__(self):
        self.prices = PriceCollector()
        self.main()

    def start_command(self, update: Update, context: CallbackContext):
        user_id = update.message.from_user.id
        if user_id not in started_users:
            started_users.append(update.message.from_user.id)
            context.bot.send_message(chat_id=admin_id, text=f"{user_id} started")
        else:
            context.bot.send_message(chat_id=admin_id, text=f"{user_id} started again")

        keyboard = [
            ['طلا', "سکه"],
            ["ارز", "کریپتوکارنسی"],
        ]
        update.message.reply_text(text='گزینه مورد نظر خود را انتخاب کنید : ',
                                  reply_markup=ReplyKeyboardMarkup(keyboard,
                                                                   resize_keyboard=True))

    def golds_command(self, update: Update, context: CallbackContext):
        user_id_gold18 = update.message.from_user.id
        if user_id_gold18 not in started_users_gold18:
            started_users_gold18.append(update.message.from_user.id)
            context.bot.send_message(chat_id=admin_id, text=f"{user_id_gold18} was looking for gold")
        else:
            context.bot.send_message(chat_id=admin_id, text=f"{user_id_gold18} was looking for gold again")

        if len(self.prices.gold_18_price) == 0:
            self.prices.gold_collector()
        else:
            pass

        text = ""
        text = text + f"انس طلا : {self.prices.goldons_price} دلار \n" + f"طلای ۱۸ عیار : {self.prices.gold_18_price} ریال \n" + f"مثقال طلا : {self.prices.goldmesghal_price} ریال "

        sender(text, update)

    def goldcoin_command(self, update: Update, context: CallbackContext):
        user_id_goldcoin = update.message.from_user.id
        if user_id_goldcoin not in started_users_goldcoin:
            started_users_goldcoin.append(update.message.from_user.id)
            context.bot.send_message(chat_id=admin_id, text=f"{user_id_goldcoin} was looking for gold coins")
        else:
            context.bot.send_message(chat_id=admin_id, text=f"{user_id_goldcoin} was looking for gold coins again")
        if len(self.prices.coin_price) == 0:
            self.prices.coin_collector()
        else:
            pass

        text = ""
        text = text + f"سکه امامی : {self.prices.coin_price} ریال \n" + f"سکه بهار آزادی : {self.prices.coinb_price} ریال \n" + f"سکه نیم بها : {self.prices.coinnim_price} ریال \n"  f"ربع سکه : {self.prices.coinrob_price} ریال \n" + f"سکه یک گرمی : {self.prices.coingerami_price} ریال \n"

        sender(text, update)

    def currency_command(self, update: Update, context: CallbackContext):
        user_id_currency = update.message.from_user.id
        if user_id_currency not in started_users_currency:
            started_users_currency.append(update.message.from_user.id)
            context.bot.send_message(chat_id=admin_id, text=f"{user_id_currency} was looking for currencies")
        else:
            context.bot.send_message(chat_id=admin_id, text=f"{user_id_currency} was looking for currencies again")
        if len(self.prices.dollar_price) == 0:
            self.prices.currency_collector()
        else:
            pass

        text = ''
        text = text + f"🇺🇸 دلار آمریکا: {self.prices.dollar_price} ریال\n" \
                      f"🇪🇺 یورو: {self.prices.euro_price} ریال\n" \
                      f"🇬🇧 پوند انگلیس: {self.prices.pound_price} ریال\n" \
                      f"🇹🇷 لیر ترکیه: {self.prices.lira_price} ریال\n" \
                      f"🇦🇪 درهم امارات: {self.prices.derham_price} ریال\n"
        sender(text, update)

    def cryptocurrency_command(self, update: Update, context: CallbackContext):
        user_id_cryptocurrency = update.message.from_user.id
        if user_id_cryptocurrency not in started_users_cryptocurrency:
            started_users_currency.append(update.message.from_user.id)
            context.bot.send_message(chat_id=admin_id, text=f"{user_id_cryptocurrency} was looking for cyptocurrencies")
        else:
            context.bot.send_message(chat_id=admin_id,
                                     text=f"{user_id_cryptocurrency} was looking for cryptocurrencies again")

        # if len(dollar_price) == 0:
        #     dollar_price
        # else:
        #     pass

        text = ''
        text = text + f"بزودی..."
        sender(text, update)

    def main(self):
        # Nerkh
        # updater = Updater("TOKEN")
        # Testing
        updater = Updater("TOKEN")
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.start_command))
        dispatcher.add_handler(CommandHandler("gold", self.golds_command))
        # dispatcher.add_handler(CommandHandler("asus", self.asus_command))
        # dispatcher.add_handler(CommandHandler("acer", self.acer_command))
        dispatcher.add_handler(MessageHandler(Filters.regex("طلا"), self.golds_command))
        dispatcher.add_handler(MessageHandler(Filters.regex("سکه"), self.goldcoin_command))
        dispatcher.add_handler(MessageHandler(Filters.regex("ارز"), self.currency_command))
        dispatcher.add_handler(MessageHandler(Filters.regex("کریپتوکارنسی"), self.cryptocurrency_command))
        # dispatcher.add_handler(MessageHandler(Filters.regex("HP"), self.hp_command))
        # dispatcher.add_handler(MessageHandler(Filters.regex("Surface"), self.surface_command))
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    MainApp()
