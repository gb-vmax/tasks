# Bug Report

### Describe the bug

I'm experiencing an issue where function parameters are not being included correctly during tree-shaking. It seems like non-identifier parameters (like destructured parameters or rest parameters) are being skipped when they should be included in the bundle.

### Reproduction

```js
// Input code
function myFunction({ prop1, prop2 }) {
  console.log(prop1, prop2);
}

// After bundling, the destructured parameters are not properly included
// This causes runtime errors when the function is called
```

Another example:
```js
function handler(...args) {
  return args.length;
}

// The rest parameter handling seems broken
```

### Expected behavior

All function parameters, including destructured parameters, array patterns, and rest parameters should be properly included in the output bundle. The bundled code should work the same as the input code.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be a regression as it was working fine in previous versions. The issue only manifests when tree-shaking is enabled.

---
Repository: /testbed
