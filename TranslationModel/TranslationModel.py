import requests
import json


class NaverClientKey:
    __client_id = None
    __client_secret = None

    id_label = 'X-Naver-Client-Id'
    secret_label = 'X-Naver-Client-Secret'

    def __init__(self, envFilePath):
        with open(envFilePath, 'r') as f:
            env = json.load(f)
            self.__client_id = env[self.id_label]
            self.__client_secret = env[self.secret_label]

    def key(self):
        return {self.id_label: self.__client_id, self.secret_label: self.__client_secret}


class TranslationModel:
    __url = 'https://openapi.naver.com/v1/papago/n2mt'
    __naver_client_key = None

    """
    ================================================================

    Singleton Pattern
    글로벌하게 접근 가능한 단 한 개의 객체만을 허용하는 패턴

    ================================================================
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(TranslationModel, cls).__new__(cls)
        return cls.instance

    def __init__(self, envFilePath='', source='en', target='ko'):
        self.source = source
        self.target = target
        self.__naver_client_key = NaverClientKey(envFilePath)

    def __headers(self):
        return self.__naver_client_key.key()

    def __data(self, text):
        return {'source': self.source, 'target': self.target, 'text': text}

    def translate(self, text):
        response = requests.post(self.__url, headers=self.__headers(), json=self.__data(text))
        if response.status_code == 200:
            return response.json()['message']['result']['translatedText']
        else:
            raise Exception(f"Status Code Error"
                            f"Status Code: {response.status_code}")

    def setSource(self, source):
        self.source = source

    def setTarget(self, target):
        self.target = target

    def getSource(self):
        return self.source

    def getTarget(self):
        return self.target
