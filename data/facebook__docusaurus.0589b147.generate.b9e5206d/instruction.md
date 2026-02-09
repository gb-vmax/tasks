# Bug Report

### Describe the bug

After a recent update, the MDX generator is returning an object with a `value` property instead of returning the output directly. This breaks existing code that expects the generator output to be a string.

### Reproduction

```js
const result = generate(node, options);

// Before: result was a string
console.log(result); // Expected: "generated output"

// Now: result is an object
console.log(result); // Actual: { value: "generated output" }

// This breaks existing code that does:
const output = result.trim();
// TypeError: result.trim is not a function
```

### Expected behavior

The `generate()` function should return the output string directly, not wrapped in an object. This is how it worked previously and changing the return type is a breaking change for existing consumers of the API.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
