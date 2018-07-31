from typing import Union
from itertools import filterfalse
import re

def rgb2hex(r: float, g: float, b: float) -> str:
    return '{0:02x}{1:02x}{2:02x}'.format(int(r), int(g), int(b))

def get_shortified_description(desc: str) -> str:
    def too_short(sentence: str) -> bool:
        return True if len(sentence) < 45 else False

    def too_long(sentence: str) -> bool:
        return True if len(sentence) > 160 else False

    def does_start_with_slash(para: str) -> bool:
        return True if para.startswith('/') else False

    def is_list_item(sentence: str) -> bool:
        regex = re.compile(r'^\w\)|^\d\)')
        return True if re.match(regex, sentence) else False

    paragraphs = desc.split('\n')
    paragraphs = filterfalse(does_start_with_slash, paragraphs)

    for paragraph in paragraphs:
        sentences = paragraph.split('. ')
        sentences = filterfalse(too_short, sentences)
        sentences = filterfalse(too_long, sentences)
        sentences = filterfalse(is_list_item, sentences)
        for sentence in sentences:
            if sentence:
                if not sentence.endswith('.'):
                    sentence = sentence + '.'

                return sentence

    #TODO how to deal with fails?
    return ''


def enchant_description_with_title(desc: str, title: str) -> str:
    common_non_basic_form_sufixes = ('or', 'ar', 'er', 'en', 'an')

    core_title = title
    if title.endswith(common_non_basic_form_sufixes):
        core_title = core_title[:-2]

    if core_title in desc:
        return desc

    return '{0}: {1}'.format(title, desc)
