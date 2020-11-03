# curried-interpreter-hard

__Difficulty:__ \* \* \* \* \_

_This is a harder version of [Curried Interpreter (Easy)](/curried-interpreter-easy)._

## Requirements

You are going to make yet another interpreter similar to [Curried Interpreter (Easy)](/curried-interpreter-easy), but with different tokens and syntax (this version is more like a proper interpreted language).

Your goal is to create a programming language with the following tokens:

- `start`: marks the start of a program
- `return_` (`return_ <value>`): marks the end of a program, and returns the given `<value>`
- `let` (`let <var_name> <value>`): sets the variable `<var_name>` to the given `<value>`
- `add` (`add <value> <value>`) returns the sum of the two `<value>`
- `sub` (`sub <value> <value>`) returns the result of the first `<value>` minus the second `<value>`
- `mul` (`mul <value> <value>`) returns the product of the two `<value>`
- `div` (`div <value> <value>`) returns the result of the first `<value>` divided by the second `<value>` (integer division)

Each `<value>` can either be an integer (immediate value), a string (value of the variable), or an operator (`add`, `sub`, etc) (return value of the operator).

Demo:
```
start
let 'my_var' add 5 8
let 'banana' mul 'my_var' 2
return_ 'banana'
```
is equivalent to the Python code:
```python
my_var = 5 + 8
banana = my_var * 2
return banana
```

which returns `26`.

Just like the easier version of this problem, each token is passed in via a function call (with no line break indications):
```python
>>> start(let)('my_var')(add)(5)(8)(let)('banana')(mul)('my_var')(2)(return_)('banana')
26
```

More examples:
```python
>>> start(let)('x')(20)(return_)(sub)(10)('x')
-10
```

```python
>>> start(return_)(mul)(10)(15)
150
```

Your interpreter should also allow nested operators. Since each operator takes in exactly 2 parameters, it is possible to deduce the hierarchy of the nested structure. Operator functions are right associative.

This:
```
add add 5 add 3 2 5
```
has the structure of this:
```
add(add(5, add(3, 2)), 5)
```

__Like the easier version of this problem, please note that custom classes are not allowed in the solution, as Python's \_\_call\_\_ overloading makes this problem too trivial.__ Your solution should use functions and lambdas to achieve this instead.