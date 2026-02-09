# Bug Report

### Describe the bug

I'm encountering an issue with object property shorthand detection. When using shorthand property syntax in object literals, the properties are being incorrectly identified as non-shorthand, and vice versa - regular properties are being detected as shorthand.

### Reproduction

```js
// This shorthand property is incorrectly identified as non-shorthand
const name = 'test';
const obj1 = { name };
// Expected: shorthand = true
// Actual: shorthand = false

// This regular property is incorrectly identified as shorthand
const obj2 = { name: 'test' };
// Expected: shorthand = false  
// Actual: shorthand = true
```

The behavior seems to be completely inverted from what it should be. This is causing issues with code that relies on correctly identifying shorthand vs. regular property syntax.

### Expected behavior

Shorthand properties (like `{ name }`) should be correctly identified as shorthand, and regular properties (like `{ name: 'test' }`) should be identified as non-shorthand.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
