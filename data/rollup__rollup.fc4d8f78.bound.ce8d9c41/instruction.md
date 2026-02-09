# Bug Report

### Describe the bug

I'm experiencing an issue with member expression handling where property access on objects appears to be incorrectly bound. When accessing properties through member expressions (e.g., `obj.property` or `obj['property']`), the binding state seems to be inverted, causing unexpected behavior in the compiled output.

### Reproduction

```js
const obj = {
  value: 42
};

// Accessing a member property
console.log(obj.value);

// Or using bracket notation
console.log(obj['value']);
```

The member expressions are not being handled correctly, and the bound state appears to be flipped. This affects how properties are resolved and can lead to incorrect code generation or runtime behavior.

### Expected behavior

Member expressions should correctly track their bound state and resolve property access as expected. The binding logic should properly determine whether a member expression has been bound to its context.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
