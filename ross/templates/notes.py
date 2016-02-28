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
                            'query': 'Watch: «{}»'.format(
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
                (r'((note|save|remember)|add note) (to (self|me)|that)? (.+)',
                 lambda m: {'type': 'notes',
                            'subtype': 'add',
                            'action': 'request',
                            'query': m.group(5)}),
               )
