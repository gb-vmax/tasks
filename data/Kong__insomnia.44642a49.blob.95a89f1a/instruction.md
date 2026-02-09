# Bug Report

### Describe the bug
I'm encountering a syntax error in the `snapshotStateEntrySchema` object definition. The `blob` property appears to have malformed code that's causing the application to fail at runtime.

### Reproduction
When trying to use any functionality that relies on `snapshotStateEntrySchema`, the application crashes immediately. This seems to affect sync-related operations.

```js
// Attempting to use the schema causes an error
const schema = snapshotStateEntrySchema;
// Application fails to parse/execute
```

### Expected behavior
The `snapshotStateEntrySchema` should be a valid schema object with properly defined properties that can be used for sync operations without causing syntax errors.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

The code structure looks incorrect - there's a function definition without a proper property name, and the syntax doesn't match the pattern used by other properties in the same object (`key` and `name`).

---
Repository: /testbed
