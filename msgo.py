import requests
import msg_config as cfg

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

    def telegram_send(self):
        '''
        Enviara el mensaje almacenado en self.message, a traves del bot de telegram.
        '''
        __telegram_url__ = cfg.TELEGRAM_URL

        requests.post(__telegram_url__ + self.__token__ + '/sendMessage',
                data={'chat_id': self.__chat_id__, 'text': self.__message__})