# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

LANGUAGE_CODE = {
    'mandarin': 'zh',
    'chinese': 'zh',
    'traditional chinese': 'zh',
    'spanish': 'es',
    'hindi': 'hi',
    'arabic': 'ar',
    'portuguese': 'pt',
    'bengali': 'bn',
    'russian': 'ru',
    'japanese': 'ja',
    'punjabi': 'pa',
    'german': 'de',
    'french': 'fr',
    'korean': 'ko',
    'turkish': 'tr',
    'polish': 'pl',
    'armenian': 'hy'
}

EN_LANGUAGE_LIST = '|'.join(('mandarin', 'chinese', 'traditional chinese',
                             'spanish', 'hindi', 'arabic', 'portuguese',
                             'bengali', 'russian', 'japanese', 'punjabi',
                             'german', 'french', 'korean', 'turkish',
                             'polish', 'armenian'))

en_templates = (
                # Hot to say hello in Russian?
                (r'(how ?t?o? )?say (.+) in ({})'.format(EN_LANGUAGE_LIST),
                 lambda m: {'type': 'translate',
                            'subtype': 'to_another_lang',
                            'action': 'question',
                            'query': m.group(2),
                            'language': LANGUAGE_CODE[m.group(3)]}),
               )
