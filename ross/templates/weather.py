# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # Weather in London
                (r'weather (in|on) (.+)( city| county)?',
                 lambda m: {'type': 'weather',
                            'subtype': 'search',
                            'action': 'request',
                            'query': m.group(2)}),
               )

ru_templates = (
                # Погода в Лондоне
                (r'погода (в|на)( городе)? (.+)е',
                 lambda m: {'type': 'weather',
                            'subtype': 'search',
                            'action': 'request',
                            'query': m.group(3)}),
               )
