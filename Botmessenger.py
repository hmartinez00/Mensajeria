import json
from MessagesKit.msgo import tg_msgo
from datetime import datetime as dt

now = dt.now()

ruta_archivo_json = 'settings.json'

with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)

url = datos_json['telegram']['TELEGRAM_URL']
chat_id = datos_json['telegram']['TELEGRAM_CHAT_ID']
token = datos_json['telegram']['TELEGRAM_TOKEN']



send_pasaje = f'''Date: {now} Hi, 
this is my english homework.'''


bot = tg_msgo(
    url,
    chat_id,
    token,
    send_pasaje,
)

bot.telegram_sender()

# telefono = '+584265200611'
# telefono = '+584124275798'

# bot = ws_msgo(
#     telefono,
#     message,
# )

# bot.whatsapp_sender()


