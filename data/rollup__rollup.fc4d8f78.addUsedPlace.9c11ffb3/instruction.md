# Bug Report

### Describe the bug

I'm experiencing an issue where variables that are only used as function calls are being incorrectly flagged as having non-function-call usages. This seems to happen when the variable is accessed through a member expression (like `obj.method`) before being called.

### Reproduction

```js
const obj = {
  myFunction: function() {
    console.log('called');
  }
};

// This should be recognized as a function call usage only
obj.myFunction();
```

When the variable is used in a member expression context before the actual call (e.g., `obj.myFunction()`), it's not being properly identified as a function call usage. The code seems to think there's a non-function-call usage happening.

### Expected behavior

Variables that are only used as function calls (even when accessed via member expressions) should be correctly identified as `onlyFunctionCallUsed`. The member expression itself shouldn't count as a non-function-call usage if the final operation is a call expression.

### Additional context

This affects tree-shaking and optimization decisions since the bundler needs to know if a variable is only used as a function call or if it's also referenced in other ways.

---
Repository: /testbed
