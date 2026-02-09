# Bug Report

### Describe the bug

I'm experiencing an issue with function parameter deoptimization when accessing nested properties. It seems like parameters are being marked as reassigned even when only nested properties are being modified, which is causing incorrect tree-shaking behavior.

### Reproduction

```js
function processData(options) {
  // Modifying a nested property
  options.config.enabled = true;
  return options;
}

const result = processData({
  config: {
    enabled: false
  }
});
```

In this case, the entire `options` parameter is being treated as if it was reassigned, even though only a deeply nested property (`options.config.enabled`) was modified. This causes the bundler to be overly conservative and not tree-shake code that should be removable.

### Expected behavior

When a nested property path like `options.config.enabled` is deoptimized, only that specific path should be marked as deoptimized. The parameter itself should not be marked as reassigned unless it's actually being reassigned at the top level (e.g., `options = something`).

The deoptimization should only propagate to the specific property being modified, not cause the entire parameter to be treated as reassigned.

### Additional context

This seems to affect how the bundler analyzes side effects and determines what code can be safely removed. The issue appears when working with function parameters that have nested object properties being modified.

---
Repository: /testbed
