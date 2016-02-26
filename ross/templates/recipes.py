# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # How to cook a cake?
                (r'how ?(to|i can)? cook (.+)',
                 lambda m: {'type': 'recipes',
                            'subtype': 'search',
                            'action': 'question',
                            'query': m.group(2)}),
                # Cook me cake
                (r'cook ?(me)? (.+)',
                 lambda m: {'type': 'recipes',
                            'subtype': 'search',
                            'action': 'request',
                            'query': m.group(2)}),
                # Find me recipe of cake
                (r'((find|search) ?(me)? )?(recipes? of) (.+)',
                 lambda m: {'type': 'recipes',
                            'subtype': 'search',
                            'action': 'question',
                            'query': m.group(5)}),
                # I want cake recipes
                (r'(find|search|i (need|want)) ?(me)? (.+) recipes?',
                 lambda m: {'type': 'recipes',
                            'subtype': 'search',
                            'action': 'question',
                            'query': m.group(4)}),
                # I am planning to cook a cake
                (r'(i |i (am|\'m)? )?(want|need|must|should) ?(to)? cook (.+)',
                 lambda m: {'type': 'recipes',
                            'subtype': 'search',
                            'action': 'plans',
                            'query': m.group(5)}),
                # I will cook a cake
                (r'i((\'m| am) plann?(ing)? to| will) cook (.+)',
                 lambda m: {'type': 'recipes',
                            'subtype': 'search',
                            'action': 'plans',
                            'query': m.group(4)}),
                # Search for cake recipes
                (r'search for (.+) recipes?',
                 lambda m: {'type': 'recipes',
                            'subtype': 'search',
                            'action': 'question',
                            'query': m.group(1)}),
               )
