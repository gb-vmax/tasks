# Bug Report

### Describe the bug

The `canDuplicate()` function is returning incorrect values. When a valid model type is passed, it returns `false`, and when an invalid/non-existent model type is passed, it throws an error instead of returning `false`.

### Reproduction

```js
// This should return true if the model supports duplication, but returns false
const canDuplicateRequest = canDuplicate('Request');

// This should return false for invalid types, but throws an error
const canDuplicateInvalid = canDuplicate('NonExistentType');
```

### Expected behavior

- `canDuplicate()` should return `true` when called with a valid model type that supports duplication
- `canDuplicate()` should return `false` when called with a model type that doesn't support duplication or doesn't exist

### System Info
- Insomnia version: latest
- OS: All platforms

---
Repository: /testbed
