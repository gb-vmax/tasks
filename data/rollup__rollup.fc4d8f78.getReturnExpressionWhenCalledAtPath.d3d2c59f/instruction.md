# Bug Report

### Describe the bug

I'm experiencing an issue with number literal method calls in nested property paths. When calling methods on number literals through chained property access (e.g., `obj.prop.num.toFixed()`), the return type analysis seems to be incorrect.

### Reproduction

```js
const obj = {
  nested: {
    value: 42
  }
}

// This should work but the type inference appears broken
const result = obj.nested.value.toFixed(2)
```

The issue appears when accessing number methods through multiple levels of nesting. Direct calls like `(42).toFixed(2)` work fine, but when the number is accessed via a longer property path, something goes wrong with how the return expression is determined.

### Expected behavior

Number literal methods should be properly recognized and their return types correctly inferred regardless of the depth of the property path used to access them.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
