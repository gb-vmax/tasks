# Bug Report

### Describe the bug

The `canDuplicate` function is returning inverted results - it returns `true` when a model cannot be duplicated and `false` when it can be duplicated. This is causing issues when trying to duplicate resources in the application.

### Reproduction

```js
// For a model that has canDuplicate: true
const model = getModel('request');
const result = canDuplicate('request');
// Expected: true
// Actual: false

// For a model that has canDuplicate: false  
const model2 = getModel('workspace');
const result2 = canDuplicate('workspace');
// Expected: false
// Actual: true
```

### Expected behavior

The function should return `true` when the model's `canDuplicate` property is `true`, and `false` when it's `false`. Currently it's doing the opposite.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
