# Bug Report

### Describe the bug

I'm encountering an issue with variable reassignment tracking in nested object paths. When I try to modify a property on a local variable, the reassignment detection appears to be inverted - it's triggering deoptimization when the path is non-empty instead of when it's empty.

### Reproduction

```js
// Given a local variable with nested properties
const obj = {
  nested: {
    value: 42
  }
}

// Modifying the root should trigger reassignment
obj = {}  // This doesn't get tracked properly

// But modifying nested properties triggers it instead
obj.nested.value = 100  // This incorrectly marks as reassigned
```

Additionally, there seems to be a problem with the interaction tracking logic. Variables that should be considered as having effects are being skipped, and vice versa. The condition for checking whether an entity path has been tracked appears to be backwards.

### Expected behavior

- Reassignment should only be marked when the path length is 0 (i.e., the variable itself is being reassigned)
- Nested property modifications should not trigger full variable reassignment
- The interaction tracking should correctly identify when a path has already been tracked to avoid redundant effect checks

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing incorrect tree-shaking behavior where code that should be removed is being kept, and in some cases variables are being incorrectly marked as reassigned when only their properties are modified.

---
Repository: /testbed
