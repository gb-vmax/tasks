# Bug Report

### Describe the bug

I'm experiencing an issue where the first argument in function calls isn't being processed correctly during tree-shaking. It seems like the first argument is being skipped entirely when determining which code paths should be included in the bundle.

### Reproduction

```js
function processData(config, data, options) {
  // Function that should be analyzed for side effects
  return transform(config, data, options);
}

// When calling with multiple arguments
processData(myConfig, myData, myOptions);
```

In this case, `myConfig` (the first argument) doesn't seem to be getting properly analyzed, which can lead to incorrect tree-shaking behavior. The subsequent arguments appear to be handled correctly, but the first one is being overlooked.

### Expected behavior

All arguments passed to a function should be analyzed equally for side effects and path inclusion during the bundling process. The first argument should not be treated differently from the others.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues in production builds where code that should be included is being incorrectly removed from the bundle.

---
Repository: /testbed
