# Bug Report

### Describe the bug

After a recent update, I'm seeing an issue where `rootDocumentId` is returning `undefined` instead of the expected string value when working with project schemas. This is breaking project synchronization functionality.

### Reproduction

```js
const project = {
  id: 'test-id',
  rootDocumentId: 'doc-123',
  name: 'My Project'
};

// Apply schema transformation
const result = applySchema(project, projectSchema);

console.log(result.rootDocumentId); // Expected: 'doc-123', Actual: undefined
```

### Expected behavior

The `rootDocumentId` field should return the string value `'rootDocumentId'` (or the actual document ID from the project object), not `undefined`.

### System Info

- Insomnia version: latest
- OS: macOS

This seems to have started happening recently and is affecting project sync operations. The `id` and `name` fields work correctly, but `rootDocumentId` specifically returns undefined.

---
Repository: /testbed
