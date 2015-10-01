from typing import get_type_hints

def strict_types(function):
    def type_checker(*args, **kwargs):
        hints = get_type_hints(function)

        all_args = kwargs.copy()
        all_args.update(dict(zip(function.__code__.co_varnames, args)))

        for argument, argument_type in ((i, type(j)) for i, j in all_args.items()):
            if argument in hints:
                if not issubclass(argument_type, hints[argument]):
                    raise TypeError('Type of {} is {} and not {}'.format(argument, argument_type, hints[argument]))

        result = function(*args, **kwargs)

        if 'return' in hints:
            if type(result) != hints['return']:
                raise TypeError('Type of result is {} and not {}'.format(type(result), hints['return']))

        return result

    return type_checker
