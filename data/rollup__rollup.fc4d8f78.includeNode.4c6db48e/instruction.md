# Bug Report

### Describe the bug

When bundling code with functions that have destructured parameters or rest parameters, the tree-shaking behavior is incorrect. Parameters are not being properly included in the bundle when the `arguments` variable is not used.

### Reproduction

```js
function example({ a, b }) {
  return a + b;
}

// Or with rest parameters
function example2(...args) {
  return args.length;
}

export { example, example2 };
```

When bundling this code, the function parameters are incorrectly included/excluded from the output, leading to broken code in the final bundle.

### Expected behavior

All function parameters (including destructured and rest parameters) should be properly included in the bundle regardless of whether the `arguments` variable is used within the function body.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
