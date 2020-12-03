# brainfuck-interpreter

__Difficulty:__ \* \* \_ \_ \_

## Requirements
Your goal is to write an interpreter for the BrainFuck esoteric language in __one line__ (no semicolon).

Return a string of the output of the given program with the given input.
```python
def brainfuck(code: str, input: str) -> str:
	pass
```

## Notes
- 30000 cells, each wrapped in \[0, 255\] (255 + 1 = 0, and 0 - 1 = 255).
- All code are valid, and will not go beyond the first or the last cell.
- The total operations encountered (including those in a loop) will be <= 20000.