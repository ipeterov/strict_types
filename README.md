# strict_types
This is `strict_types` lib (which consists mostly of one decorator) I created for python that implements strict typing using type-hints. It works only with python 3.5 for now, though I think it's pssible to make it work with any version of python using function annotations syntax.

## Installation
You can try installing it via pip (that doesn't work for my ubuntu machine)
```
pip3 install git+git://github.com/ipeterov/strict_types@maste
```
or by downloading .tar.gz file, unpacking it and running
```
python3 setup.py install
```
in the folder that was created after unpacking. This is not the best option, but it works on all my machines.

## Usage
You can import it
```python
from strict_types import strict_types
```
then use it as a decorator
```python
@strict_types
def repeat_str(mystr: str, times: int):
    return mystr * times
```
and it will raise a `TypeError` if something of the wrong type is passed to the function e.g. `repeat_str('spam', 'eggs)'`
```
Traceback (most recent call last):
  File "strict_types.py", line 29, in <module>
    repeat_str('spam', 'eggs')
  File "strict_types.py", line 13, in type_checker
    raise TypeError('Type of {} is {} and not {}'.format(argument, argument_type, hints[argument]))
TypeError: Type of times is <class 'str'> and not <class 'int'>

```

## Using [abc](https://docs.python.org/3/library/abc.html) (abstract base classes)
Though it is possible to use it to restrict functions input to only one type, e.g.
```python
@strict_types.strict_types
def repeat_str(mystr: str, times: int):
    return mystr * times
```
the recommended way to use it is with abstract base classes
```python
from numbers import Number # a hierarchy of numeric abstract base classes.
def mutiply(a: Number, b: Number):
    return a * b
```
This function will accept `float`, `int`, `real`, or any kind of number, but will raise an exception if something different (like `function`, `list` or `string`) is passed to it.
