# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # Who is Taylor Swift?
                (r'who ?(is|are)? (.+)',
                 lambda m: {'type': 'wikipedia',
                            'subtype': 'summary',
                            'action': 'question',
                            'query': m.group(2)}),
                # What is compiler?
                (r'what ?(is|are)? (.+)',
                 lambda m: {'type': 'wikipedia',
                            'subtype': 'summary',
                            'action': 'question',
                            'query': m.group(2)}),
               )

ru_templates = (
                # Кто такая Taylor Swift?
                (r'кто ?(так(ая|ой|ое|ие))? (.+)',
                 lambda m: {'type': 'wikipedia',
                            'subtype': 'summary',
                            'action': 'question',
                            'query': m.group(3)}),
                # Что такое компилятор?
                (r'что ?(так(ая|ой|ое|ие))? (.+)',
                 lambda m: {'type': 'wikipedia',
                            'subtype': 'summary',
                            'action': 'question',
                            'query': m.group(3)}),
               )
