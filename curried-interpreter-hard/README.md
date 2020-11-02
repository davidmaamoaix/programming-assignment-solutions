# curried-interpreter-hard

__Difficulty:__ \* \* \* \* \_

_This is a harder version of [Curried Interpreter (Easy)](/curried-interpreter-easy)._

## Requirements

You are going to make yet another interpreter similar to [Curried Interpreter (Easy)](/curried-interpreter-easy), but with different tokens and syntax (this version is more like a proper interpreted language).

The following custom syntax
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

Your goal is to create appropiate definitions for the following tokens so that the above syntax is valid Python:
- `start`:
- `return_` (`return_ <value>`)
- `let` (`let <variable_name> <value>`)
- `add` (`add <value> <value>`)
- `sub` (`sub <value> <value>`)
- `mul` (`mul <value> <value>`)
- `div` (`div <value> <value>`)