# -*- coding: utf-8 -*-

"""
@author: Seva Zhidkov
@contact: zhidkovseva@gmail.com
@license: Apache License 2.0
@version: 0.1.1
Copyright (C) 2015
"""

from __future__ import print_function

import os
import os.path
import inspect
import importlib
import re


class Request:
    """
    Result of parsing user's message
    """
    def __init__(self, type=None, subtype=None,
                 action=None, query=None, **kwargs):
        """
        Save result of proccesing message, after matching regex

        :param type: type of user's requests. For example: 'how-to',
                    'defenition', 'events', 'reminders', 'notes',
                    'places', 'cook' etc.
        :param subtype: more information about user's request type.
                        For example, if request_type = 'places',
                        request_subtype may be 'search' or 'recommend'
        :param action: user's point. For example: 'question' (where is moscow),
                       'request' (add car washing to my to-do), 'thanks' (wow,
                       that's cool)
        :param query: user's query in message, for example:
                      'who is taylor swift' => 'taylor swift'
        :param **kwargs: additional variables, request_type-specific
        """
        self.type = type
        self.subtype = subtype
        self.action = action
        self.query = query
        # Set all additional variables as object attributes
        for (attribute, value) in kwargs.items():
            self.__setattr__(attribute, value)

    def __str__(self):
        """
        Represent request as string
        """
        return str(self.__dict__)


def find_templates():
    """
    Load python modules from templates directory and get templates list

    :return: list of tuples (pairs):
             [(compiled regex, lambda regex_match: return message_data)]
    """
    templates = []
    templates_directory = (inspect.getsourcefile(lambda: 0).rstrip('__init__.py') +
                           'templates')
    template_files = os.listdir(templates_directory)
    for template_file in template_files:
        if template_file.startswith('.') or not template_file.endswith('.py'):
            continue
        # Hack for dev development and disutils
        try:
            template_module = importlib.import_module('templates.{}'.format(
               template_file.rstrip('.py')
            ))
        except ImportError:
            template_module = importlib.import_module('ross.templates.{}'.format(
               template_file.rstrip('.py')
            ))
        # Iterate throw items in template.
        # If there are variable ends with 'templates',
        # extend templates list with it.
        for (name, content) in template_module.__dict__.items():
            if name.endswith('templates'):
                for (regex_text, data_func) in content:
                    templates.append((re.compile(regex_text), data_func))
    return templates


def normalize_message(message_text):
    """
    Remove punctuation marks, articles
    and bot appeals (like 'hey bot')

    :param message_text: user's message text
    :return: normalized message text
    """
    for mark in PUNCTUATION_MARKS:
        message_text = message_text.replace(mark, ' ')
    # Add barier elements for not deleting middle of word
    message_text = ' ' + message_text + ' '
    for article in ARTICLES:
        message_text = message_text.replace(article, ' ')
    # Delete extra spaces
    message_text = ' '.join(message_text.split())
    # TODO: Delete bot appeals (like 'hey bot', 'hi', 'bot') if it's not
    #       the only content of message
    return message_text


def process_message(message_text):
    """
    Search matches for message_text in templates and return data about message.
    If there is no template for message: return None

    :param message_text: user's message text
    :return: Result object or None
    """
    message_text = normalize_message(message_text)
    for (regex, data_lambda) in TEMPLATES:
        match = regex.match(message_text, re.IGNORECASE)
        if match:
            result = Request(**data_lambda(match))
            return result

PUNCTUATION_MARKS = ['.', ',', '!', '?', '(', ')']
ARTICLES = [' a ', ' the ']
TEMPLATES = find_templates()

if __name__ == '__main__':
    input_message = input('Enter message: ')
    while input_message:
        print(process_message(input_message))
        input_message = input('Enter message: ')
