# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with the database `get` function when passing `undefined` as the `id` parameter. The function now appears to be returning `null` instead of the expected behavior.

### Reproduction

```js
const result = await database.get('Request', undefined);
// Expected: should handle undefined properly
// Actual: returns null immediately
```

Previously, when calling `database.get()` with an undefined `id`, the function would properly handle this case. Now it seems to short-circuit and return `null` without the expected processing.

### Steps to reproduce:
1. Call `database.get(type, undefined)` where type is any valid document type
2. Observe that the function returns `null`
3. Expected behavior was different before the recent changes

### Expected behavior

The function should handle `undefined` id parameters the same way it did before. In some cases, passing `undefined` was valid and would be processed accordingly by the underlying `_send` function.

### Additional context

This seems to have started happening after some recent changes to the database module. The issue occurs specifically when `id` is `undefined` (not just when it's `'n/a'`).

---
Repository: /testbed
