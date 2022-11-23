import requests

class msgo:

    def __init__(
            self,
            __chat_id__,
            __token__,
            __message__,
        ):

        self.__chat_id__ = __chat_id__
        self.__token__ = __token__
        self.__message__ = __message__

    def envio(self):
        requests.post('https://api.telegram.org/bot' + self.__token__ + '/sendMessage',
                data={'chat_id': self.__chat_id__, 'text': self.__message__})