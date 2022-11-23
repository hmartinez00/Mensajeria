import requests
import pywhatkit
import msg_config as cfg
from datetime import datetime, timedelta


class tg_msgo:

    def __init__(
            self,
            __chat_id__,
            __token__,
            __message__,
        ):

        self.__chat_id__ = __chat_id__
        self.__token__ = __token__
        self.__message__ = __message__

    def telegram_sender(self):
        '''
        Enviara el mensaje almacenado en self.message, a traves del bot de telegram.
        '''
        __telegram_url__ = cfg.TELEGRAM_URL

        requests.post(__telegram_url__ + self.__token__ + '/sendMessage',
                data={'chat_id': self.__chat_id__, 'text': self.__message__})

class ws_msgo:


    def __init__(
            self,
            __phone__,
            __message__,
        ):

        ahora = datetime.now()
        delay = ahora + timedelta(minutes=1)
    
        self.__phone__ = __phone__
        self.__message__ = __message__
        self.hour = delay.hour
        self.min = delay.minute

    
    def whatsapp_send(self):
        '''
        Enviara el mensaje almacenado en self.message, al minuto siguiente del envio a traves de una api de whatsapp.
        '''

        pywhatkit.sendwhatmsg(
                self.__phone__, 
                self.__message__, 
                self.hour, 
                self.min
            )