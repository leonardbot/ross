# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # My last notes
                (r'(my )?(last )?notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 10,
                            'query': None}),
                # My last note
                (r'(my )?last note',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None}),
                # Note number #1
                (r'note( number)? (\#)?(\d+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'id': int(m.group(3)),
                            'query': None}),
                # #1 note
                (r'\#?(\d+) note',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'id': int(m.group(1)),
                            'query': None}),
                # I am planning to watch Friends series
                (r'i(\'m| am)? (want|planning)( to)? watch (.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'info',
                            'query': 'Watch {}'.format(
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
                (r'((note|save|remember)|(add|create) note) (to (self|me) |that )?(.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': m.group(6)}),
                # Write I should go to doctor
                (r'write ?(.+)?',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': m.group(1)}),
                # Create new note
                (r'(create )?(new )?note',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': None}),
                # All notes
                (r'(all )?notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'all',
                            'query': None}),
                # View notes
                (r'(view|my) notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 10,
                            'query': None}),
                # View note
                (r'view note',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None}),
                # My last 5 notes
                (r'(my )?(last )?(\d+) notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': int(m.group(3)),
                            'query': None}),
               )

ru_templates = (
                # Заметка номер #1
                (r'заметка( номер)? (\#|№)?(\d+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'id': int(m.group(3)),
                            'query': None}),
                # #1 заметка
                (r'\#?(\d+) заметка',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'id': int(m.group(1)),
                            'query': None}),
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
                # Создай заметку
                (r'(создай|добавь) заметку',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': None}),
                # Запиши
                (r'(запиши|запомни)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': None}),
                # Все заметки
                (r'(все )?заметки',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'all',
                            'query': None}),
                # Посмотреть заметки
                (r'((про|по)?смотреть|мои) заметки',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 10,
                            'query': None}),
                # Просмотреть заметку
                (r'(((про|по)?смотреть|мои) заметки|заметка)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None}),
                # Моя последняя заметка
                (r'(моя )?последняя заметка',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None}),
                # Мои последние 2 заметки
                (r'(мои )?(последние )?(\d+) замет(ок|ки)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': int(m.group(3)),
                            'query': None}),
                # Мои последние заметки
                (r'(мои )?(последние )?заметки',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 10,
                            'query': None}),

               )
