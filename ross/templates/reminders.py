# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # Timer for 15 minutes
                (r'timer (for |on )?(\d+) min(utes?)?',
                 lambda m: {'type': 'reminders',
                            'subtype': 'create',
                            'action': 'request',
                            'time_after': int(m.group(2)) * 60,
                            'query': 'Timer!'}),
                # Remind me go to the theater
                (r'remind( me)? (.+)',
                 lambda m: {'type': 'reminders',
                            'subtype': 'create',
                            'action': 'request',
                            'time_in': 'tomorrow',
                            'query': m.group(2)}),
               )

ru_templates = (
                # Таймер на 15 минут
                (r'таймер (на )?(\d+) м(инут(ы|а)?)?',
                 lambda m: {'type': 'reminders',
                            'subtype': 'create',
                            'action': 'request',
                            'time_after': int(m.group(2)) * 60,
                            'query': 'Таймер'}),
                # Напомни мне погулять с собакой
                (r'напомни( мне)? (.+)',
                 lambda m: {'type': 'reminders',
                            'subtype': 'create',
                            'action': 'request',
                            'time_in': 'tomorrow',
                            'query': m.group(2)}),
               )
