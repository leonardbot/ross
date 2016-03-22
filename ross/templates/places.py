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
                (r'(is|are) ?(there)? (.+?) (near there|near|there|not far|about|around)+',
                lambda m: {'type': 'places',
                           'subtype': 'search',
                           'action': 'question',
                           'query': m.group(3)}),
                # What is around there?
                (r'around there',
                lambda m: {'type': 'places',
                           'subtype': 'explore',
                           'action': 'question',
                           'query': None}),
                # Where i can go today?
                (r'(i can|can i|to|can) go',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'question',
                            'query': None}),
                # Cheap places around
                (r'cheap places',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'request',
                            'query': 'cheap'}),
                # Places around
                (r'places',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'request',
                            'query': None}),
               )

ru_templates = (
                # Где здесь ближайший Старбакс?
                (r'где (здесь|тут)( ближайший)? (.+)',
                 lambda m: {'type': 'places',
                            'subtype': 'search',
                            'action': 'question',
                            'query': m.group(3)}),
                # Что есть недалеко отсюда?
                (r'(недалеко|близко) (здесь|отсюда)',
                lambda m: {'type': 'places',
                           'subtype': 'explore',
                           'action': 'question',
                           'query': None}),
                # Куда мне сходить сегодня вечером?
                (r'куда( .+)? (сходить|пойти)',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'question',
                            'query': None}),
                # Хочу сходить в бар
                (r'хочу (сходить в бар|побухать|выпить)',
                 lambda m: {'type': 'places',
                            'subtype': 'search',
                            'action': 'plans',
                            'query': 'бар'}),
                # Дешевые места поблизости
                (r'дешевые места',
                 lambda m: {'type': 'places',
                            'subtype': 'search',
                            'action': 'request',
                            'query': 'дешево'}),
                # Места поблизости
                (r'места',
                 lambda m: {'type': 'places',
                            'subtype': 'explore',
                            'action': 'request',
                            'query': None}),
               )
