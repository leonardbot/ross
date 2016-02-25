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
*subtypes*: search/recommend

*query*: name of dish

*action*: question/plan/request

#### Places
*subtypes*: search/recommend

*query*: name of place, from cafe name to country name

*action*: question/plan/request
