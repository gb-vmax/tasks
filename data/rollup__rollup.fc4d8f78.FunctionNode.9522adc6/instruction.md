# Bug Report

### Describe the bug

I'm encountering an issue with function parameter handling in the bundler. When a function has both non-identifier parameters (like destructuring patterns or rest parameters) and uses the `arguments` object, the parameters aren't being processed correctly.

### Reproduction

```js
function example({ a, b }, ...rest) {
  console.log(arguments);
  return a + b;
}

// The function parameters should be included in the bundle
// but they're being skipped incorrectly
```

### Expected behavior

All function parameters should be properly included and processed when the function uses the `arguments` object, regardless of whether they are simple identifiers or complex patterns like destructuring or rest parameters.

### Additional context

This seems to affect functions that have:
- Destructuring parameters (object or array)
- Rest parameters
- Default parameters
- AND use the `arguments` object

The issue doesn't occur if the function only has simple identifier parameters or if it doesn't reference `arguments`.

---
Repository: /testbed
