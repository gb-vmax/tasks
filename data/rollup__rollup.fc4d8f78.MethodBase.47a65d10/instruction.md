# Bug Report

### Describe the bug

I'm experiencing an issue where computed property keys in object methods are being treated incorrectly. When I use bracket notation to define a method with a computed property name, it seems like the computed flag is inverted - methods that should be recognized as computed are treated as non-computed and vice versa.

### Reproduction

```js
const obj = {
  // This should be treated as a computed property
  [Symbol.iterator]() {
    return this;
  },
  
  // This should be treated as a regular property
  normalMethod() {
    return 'test';
  }
}
```

The bundler appears to be misidentifying which methods have computed keys vs. regular string keys. This causes incorrect code generation and runtime errors when the computed properties are accessed.

### Expected behavior

Methods defined with bracket notation (computed property names) should be correctly identified and handled differently from regular named methods during the compilation/bundling process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
