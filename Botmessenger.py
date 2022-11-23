import msg_config as cfg
from msgo import msgo

chat_id = cfg.TELEGRAM_CHAT_ID
token = cfg.TELEGRAM_TOKEN
message = 'Hola!'

bot = msgo(
    chat_id,
    token,
    message,
)

bot.telegram_send()