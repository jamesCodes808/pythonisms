# Pythonisms

Using pythonic methods creates an iterable linked list. 

`__iter__` gives Linked Lists customized ability to:

- be used in `for in` loops
- be used in list comprehension
- convert into a list or other collection type

set up and tests

```
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pytest tests/test_main.py
```