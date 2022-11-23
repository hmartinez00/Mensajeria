import config as cfg
from msgo import envio
import requests

chat_id = cfg.CHAT_ID
token = cfg.TOKEN

message = 'Hola!'
print(message, end='\r')
envio(chat_id, token, message)