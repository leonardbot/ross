# Ross
Python library for processing people requests for bot based on regular expressions

## Install
```
pip3 install ross
```

## Usage
```
>>> import ross
>>> ross.process_message('How to cook a cake?')
{'subtype': 'search', 'action': 'question', 'type': 'recipes', 'query': 'cake'}
>>> ross.process_message('Is there starbucks not far?').query
'starbucks'
```
## Data types

#### Recipes
*subtype*: search/recommend

*query*: name of dish

*action*: question/plan/request

#### Places
*subtype*: search/recommend

*query*: name of place, from cafe name to country name

*action*: question/plan/request

#### Translate

*subtype*: to_another_lang/to_user_lang

*query*: phrase to translate

*language*: if subtype == to_another_lang, language code for translation
