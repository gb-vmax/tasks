# Bug Report

### Describe the bug

Arrow functions that are immediately invoked (IIFE pattern) are not being detected correctly, causing tree-shaking to behave unexpectedly. The bundler seems to be removing or incorrectly handling arrow function IIFEs.

### Reproduction

```js
// IIFE with arrow function
const result = (() => {
  return 'test';
})();

console.log(result); // Should output 'test'
```

When bundling code that uses this pattern, the arrow function IIFE is not being recognized properly. This affects dead code elimination and may cause runtime errors or unexpected behavior.

### Expected behavior

Arrow function IIFEs should be detected and handled the same way as regular function IIFEs. The code should bundle correctly and execute as expected.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
