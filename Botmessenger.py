import msg_config as cfg
from msgo import tg_msgo, ws_msgo

# chat_id = cfg.TELEGRAM_CHAT_ID
# token = cfg.TELEGRAM_TOKEN

message = 'Hola soy Hector y estoy probando la libreria de python pywhatkit para mensajeria'

# telefono = '+584265200611'
telefono = '+584124275798'

# bot = tg_msgo(
#     chat_id,
#     token,
#     message,
# )

# bot.telegram_sender()


bot = ws_msgo(
    telefono,
    message,
)

bot.whatsapp_sender()