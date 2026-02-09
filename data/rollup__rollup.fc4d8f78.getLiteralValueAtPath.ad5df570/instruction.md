# Bug Report

### Describe the bug

Template literals are not being properly evaluated at compile time. When using a simple template literal without any expressions (e.g., `` `hello` ``), the bundler should be able to determine its literal value for optimization purposes, but it's currently returning `UnknownValue` instead of the actual string value.

### Reproduction

```js
// Simple template literal without expressions
const greeting = `hello world`;

// This should be optimizable but isn't being detected
console.log(greeting);
```

The bundler should recognize that this is a static string value and optimize accordingly, but it's treating it as an unknown value even though there are no dynamic expressions in the template.

### Expected behavior

Template literals without any expressions (just a single quasi element) should be treated the same as regular string literals and their values should be extractable for optimization purposes.

### Additional context

This seems to affect tree-shaking and dead code elimination since the bundler can't determine the literal values of simple template strings anymore.

---
Repository: /testbed
