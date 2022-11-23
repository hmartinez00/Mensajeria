import requests

def envio(__chat_id__, __token__, __message__):
     requests.post('https://api.telegram.org/bot' + __token__ + '/sendMessage',
              data={'chat_id': __chat_id__, 'text': __message__})