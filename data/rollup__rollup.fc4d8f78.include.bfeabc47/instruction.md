# Bug Report

### Describe the bug

I'm experiencing an issue with binary expressions where the left and right operands are not being included correctly during tree-shaking. It seems like expressions that should be evaluated are being incorrectly removed from the output bundle.

### Reproduction

```js
// Input code
const x = 5;
const y = 10;
const result = x + y;
console.log(result);

// After bundling, the binary expression seems to be handled incorrectly
// and the operands are missing from the output
```

Also seeing issues with `instanceof` checks where the right-hand side's `Symbol.hasInstance` is being called even when it shouldn't be.

### Expected behavior

Binary expressions should have their left and right operands properly included in the bundle when the expression is used. The `instanceof` operator should only trigger the `Symbol.hasInstance` path when appropriate.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
