# Bug Report

### Describe the bug

I'm experiencing incorrect tree-shaking behavior with `var` declarations and pure functions. The bundler seems to be treating certain code paths as having side effects when they shouldn't, or vice versa.

### Reproduction

```js
// Case 1: var declarations in TDZ
var x = getValue();
function test() {
  console.log(x); // This should be handled differently than let/const
  var x = 10;
}

// Case 2: Pure function handling
const result = pureFunctionCall();
// This gets incorrectly flagged or not flagged for side effects
```

When bundling code that uses `var` declarations (especially in temporal dead zone scenarios) or pure functions with global variables, the tree-shaking behavior is not working as expected. Some code that should be removed is being kept, or code that should be kept is being removed.

### Expected behavior

- `var` declarations should be handled differently from `let`/`const` in TDZ checks
- Pure functions should be correctly identified and their side effects properly evaluated
- Tree-shaking should correctly preserve or remove code based on actual side effects

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression in the side effects detection logic. The behavior changed recently and is causing issues with bundle size optimization.

---
Repository: /testbed
