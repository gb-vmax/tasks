# Bug Report

### Describe the bug

I'm experiencing an issue with the database `remove` function after a recent update. When trying to delete documents, I'm getting unexpected behavior - it seems like the function signature or implementation changed but the removal isn't working as expected.

### Reproduction

```js
const doc = {
  _id: 'test_123',
  type: 'request',
  parentId: 'workspace_1',
  // ... other properties
};

// This used to work but now fails
await database.remove(doc);
```

The code throws an error or doesn't properly remove the document from the database. It looks like there might be a syntax issue in the remove function implementation.

### Expected behavior

The `remove` function should properly delete the document and its descendants from the database without errors. The function should maintain backward compatibility with existing code that calls it with the standard parameters.

### Additional context

This appears to have started happening after recent changes to the database module. The function seems to have duplicate or malformed code that's preventing it from executing correctly.

---
Repository: /testbed
