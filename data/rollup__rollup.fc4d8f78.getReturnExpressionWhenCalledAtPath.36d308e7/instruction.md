# Bug Report

### Describe the bug

I'm experiencing an issue with function call purity detection in my bundled code. Functions that should be marked as pure are being treated as having side effects, which prevents proper tree-shaking and code optimization.

### Reproduction

```js
// Define a pure function
function pureMath(x) {
  return x * 2;
}

// Call it in a way that should be optimized away
const unused = pureMath(5);

// Expected: The call should be removed during tree-shaking
// Actual: The call is preserved in the bundle
```

This seems to affect the dead code elimination phase. When I check the output bundle, code that references pure functions but whose results are never used is still being included.

### Expected behavior

Pure function calls with unused results should be eliminated during the tree-shaking process. The bundler should correctly identify these functions as having no side effects and optimize them out when their return values aren't used.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
