# Bug Report

### Describe the bug

I'm experiencing an issue with global variable access detection. When accessing properties on global variables, the bundler is incorrectly treating them as having side effects and not properly tree-shaking the code.

### Reproduction

```js
// This code should be tree-shaken but isn't
const x = undefined.toString;

// Also affects property access on other globals
const y = Math.random.toString;
```

The problem seems to be that accessing properties on global variables (especially `undefined`) is being flagged as having effects when it shouldn't be. This prevents dead code elimination from working correctly.

### Expected behavior

Property access on global variables like `undefined` should not be considered as having side effects. The code above should be properly tree-shaken when the variables are unused.

### Additional context

This appears to have started happening recently. The bundler used to correctly identify that these property accesses are safe and could be removed during tree-shaking.

---
Repository: /testbed
