import telebot
import time

TOKEN = 8505121686:AAFfTD5pMiU7SiVH4joZa6k_vbWtH46w67o

bot = telebot.TeleBot(TOKEN)

# Mensagem inicial
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Envie a prova de pagamento que eu libero o acesso manualmente.")

# Comando para você liberar vídeos manualmente
@bot.message_handler(commands=['liberar'])
def liberar_acesso(message):
    bot.reply_to(message, "Acesso liberado! (isso é só um comando de exemplo)")

# Bot rodando
while True:
    try:
        bot.polling(none_stop=True)
    except Exception:
        time.sleep(5)
