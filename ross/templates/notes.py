# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # write note
                (r'(note|mark|write)( note)?$,
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': None}),
                # note that I will speak at the conference
                (r'(note|mark|write)( note)?.?(that|about)?.?(\W+.+|\w+.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': str(m.group(3)}),
                # new note about geography lecture
                (r'(new)?.?note (about)?.?(\W+.+|\w+.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': str(m.group(2)}),
                # show all notes
                (r'(show|display) (my|all|all my)?.?notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'all',
                            'query': None}),
                # show my last 5 notes
                (r'(show|display) (my)?.?last (\d+) notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': int(m.group(3)),
                            'query': None}),
                # show first 2 notes
                (r'(show|display) (my)?.?first (\d+) notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'first',
                            'number': int(m.group(3)),
                            'query': None}),         
                # show note number 10
                (r'(show|display) (my)?.?note (#|№|number)?.?(\d+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'id': int(m.group(4)),
                            'query': None}),
                # show new note
                (r'(show|display) (my)?.?(last|new) note',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None}),
                # delete all my notes
                (r'delete (my|all|all my)?.?notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'all',
                            'query': None}),
                # delete last 20 notes
                (r'delete (my)?.?last (\d+) notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'last',
                            'number': int(m.group(2)),
                            'query': None}),
                # delete my first 5 notes
                (r'delete (my)?.?first (\d+) notes',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'first',
                            'number': int(m.group(2)),
                            'query': None}),
                # delete note #1
                (r'delete (my)?.?note (#|№|number)?.?(\d+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'position': int(m.group(3)),
                            'query': None}),
                # delete my last note
                (r'delete (my)?.?(last|new) note',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None})
               )

ru_templates = (
                # сделай заметку
                (r'(создай|запиши|сделай)( заметку)?$,
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': None}),
                # запиши что мне завтра выступать на конференции
                (r'(создай|запиши|сделай)( заметку)?.?(что|про|о|об)?.?(\W+.+|\w+.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': str(m.group(4)}),
                # новая заметка про лекцию по географии
                (r'(новая)?.?заметка (про|о|об)?.?(\W+.+|\w+.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': str(m.group(3)}),
                # покажи все заметки
                (r'(покажи|отобрази) (мои|все|все мои)?.?заметки',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'all',
                            'query': None}),
                # отобрази мои последние 5 заметок
                (r'(покажи|отобрази) (мои)?.?последние (\d+) замет(ок|ки)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': int(m.group(3)),
                            'query': None}),
                # покажи первые 2 заметки
                (r'(покажи|отобрази) (мои)?.?первые (\d+) замет(ок|ки)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'first',
                            'number': int(m.group(3)),
                            'query': None}),         
                # отобрази заметку номер 10
                (r'(покажи|отобрази) (мою)?.?заметку (#|№|номер)?.?(\d+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'id': int(m.group(4)),
                            'query': None}),
                # покажи мою новую заметку
                (r'(покажи|отобрази) (мою)?.?(последнюю|новую) заметку',
                 lambda m: {'type': 'notes',
                            'subtype': 'view',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None}),
                # удали все мои заметки
                (r'удали (мои|все|все мои)?.?заметки',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'all',
                            'query': None}),
                # удали последние 20 заметок
                (r'удали (мои)?.?последние (\d+) замет(ок|ки)',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'last',
                            'number': int(m.group(2)),
                            'query': None}),
                # удали мои первые 5 заметок
                (r'удали (мои)?.?первые (\d+) замет(ок|ки)',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'first',
                            'number': int(m.group(2)),
                            'query': None}),
                # удали заметку #1
                (r'удали (мою)?.?заметку (#|№|номер)?.?(\d+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'id',
                            'number': 1,
                            'position': int(m.group(3)),
                            'query': None}),
                # удали мою последнюю заметку
                (r'удали (мою)?.?(последнюю|новую) заметку',
                 lambda m: {'type': 'notes',
                            'subtype': 'delete',
                            'action': 'request',
                            'position': 'last',
                            'number': 1,
                            'query': None})
               )
