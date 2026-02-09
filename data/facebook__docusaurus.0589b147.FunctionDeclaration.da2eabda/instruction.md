# Bug Report

### Describe the bug

I'm encountering an issue with function declarations in generated code. When I have a regular (non-generator) function, the output incorrectly includes `function*` instead of `function`. Similarly, when I have an actual generator function, it's being output as a regular `function` instead of `function*`.

### Reproduction

```js
// Input: Regular function
function myFunction() {
  return 42;
}

// Generated output includes: function* myFunction() { ... }
// Expected output should be: function myFunction() { ... }

// Input: Generator function
function* myGenerator() {
  yield 1;
}

// Generated output includes: function myGenerator() { ... }
// Expected output should be: function* myGenerator() { ... }
```

The function types are being inverted - generators are rendered as regular functions and regular functions are rendered as generators.

### Expected behavior

- Regular functions should be output as `function functionName()`
- Generator functions should be output as `function* functionName()`

The generator asterisk should only appear when the function actually is a generator.

---
Repository: /testbed
