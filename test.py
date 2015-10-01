from strict_types import strict_types

@strict_types
def repeat_str(mystr: str, times: int):
    return mystr * times

print(repeat_str('spam', 8))

print(repeat_str('spam', 'eggs'))

