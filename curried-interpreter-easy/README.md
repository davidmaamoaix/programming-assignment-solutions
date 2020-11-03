# curried-interpreter-easy

__Difficulty:__ \* \_ \_ \_ \_

## Background

Consider this syntax:
```python
my_function(arg_1)(arg_2)(arg_3)
```

This is valid Python syntax. `my_function` is a function that takes in a single parameter (`arg_1`) and returns another function, which also takes in a single parameter(`arg_2`) and returns another function, which takes in a single parameter (`arg_3`) and return whatever it returns (an int, a string, or even another function, in which case this chain can go on).

## Requirements

Your goal is to make a stack based programming language in Python with the following functions/tokens:

- `start` - Marks the start of the program.
- `end` - Marks the end of the program, and returns the top element in the stack.
- `push x` - Pushes the integer `x` into the stack.
- `add` - Adds together the top two elements on the stack.
- `sub` - Subtracts the top-most element by the second top-most element on the stack.
- `mul` - Multiplies the top two elements on the stack.
- `div` - Divides (integer division) the top-most element by the second top-most element on the stack.

To illustrate:

```
   start push 5 push 3 add end
 = 8
```

```
   start push 2 push 5 div push 3 push 8 mul mul end
 = 48
```

However, this is not valid Python syntax. We can, however, add parenthesis around each token to make it valid:

```python
start(push)(4)(push)(9)(div)(end)
```

which returns `2` in this case.

This is similar to the syntax mentioned in [Background](#Background).

Your goal is to create appropriate definitions for `start`, `end`, `push`, `add`, `sub`, `mul` and `div` so that the custom language is valid Python syntax, and evaluates to the correct value.

For instance, typing this in a shell should result in:

```python
>>> start(push)(5)(push)(8)(push)(1)(add)(add)(end)
14
```

__Please note that custom classes are not allowed in the solution, as Python's \_\_call\_\_ method makes this problem too trivial.__ Your solution should use functions and lambdas to achieve this instead.

## Notes
- If you haven't played with functional programming before, consider this problem a 2-star.
- Don't worry about division by `0`. There won't be any test cases on that.
- I also published a puzzle version of this problem on Codewars [here](https://www.codewars.com/kata/5f7a715f6c1f810017c3eb07).