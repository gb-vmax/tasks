# Bug Report

### Describe the bug

I'm experiencing an issue where variables that are used in non-function-call contexts are incorrectly being marked as only used in function calls. This affects tree-shaking and code optimization behavior.

### Reproduction

```js
// Example code that triggers the issue
function myFunction() {
  console.log('test');
}

// Using the function in a non-call context
const ref = myFunction;
export default ref;
```

In this case, `myFunction` is being referenced but not called. However, the variable tracking seems to be incorrectly identifying this usage pattern.

### Expected behavior

When a variable is used in a non-call context (like being assigned to another variable or exported), it should be properly tracked as having non-function-call usage. The `onlyFunctionCallUsed` flag should be set to `false` for such cases.

Currently, it appears that:
1. Variables referenced in export default declarations are not being handled correctly
2. The logic for detecting whether a variable is used as a function call vs. a regular reference seems inverted

### System Info
- Rollup version: latest
- Node version: 18.x

This is affecting our bundle optimization as functions that should be preserved are being incorrectly flagged.

---
Repository: /testbed
