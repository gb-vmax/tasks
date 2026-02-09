# Bug Report

### Describe the bug

The `canDuplicate()` function is returning incorrect values when checking if a model type can be duplicated. It seems to be returning the opposite of what's expected - returning `false` when it should return `true` and vice versa.

### Reproduction

```js
// For a model that exists and has canDuplicate = true
const result = canDuplicate('request');
console.log(result); // Expected: true, Actual: false

// For a model that exists and has canDuplicate = false (or undefined)
const result2 = canDuplicate('workspace');
console.log(result2); // Expected: false, Actual: depends on model existence
```

### Expected behavior

When calling `canDuplicate()` with a valid model type:
- Should return `true` if the model exists and its `canDuplicate` property is `true`
- Should return `false` if the model doesn't exist or if `canDuplicate` is `false`/`undefined`

Currently the logic appears inverted and duplication functionality is broken for models that should support it.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
