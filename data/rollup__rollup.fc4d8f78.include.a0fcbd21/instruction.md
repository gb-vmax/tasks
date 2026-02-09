# Bug Report

### Describe the bug

I'm experiencing an issue with function parameter handling in bundled code. When a function uses destructuring or default parameters, they seem to be getting incorrectly stripped out or not included in the final bundle, even though they should be preserved.

### Reproduction

```js
function example({ a, b = 10 }) {
  console.log(arguments);
  return a + b;
}

export { example };
```

After bundling, the destructured parameters are missing from the output, causing the function to break at runtime.

### Expected behavior

All function parameters (including destructured parameters and those with default values) should be included in the bundled output when the `arguments` object is referenced in the function body. The function should work correctly in the final bundle.

### Additional context

This seems to affect functions that reference the `arguments` object. Simple identifier parameters work fine, but more complex parameter patterns get lost during the bundling process.

---
Repository: /testbed
