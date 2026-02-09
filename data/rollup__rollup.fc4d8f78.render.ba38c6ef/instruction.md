# Bug Report

### Describe the bug

I'm experiencing an issue with how `return` statements are being rendered in the output. When there's a return statement with an argument that doesn't have whitespace immediately after the `return` keyword, the spacing is getting messed up in the generated code.

### Reproduction

```js
// Input code
function test() {
  return(value);
}

// Expected output
function test() {
  return (value);
}

// Actual output - space is added in the wrong place
function test() {
  return  (value);
}
```

It seems like when the argument starts right after `return` (position-wise), the whitespace handling is incorrect. The space either gets added when it shouldn't, or gets added in the wrong position.

### Expected behavior

Return statements should be rendered with proper spacing - a single space between `return` and its argument when needed, and no extra spaces should be added when whitespace already exists.

### Additional context

This appears to affect cases where:
- The return argument is immediately adjacent to the keyword (no space in source)
- The return argument already has space after the keyword

The output is producing malformed spacing in the generated code.

---
Repository: /testbed
