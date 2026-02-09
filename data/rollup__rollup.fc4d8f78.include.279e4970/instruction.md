# Bug Report

### Describe the bug

When using arrow functions with destructured parameters, the first parameter doesn't get included in the output bundle. Only parameters after the first one are being processed correctly.

### Reproduction

```js
// Input code
export const myFunction = ({ a }, { b }) => {
  return a + b;
};

// After bundling, the first parameter `{ a }` is not included properly
// Only `{ b }` gets handled correctly
```

This seems to affect arrow functions specifically when they have multiple parameters that are not simple identifiers (e.g., destructured objects or arrays).

### Expected behavior

All parameters of an arrow function should be included in the bundle, regardless of their position. The first parameter should be treated the same way as subsequent parameters.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
