# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # I am planning to watch Friends series
                (r'i(\'m| am)? (want|planning) to watch (.+) (series|film|movie)$',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'info',
                            'query': 'Watch «{}»'.format(
                                m.group(3).capitalize()
                            ),
                            'movie': m.group(3)}),
                # I parked my car in section A
                (r'(i )?parke?d?( my)? (car|bike|cycle|motocycle) (in|on) (.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'info',
                            'query': 'Parking: {}'.format(m.group(5)),
                            'parking': m.group(5)}),
                # Note that I should do something
                (r'((note|save|remember)|(add|create) note) (to (self|me)|that)? (.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': m.group(6)}),
               )

ru_templates = (
                # Я хочу посмотреть дедпула
                (r'(я )?(хочу|планирую|думаю) посмотреть (.+)а?',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'info',
                            'query': 'Посмотреть «{}»'.format(
                                m.group(3).capitalize()
                            ),
                            'movie': m.group(3)}),
                # Мне посоветовали посмотреть дедпула
                (r'(тут )?(мне )?(посоветовали?|п?о?рекомендовали?) посмотреть (.+)а',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'info',
                            'query': 'Посмотреть «{}»'.format(
                                m.group(4).capitalize()
                            ),
                            'movie': m.group(4)}),
                # Я припарковал машину на тверской
                (r'(я |мы )?(при)?парковал(и|а)? машин(у|ы) (.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'info',
                            'query': 'Парковка: {}'.format(m.group(5)),
                            'parking': m.group(5)}),
                # Запиши, что я должен купить батон
                (r'(запиши|запомни)( что)? (.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': m.group(3)}),
                # Создай заметку о завтрешней презентации
                (r'(создай |добавь )?заметк(а|у) (.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': m.group(3)}),
               )
