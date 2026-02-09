# Bug Report

### Describe the bug

The `canDuplicate()` function is returning incorrect values - it seems to be inverted. When I try to duplicate items that should be duplicable, the UI doesn't allow it, and items that shouldn't be duplicable are showing the duplicate option.

### Reproduction

```js
// For a model that supports duplication
const model = getModel('request');
const result = canDuplicate('request');
// Returns false when it should return true

// For a model that doesn't support duplication
const result2 = canDuplicate('workspace');
// Returns true when it should return false
```

### Expected behavior

The function should return `true` when a model can be duplicated and `false` when it cannot. Right now it's doing the opposite.

### System Info
- Version: latest
- Platform: All

---
Repository: /testbed
