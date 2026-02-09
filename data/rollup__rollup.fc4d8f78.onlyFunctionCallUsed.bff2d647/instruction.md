# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking of named IIFEs (Immediately Invoked Function Expressions). When a named function expression is immediately invoked, it's being incorrectly removed during the tree-shaking process, even though it has side effects that should be preserved.

### Reproduction

```js
// Input code
const result = (function myFunc() {
  console.log('This should run');
  return 42;
})();

console.log(result);
```

After bundling, the IIFE gets removed entirely, causing the side effect (console.log) to be lost and `result` to be undefined.

### Expected behavior

Named IIFEs should be treated the same as anonymous IIFEs - they should be preserved when they have side effects or when their return value is used. The function name in an IIFE is just for internal reference and shouldn't affect whether the expression is considered "used".

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
