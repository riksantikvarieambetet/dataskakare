import shelve

from google.oauth2 import service_account
from google.cloud import translate

class GoogleTranslate:
    def __init__(self, service_account_file, cache=True, target_language=None):
        credentials = service_account.Credentials.from_service_account_file(service_account_file)
        if not target_language:
            target_language = 'en'

        self.client = translate.Client(credentials=credentials, target_language=target_language)
        self.cache = cache
        self.target_language = target_language

    def translate(self, text, source_language=None):
        if self.cache:
            cache = shelve.open('google_translation_{}_cache'.format(self.target_language))

        if self.cache and text in cache:
            response = cache[text]
        else:
            response = self.client.translate(text, source_language=source_language)
            cache[text] = response

        if self.cache:
            cache.close()

        return response
