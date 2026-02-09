# Bug Report

### Describe the bug

I'm encountering an issue where assignment targets in member expressions are not being included correctly in the output bundle. When a member expression is used as an assignment target, it seems like the node inclusion logic is not working as expected.

### Reproduction

```js
const obj = {};
obj.nested = {};
obj.nested.value = 42;
```

When bundling code like this, the assignment target (`obj.nested.value`) should be properly included in the output, but it appears that the inclusion logic is inverted - nodes are only being processed when they're already included, rather than when they need to be included.

### Expected behavior

Assignment targets in member expressions should be properly included in the bundle regardless of their current inclusion state. The bundler should mark these nodes for inclusion when they're used as assignment targets.

### Additional context

This seems to affect any code that uses member expressions on the left-hand side of an assignment. The issue might be related to how the inclusion context is being checked before processing the assignment target.

---
Repository: /testbed
