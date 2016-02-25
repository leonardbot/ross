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
               )
