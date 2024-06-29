import telebot
import random
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde el archivo .env
load_dotenv()
# Obtener el token del bot
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Lista de chistes cortos
chistes = [
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "¿Por qué estuvo el libro de matemáticas en el hospital? ¡Porque tenía muchos problemas!",
    "¿Qué le dice una iguana a su hermana gemela? Somos iguanitas.",
    "¿Qué hace una impresora en la playa? ¡Saca copias de seguridad!",
    "¿Qué hace una abeja en el cine? ¡Zum-bido!",
    "¿Qué le dice un jardinero a otro jardinero? ¡Estamos en las mismas ramas!",
    "¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!",
    "¿Cómo se llama el campeón de buceo japonés? ¡Tokofondo!",
    "¿Cuál es el colmo de un electricista? ¡Que su esposa le sea infiel con el hijo de un cortocircuito!",
    "¿Por qué los pájaros no usan zapatos? ¡Porque tienen tenis!",
    "¿Qué le dice un árbol a otro? ¡Nos vemos en el bosque!",
    "¿Cómo se dice dios en japonés? ¡Kamisama!",
    "¿Por qué llora el libro de matemáticas? ¡Porque tiene muchos problemas!",
    "¿Qué le dice un huevo a una sartén? ¡Me tienes frito!",
    "¿Cuál es el animal más antiguo? ¡La cebra porque está en blanco y negro!",
    "¿Qué hace un pez en un árbol? ¡Nada, porque los peces no trepan!"
]

# Lista de adivinanzas
adivinanzas = [
    "Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera.",
    "Aunque no hablo, siempre cuento. Sin mí, nunca sabes el monto.",
    "Del cielo bajo, del suelo subo, y en un cofre me encierro.",
    "Dos hermanitos muy unidos que siempre van de la mano. Cuando los quiere el señor, les corta la cabeza, y los manda a freír.",
    "Vuela sin alas, llora sin ojos. Sin boca te habla y sin lengua te nombra.",
    "Un palacio muy plateado, con muchas damas dentro bailando.",
    "Roja por dentro, verde por fuera. Si quieres que te lo diga, espera.",
    "Viste de verde, amarillo y rojo, y en las vacaciones, se transforma en fuego.",
    "Con agujas y sin hilo, viajo por todo el mundo y siempre vuelvo al mismo sitio.",
    "Cuando menos lo piensas, algo suena. Si algo te dice, algo responde."
]


# Creación de los comandos básicos 
@bot.message_handler(commands=['start'])
def send_start(message):
    start_text = """
    ¡Hola! Bienvenido a uno de mis primeros bots de Telegram.
    
    Puedes usar los siguientes comandos conmigo:
    
    /start - Inicia una conversación conmigo
    /help - Obtiene ayuda sobre cómo usar el bot
    /about - Muestra información sobre este bot
    /chiste - Alegra tu día leyendo un chiste
    /adivinanza - Pon a prueba tu mente con una adivinanza
    
    ¡Espero que disfrutes usando este bot!
    """
    bot.reply_to(message, start_text)


@bot.message_handler(commands=['help']) 
def send_help(message):
    bot.reply_to(message, "¡Claro! Estoy aquí para ayudarte. Si tienes alguna pregunta o necesitas asistencia, no dudes en decírmelo. Estoy aquí para hacer que tu experiencia con este bot sea lo más fácil y agradable posible.")


@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
    ¡Hola! Soy un bot de Telegram creado por EduardoHernandezGuzman para ayudarte en tus tareas diarias.
    
    Este bot fue creado como parte de mi primer proyecto de desarrollo de un bot de Telegram.
    """
    bot.reply_to(message, about_text)

@bot.message_handler(commands=['chiste'])
def send_random_joke(message):
    random_joke = random.choice(chistes)
    bot.reply_to(message, random_joke)

@bot.message_handler(commands=['adivinanza'])
def send_random_riddle(message):
    random_riddle = random.choice(adivinanzas)
    bot.reply_to(message, random_riddle)


if __name__ == "__main__":
    bot.polling(none_stop=True)