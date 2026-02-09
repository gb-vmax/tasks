# Bug Report

### Describe the bug

I'm experiencing an issue with arrow functions where the first parameter seems to be ignored or not processed correctly. When using arrow functions with multiple parameters, the behavior is inconsistent - it looks like the first parameter isn't being handled the same way as the rest.

### Reproduction

```js
const myArrowFunc = (a, b, c) => {
  return a + b + c;
};

// When bundling, the first parameter 'a' doesn't seem to be 
// processed correctly in certain scenarios
```

I noticed this affects arrow functions specifically, and it seems related to how parameters are being iterated over during the compilation/bundling process.

### Expected behavior

All parameters of an arrow function should be processed equally, regardless of their position. The first parameter should receive the same treatment as subsequent parameters.

### Additional context

This appears to have started recently. Not sure if there was a change in how arrow function parameters are handled, but the first parameter is definitely being treated differently than it should be.

---
Repository: /testbed
