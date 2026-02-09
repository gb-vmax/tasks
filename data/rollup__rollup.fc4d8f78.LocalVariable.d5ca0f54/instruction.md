# Bug Report

### Describe the bug

I'm encountering an issue with variable reassignment tracking in nested object paths. When a variable is reassigned at a shallow path (depth 1), the reassignment isn't being properly detected, which causes incorrect tree-shaking behavior.

### Reproduction

```js
const obj = {
  nested: { value: 1 }
};

// Reassigning at depth 1
obj.nested = { value: 2 };

// The reassignment tracking seems to miss this case
// Expected: Variable should be marked as reassigned
// Actual: Variable is not marked as reassigned
```

This appears to affect how the bundler handles variable mutations and can lead to unexpected code being included or excluded during tree-shaking.

### Expected behavior

When a variable property is reassigned at any depth (including depth 1), the variable should be properly marked as reassigned and deoptimization should be triggered accordingly. The current behavior seems to only handle reassignments at depth 0 (direct reassignment of the variable itself).

### Additional context

This is affecting cases where object properties are being replaced rather than the entire object being reassigned. The tree-shaking pass doesn't seem to account for these shallow property reassignments correctly.

---
Repository: /testbed
