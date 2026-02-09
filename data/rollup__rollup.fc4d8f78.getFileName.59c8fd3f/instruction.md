# Bug Report

### Describe the bug

I'm encountering an issue with external module path resolution when `renormalizeRenderPath` is enabled. The path normalization logic seems to be inverted - when `renormalizeRenderPath` is `true`, it returns the raw `id` instead of the normalized relative path, and vice versa.

### Reproduction

```js
// Setup with renormalizeRenderPath enabled
const options = {
  external: ['some-external-module'],
  output: {
    paths: {}
  }
};

// When renormalizeRenderPath is true
// Expected: normalized relative path
// Actual: returns the raw module id without normalization

// When renormalizeRenderPath is false  
// Expected: raw module id
// Actual: returns normalized relative path
```

The behavior appears to be backwards from what the flag name suggests. When I set `renormalizeRenderPath: true`, I expect the path to be normalized, but instead I get the unnormalized id.

### Expected behavior

When `renormalizeRenderPath` is `true`, external module paths should be normalized relative to `inputBase`. When it's `false`, the raw module id should be returned without normalization.

### System Info

- rollup version: latest
- Node version: 18.x

---
Repository: /testbed
