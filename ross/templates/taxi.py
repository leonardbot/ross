# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # I want to get taxi
                (r'(taxi|uber)',
                 lambda m: {'type': 'taxi',
                            'subtype': 'get',
                            'action': 'request',
                            'query': None}),
               )

ru_templates = (
                # Мне нужно вызвать такси
                (r'(такси|(у|ю)бер)',
                 lambda m: {'type': 'taxi',
                            'subtype': 'get',
                            'action': 'request',
                            'query': None}),
               )
