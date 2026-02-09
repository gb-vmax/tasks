# Bug Report

### Describe the bug

When creating multiple proto directories with the same name under the same parent, the system doesn't prevent duplicate names. This leads to confusion when multiple directories with identical names exist in the same location.

### Reproduction

```js
const parentId = 'some-parent-id';

// Create first directory
await create({ parentId, name: 'MyProtos' });

// Create second directory with same name - should get a unique name
await create({ parentId, name: 'MyProtos' });

// Both directories end up with the name 'MyProtos'
// Expected: second one should be 'MyProtos (2)' or similar
```

### Expected behavior

When creating a proto directory with a name that already exists among its siblings, the system should automatically append a counter (e.g., "(2)", "(3)", etc.) to make the name unique, similar to how file systems handle duplicate filenames.

### Additional context

This becomes especially problematic when importing multiple proto files or creating directories programmatically, as there's no way to distinguish between directories with the same name in the UI.

---
Repository: /testbed
