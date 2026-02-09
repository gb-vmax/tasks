# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where object properties are being included multiple times in the bundle. It seems like when a property path is accessed repeatedly, the inclusion logic doesn't properly check if the property has already been marked as included, leading to redundant processing.

### Reproduction

```js
const obj = {
  nested: {
    deep: {
      value: 'test'
    }
  }
}

// Accessing the same path multiple times
obj.nested.deep.value
obj.nested.deep.value
obj.nested.deep.value
```

When bundling code that accesses the same nested property path multiple times, the property inclusion appears to be processed redundantly instead of being handled only once.

### Expected behavior

Each property should only be marked as included once, regardless of how many times the path is accessed during the inclusion phase. Subsequent calls to include the same path should be no-ops after the first inclusion.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
