# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
Copyright (C) 2015
"""

en_templates = (
                # Subcribe to Buzzfeed
                (r'subribe( to| on)? (.+)',
                 lambda m: {'type': 'rss',
                            'subtype': 'subcribe',
                            'action': 'request',
                            'query': m.group(2)}),
               )

ru_templates = (
                # Подписаться на TJ
                (r'подписаться( на)? (.+)',
                 lambda m: {'type': 'rss',
                            'subtype': 'subcribe',
                            'action': 'request',
                            'query': m.group(2)}),
               )
