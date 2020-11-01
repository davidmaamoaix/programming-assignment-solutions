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

With this in mind, create a `Variable` and `Constant` class such that they support calculation and differentiation as illustrated below:
```python
>>> x = Variable(name='x')
>>> m = Variable(name='m')
>>> y = m * x
>>> 
>>> y.evaluate(inputs={'m': 10, 'x': 15})
150
>>>
>>> y.grad(respect_to='x', inputs={'m': 2, 'x': 5})
2
```

Chains should also be supported:
```python
>>> a = Variable(name='x')
>>> b = Variable(name='m')
>>> c = Constant(4)
>>> y = (a + b) ** c
>>>
>>> y.grad(respect_to='x', inputs={'x': 3, 'm': 2})
500
```