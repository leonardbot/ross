# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # Where is starbucks?
                (r'where ?(is|are)? ?(nearest|near)? ?(.+)',
                 lambda m: {'type': 'places',
                            'subtype': 'search',
                            'action': 'question',
                            'query': m.group(3)}),
                # Is there starbucks not far?
                (r'(is|are) ?(there)? (.+?) (near there|near|there|not far|about)+',
                lambda m: {'type': 'places',
                           'subtype': 'search',
                           'action': 'question',
                           'query': m.group(3)}),
                # Where i can go today?
                (r'where (i can|can i|to) go',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'question',
                            'query': None}),
               )

ru_templates = (
                # Где здесь находится ближайший Старбакс?
                (r'где( здесь| тут)? (находится|есть)( ближайший)? (.+)',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'question',
                            'query': m.group(4)}),
                # Куда мне сходить сегодня вечером?
                (r'куда( мне)? сходить',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'question',
                            'query': None}),
                # Хочу сходить в бар
                (r'хочу (сходить в бар|побухать|выпить)',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'question',
                            'query': 'бар'}),
               )
