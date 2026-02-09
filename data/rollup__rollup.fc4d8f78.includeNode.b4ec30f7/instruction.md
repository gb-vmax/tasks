# Bug Report

### Describe the bug

I'm experiencing an issue where function parameters that are destructuring patterns or rest parameters are not being included in the bundle when they should be. This seems to affect tree-shaking behavior in certain scenarios.

### Reproduction

```js
function example({ prop1, prop2 }) {
  // Destructuring parameter should be included
  console.log(prop1, prop2);
}

function withRest(...args) {
  // Rest parameter should be included
  console.log(args);
}

function withArray([first, second]) {
  // Array destructuring parameter should be included
  console.log(first, second);
}
```

When bundling code with functions that use non-identifier parameters (destructuring, rest parameters, etc.), these parameters are being incorrectly excluded from the output bundle even when the function is used.

### Expected behavior

All function parameters, regardless of whether they are simple identifiers, destructuring patterns, or rest parameters, should be properly included in the bundle when the function is included. The current behavior seems to only include identifier parameters unless the `arguments` variable is used.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
