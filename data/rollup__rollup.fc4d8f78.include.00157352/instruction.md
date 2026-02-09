# Bug Report

### Describe the bug

I'm experiencing an issue where member expressions seem to be incorrectly included in the output bundle. Properties are being accessed before they should be available, leading to unexpected behavior in the generated code.

### Reproduction

```js
const obj = {
  nested: {
    value: 42
  }
};

// Accessing nested property
const result = obj.nested.value;
```

When bundling code that contains member expressions like the above, the property access appears to be evaluated in the wrong order. This causes the bundled output to reference properties before the object itself is properly included.

### Expected behavior

Member expressions should be included in the correct order - the object should be fully processed before its properties are accessed. The current behavior seems to process things out of sequence.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how the inclusion context handles nested member expressions. The issue becomes more apparent with deeply nested property access chains.

---
Repository: /testbed
