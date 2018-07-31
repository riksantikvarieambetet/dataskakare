import shelve

from google.oauth2 import service_account
from google.cloud import vision

from .data_transformation import rgb2hex

class GoogleVision:
    def __init__(self, service_account_file, cache=True):
        credentials = service_account.Credentials.from_service_account_file(service_account_file)
        self.client = vision.ImageAnnotatorClient(credentials=credentials)
        self.cache = cache

    def get_colors(self, url):
        colors = []

        if self.cache:
            cache = shelve.open('google_vision_color_cache')

        if self.cache and url in cache:
            response = cache[url]
        else:
            response = self.client.image_properties({
                'source': { 'image_uri': url }
            })
            cache[url] = response

        if self.cache:
            cache.close()

        for rank in response.image_properties_annotation.dominant_colors.colors:
            if rank.score < 0.01:
                continue

            c = {}
            c['score'] = rank.score
            c['hex'] = rgb2hex(rank.color.red, rank.color.green, rank.color.blue)

            colors.append(c)

        return colors

    def is_black_and_white(self, url):

        if self.cache:
            cache = shelve.open('google_vision_labels_cache')

        if self.cache and url in cache:
            response = cache[url]
        else:
            response = self.client.label_detection({
                'source': { 'image_uri': url }
            })
            cache[url] = response

        if self.cache:
            cache.close()

        for label in response.label_annotations:
            if label.description == 'black and white':
                return True

        return False

    def get_labels(self, url):

        if self.cache:
            cache = shelve.open('google_vision_labels_cache')

        if self.cache and url in cache:
            response = cache[url]
        else:
            response = self.client.label_detection({
                'source': { 'image_uri': url }
            })
            cache[url] = response

        if self.cache:
            cache.close()

        labels = list()
        
        for label in response.label_annotations:
            final_label = {}
            final_label['value'] = label.description
            final_label['score'] = label.score

            labels.append(final_label)

        return labels
