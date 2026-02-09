# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking of IIFEs (Immediately Invoked Function Expressions). It seems like function expressions that should be recognized as IIFEs are not being detected correctly, which is causing them to be incorrectly removed or retained during the bundling process.

### Reproduction

```js
// This IIFE should be handled correctly
(function() {
  console.log('This should execute');
})();

// Named function expression called immediately
(function myFunc() {
  console.log('Named IIFE');
})();
```

When bundling code with IIFEs, the detection logic appears to be broken. The bundler is not properly identifying when a function expression is being immediately invoked.

### Expected behavior

IIFEs should be correctly identified so that:
1. The function expression is recognized as being immediately called
2. Tree-shaking decisions are made based on accurate IIFE detection
3. Side effects from IIFEs are preserved when necessary

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as it was working fine in previous versions. The logic for determining if a function is only used as a function call seems off.

---
Repository: /testbed
