# Bug Report

### Describe the bug

The `getModel()` function is now case-insensitive when matching model types, which breaks existing code that relies on exact case matching. This causes issues when trying to retrieve models using the correct case-sensitive type string.

### Reproduction

```js
// Assuming we have a model with type 'Request'
const model = getModel('Request');
// This should return the Request model

// But now this also returns the same model:
const wrongModel = getModel('request');
// This shouldn't work but it does

// This can cause unexpected behavior when model types differ only in casing
```

### Expected behavior

The `getModel()` function should perform case-sensitive matching on model types. If I pass `'Request'` it should only match a model with type `'Request'`, not `'request'` or `'REQUEST'`.

### Additional context

This seems like a regression - the function used to do exact matching before. Case-sensitive type matching is important for distinguishing between different model types that might have similar names with different casing conventions.

---
Repository: /testbed
