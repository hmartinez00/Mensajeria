import config as cfg
from msgo import msgo

chat_id = cfg.CHAT_ID
token = cfg.TOKEN
message = 'Hola!'

bot = msgo(
    chat_id,
    token,
    message,
)

# print(message, end='\r')
bot.envio()