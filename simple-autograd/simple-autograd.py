# would be better design-pattern-wise if use subclasses of the Operator class

# but I decide to demonstrate how to abuse lambdas (don't do this though)
ops = {
    'add': (
        lambda a, b, inputs: a.evaluate(inputs) + b.evaluate(inputs),
        lambda a, b, x, inputs: a.grad(x, inputs) + b.grad(x, inputs)
    ),
    'sub': (
        lambda a, b, inputs: a.evaluate(inputs) - b.evaluate(inputs),
        lambda a, b, x, inputs: a.grad(x, inputs) - b.grad(x, inputs)
    ),
    'mul': (
        lambda a, b, inputs: a.evaluate(inputs) * b.evaluate(inputs),
        lambda a, b, x, inputs: a.grad(x, inputs) * b.evaluate(inputs) + \
            a.evaluate(inputs) * b.grad(x, inputs)
    ),
    'div': (
        lambda a, b, inputs: a.evaluate(inputs) / b.evaluate(inputs),
        lambda a, b, x, inputs: (a.grad(x, inputs) * b.evaluate(inputs) - \
            a.evaluate(inputs) * b.grad(x, inputs)) / (b.evaluate(inputs) ** 2)
    ),
    'pow': (
        lambda a, b, inputs: a.evaluate(inputs) ** b.evaluate(inputs),
        lambda a, b, x, inputs: b.evaluate(inputs) * (a.evaluate(inputs) ** \
            (b.evaluate(inputs) - 1)) * a.grad(x, inputs)
    )
}


class Node:

    def evaluate(self, inputs):
        raise NotImplementedError

    def grad(self, respect_to, inputs):
        raise NotImplementedError

    def __add__(self, other):
        return Operator(self, other, ops['add'])

    def __sub__(self, other):
        return Operator(self, other, ops['sub'])

    def __mul__(self, other):
        return Operator(self, other, ops['mul'])

    def __truediv__(self, other):
        return Operator(self, other, ops['div'])

    def __pow__(self, other):
        return Operator(self, other, ops['pow'])


class Operator(Node):

    def __init__(self, a, b, funcs):
        self.a = a
        self.b = b
        self.funcs = funcs # funcs: tuple(eval_func, derivative_func)

    def evaluate(self, inputs):
        return self.funcs[0](self.a, self.b, inputs)

    def grad(self, respect_to, inputs):
        return self.funcs[1](self.a, self.b, respect_to, inputs)

    def __repr__(self):
        return f'(Operator {self.a} {self.b})'


class Variable(Node):

    def __init__(self, name):
        self.name = name

    def evaluate(self, inputs):
        if not self.name in inputs:
            raise ValueError(f'Input does not contain a value for {self.name}')

        return inputs[self.name]

    def grad(self, respect_to, inputs):
        if self.name == respect_to:
            return 1

        return 0

    def __repr__(self):
        return f'(Variable {self.name})'


class Constant(Node):

    def __init__(self, value):
        self.value = value

    def evaluate(self, inputs):
        return self.value

    def grad(self, respect_to, inputs):
        return 0

    def __repr__(self):
        return f'(Constant {self.value})'