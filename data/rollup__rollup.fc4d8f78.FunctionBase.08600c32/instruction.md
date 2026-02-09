# Bug Report

### Describe the bug

I'm experiencing an issue where functions with side effects in their first parameter are not being properly detected. It seems like the tree-shaking logic is skipping the first parameter when checking for side effects, which causes incorrect code elimination in some cases.

### Reproduction

```js
function processData(config = setupGlobalState(), data) {
  return data;
}

// The setupGlobalState() call in the first parameter should be preserved
// because it has side effects, but it's being removed during tree-shaking
const result = processData(undefined, someData);
```

The function call to `setupGlobalState()` in the default parameter should be kept since it has side effects, but it appears to be getting removed during the optimization phase.

### Expected behavior

Functions should check all parameters for side effects, including the first one. Default parameter expressions that have side effects should always be preserved regardless of their position.

### Additional context

This seems to affect any function where the first parameter has a default value with side effects. Parameters after the first one are handled correctly, but the first parameter's side effects are being ignored.

---
Repository: /testbed
