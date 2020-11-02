# simple-autograd

__Difficulty:__ \* \* \_ \_ \_

Consider this mathematical expression:
```
y = (m * x) + b
```

Its computational graph might look like:
```
        y
        |
        +
       / \
      O   b
     /
    *
   / \
  m   x
```

With this in mind, create a `Variable` and `Constant` class such that they support evaluation and partial differentiation as illustrated below:
```python
>>> x = Variable(name='x')
>>> m = Variable(name='m')
>>> c = Constant('5')
>>>
>>> y = m * x * c
>>>
>>> y.evaluate(inputs={'m': 10, 'x': 15}) # calculate the value of y
750
>>>
>>> y.grad(respect_to='x', inputs={'m': 2, 'x': 5}) # calculate the derivative of y in respect to x
10
```

Chains should also be supported:
```python
>>> a = Variable(name='e')
>>> b = Variable(name='r')
>>> c = Constant(4)
>>> y = (a + b) ** c
>>>
>>> y.grad(respect_to='e', inputs={'e': 3, 'r': 2})
500
```

Here's another example:
```python
>>> x = Variable(name='x')
>>> a = Constant(3) * (x + Constant(5))
>>> b = Constant(8) * (x - Constant(20))
>>> c = a / b
>>>
>>> c.evaluate({'x': 30})
1.3125
>>>
>>> c.grad('x', {'x': 10})
-0.09375
```

The following operations should be supported:
- Addition(+)
- Subtraction(-)
- Multiplication(\*)
- Division(/)
- Power(\*\*)

__Notes:__
- The power term `c` will always be a constant in any `a ^ c` for simplicity
- Constant folding is not required, but encouraged
