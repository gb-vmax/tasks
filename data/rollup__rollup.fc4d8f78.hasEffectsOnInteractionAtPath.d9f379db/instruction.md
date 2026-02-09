# Bug Report

### Describe the bug

I'm experiencing an issue where certain property accesses on objects are being incorrectly flagged as having side effects, causing unnecessary code to be included in the bundle. This is leading to larger bundle sizes than expected.

### Reproduction

```js
const obj = {
  data: {
    value: 42
  }
}

// Accessing nested properties
const result = obj.data.value

// The code above is being treated as if it has side effects
// even though it's just a simple property access
```

When bundling code that accesses nested object properties, the bundler seems to assume these operations always have side effects, preventing proper tree-shaking.

### Expected behavior

Simple property reads on objects should not be considered as having side effects. Only actual interactions (like function calls, assignments, etc.) should be flagged as potentially having side effects. This would allow the bundler to properly eliminate dead code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
