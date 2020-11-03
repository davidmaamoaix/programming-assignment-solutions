def is_operator(value):
    return value in (add, sub, mul, div)


def valid_var(vars, name):
    if name not in vars:
        raise ValueError(f'{value} is not defined')

    return vars[name]


def let(vars):

    def var_name(name):

        def get_value(value):

            if isinstance(value, str):
                value = valid_var(vars, name)

            elif is_operator(value):

                def set_var(result):
                    vars[name] = result

                    def receive(f):
                        return f(vars)

                    return receive

                return value(vars, set_var)

            elif not isinstance(value, int):
                raise ValueError(f'{value} is not a valid value')

            def chain(f):
                vars[name] = value
                return f(vars)

            return chain

        return get_value

    return var_name


def make_op(func):

    def op(vars, callback):

        def first_param(first):

            if isinstance(first, str):
                first = valid_var(vars, first)

            elif is_operator(first):
                return first(vars, first_param)

            elif not isinstance(first, int):
                raise ValueError(f'{first} is not a valid value')

            def second_param(second):
                if isinstance(second, str):
                    second = valid_var(vars, second)

                elif is_operator(second):
                    return second(vars, second_param)

                elif not isinstance(second, int):
                    raise ValueError(f'{second} is not a valid value')

                return callback(func(first, second))

            return second_param

        return first_param

    return op


def return_(vars):

    def get_value(value):
        if isinstance(value, str):
            return valid_var(vars, value)

        elif is_operator(value):
            return value(vars, get_value)

        return value

    return get_value


start = lambda f: f({})
add = make_op(lambda a, b: a + b)
sub = make_op(lambda a, b: a - b)
mul = make_op(lambda a, b: a * b)
div = make_op(lambda a, b: a // b)