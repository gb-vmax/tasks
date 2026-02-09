# Bug Report

### Describe the bug

I'm experiencing an issue with IIFE (Immediately Invoked Function Expression) code generation where the wrapping logic seems incorrect. When generating code snippets with arrow functions enabled, the function wrapping behavior doesn't match what I expect.

### Reproduction

When using `getDirectReturnIifeLeft` with arrow functions enabled and `needsArrowReturnParens` set to true, the generated code has incorrect parentheses placement. 

```js
// Configuration
const config = {
  arrowFunctions: true,
  needsArrowReturnParens: true,
  needsWrappedFunction: false
}

// The generated IIFE wrapper appears to have the wrong wrapping condition
// Expected: wrapping should apply when either arrowFunctions OR needsArrowReturnParens is true
// Actual: wrapping only applies when arrowFunctions AND needsArrowReturnParens are both true
```

### Expected behavior

The return value wrapping should use OR logic (`||`) for `arrowFunctions` and `needsArrowReturnParens`, not AND logic (`&&`). Similarly, the outer wrapping condition should use AND logic for `arrowFunctions` and `needsWrappedFunction`.

This affects the structure of generated IIFEs and can lead to invalid JavaScript syntax in certain configurations.

### System Info
- Version: latest
- Node: 18.x

---
Repository: /testbed
