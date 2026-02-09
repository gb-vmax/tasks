# Bug Report

### Describe the bug

Class expressions are being wrapped in parentheses when they shouldn't be, causing invalid JavaScript output in certain contexts.

### Reproduction

When a class expression is used as a standalone expression statement, it's getting wrapped in parentheses incorrectly. This results in malformed output.

```js
// Input code
class MyClass {
  constructor() {}
}

// Expected output (when used as expression statement)
class MyClass {
  constructor() {}
}

// Actual output
(class MyClass {
  constructor() {
  }
})
```

The parentheses are being added in the wrong cases - they should only wrap the class expression when it's NOT an expression statement, but currently they're being added in the opposite scenario.

### Expected behavior

Class expressions should only be wrapped in parentheses when necessary (i.e., when they're NOT already in an expression statement context). When they are expression statements, they should remain unwrapped.

### Additional context

This seems to affect the rendering logic for class expressions. The wrapping behavior appears to be inverted from what it should be.

---
Repository: /testbed
