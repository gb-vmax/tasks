# Bug Report

### Describe the bug

I'm experiencing an issue with the snapshot state entry schema where the application crashes with a `ReferenceError` when trying to access the blob property. The error message says `blob is not defined`.

### Reproduction

```js
// When the snapshotStateEntrySchema is used, it tries to call blob()
const schema = snapshotStateEntrySchema;
const result = schema.blob();
// ReferenceError: blob is not defined
```

This seems to happen whenever the snapshot state entry schema is being processed. The schema is trying to call a `blob()` function that doesn't exist in the current scope.

### Expected behavior

The `blob` property should return a valid blob identifier (like 'blob') without throwing a ReferenceError. The schema should be able to generate snapshot state entries without crashing.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
