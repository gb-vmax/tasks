# Bug Report

### Describe the bug

I'm encountering an issue with rest/spread operator syntax generation. When using rest parameters in function declarations or spread operators in expressions, the output has the `...` appearing in the wrong position.

### Reproduction

```js
// Function with rest parameter
function example(...args) {
  return args;
}

// Object with spread
const obj = { ...source };

// Array with spread
const arr = [...items];
```

When processing these patterns, the spread/rest operator (`...`) is being placed after the argument/expression instead of before it, resulting in invalid JavaScript syntax like `args...` instead of `...args`.

### Expected behavior

The `...` operator should appear before the argument/expression name, not after it. The generated code should be valid JavaScript with proper rest/spread syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
