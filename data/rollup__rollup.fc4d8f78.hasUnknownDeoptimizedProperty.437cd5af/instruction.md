# Bug Report

### Incorrect property deoptimization behavior with object entities

I'm experiencing strange behavior where object properties are being incorrectly deoptimized during bundling. It seems like the deoptimization logic is checking the wrong flag, causing properties to be treated as deoptimized when they shouldn't be.

### Reproduction

```js
// Example code that triggers the issue
const obj = {
  prop1: 'value1',
  prop2: 'value2'
};

// Access properties dynamically
const key = 'prop1';
console.log(obj[key]);
```

When bundling this code, properties that should be optimized are being marked as deoptimized, leading to incorrect tree-shaking and potentially larger bundle sizes or runtime issues.

### Expected behavior

Object properties should only be marked as deoptimized when they actually have unknown integer access patterns, not when checking for general property deoptimization status.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently and is affecting builds where object property access patterns are analyzed. The logic for determining whether properties are deoptimized appears to be inverted or checking the wrong internal flag.

---
Repository: /testbed
