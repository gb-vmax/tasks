# Bug Report

### Describe the bug

I'm experiencing an issue with property copying in the remark-gfm vendor module. When properties are being copied between objects, it seems like there's a circular reference problem where properties are referencing themselves instead of the source object.

### Reproduction

```js
const source = {
  value: 'original',
  nested: {
    prop: 'data'
  }
};

const target = {};

// After copying properties using __copyProps
// target.value should return 'original' from source
// but instead it's trying to access target.value (which doesn't exist yet)
```

This results in properties being undefined or causing infinite loops when accessed, rather than correctly retrieving values from the source object.

### Expected behavior

Properties copied from the source object should correctly reference and return values from the source, not from the target object itself.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
