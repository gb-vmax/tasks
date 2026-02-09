# Bug Report

### Describe the bug

Getting a stack overflow error when accessing the deprecated `originalFileName` property on emitted assets. The property getter seems to be calling itself recursively instead of returning the actual value.

### Reproduction

```js
const asset = {
  fileName: 'test.js',
  name: 'test',
  needsCodeReference: false,
  names: ['test'],
  get originalFileName() {
    // ... deprecation warning
    return this.originalFileName; // This causes infinite recursion
  },
  originalFileNames: ['original.js'],
  source: '...',
  type: 'asset'
};

// Accessing this property crashes
console.log(asset.originalFileName); // RangeError: Maximum call stack size exceeded
```

### Expected behavior

The property should return the original file name value with a deprecation warning, not throw a stack overflow error.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
