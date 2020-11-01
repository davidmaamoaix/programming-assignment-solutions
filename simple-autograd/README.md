# simple-autograd

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
      C   b
     /
    *
   / \
  m   x
```

With this in mind, create a `Variable` and `Constant` class such that they support evaluation and differentiation as illustrated below:
```python
>>> x = Variable(name='x')
>>> m = Variable(name='m')
>>> y = m * x
>>> 
>>> y.evaluate(inputs={'m': 10, 'x': 15}) # calculate the value of y
150
>>>
>>> y.grad(respect_to='x', inputs={'m': 2, 'x': 5}) # calculate the derivative of y in respect to x
2
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

The following operations should be supported:
- Addition(+)
- Subtraction(-)
- Multiplication(*)
- Division(/)
- Power(**)