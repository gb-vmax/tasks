# Bug Report

### Describe the bug

I'm experiencing an issue where function call arguments are not being included properly during tree-shaking. It seems like arguments to function calls are being incorrectly removed from the output bundle, causing runtime errors when those arguments should be preserved.

### Reproduction

```js
// input.js
function processData(data, options) {
  return options.transform(data);
}

const result = processData(myData, {
  transform: x => x * 2
});

console.log(result);
```

After bundling, the call arguments seem to be missing or not properly included in the output, leading to undefined references at runtime.

### Expected behavior

All function call arguments should be included in the bundled output when the function call itself is included. The tree-shaking process should preserve the arguments along with the function invocation.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to have started happening recently. The bundled code runs but throws errors about missing arguments that should have been included.

---
Repository: /testbed
