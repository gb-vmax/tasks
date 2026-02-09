# Bug Report

### Describe the bug

I'm experiencing an issue with the `removeWhere` function in the database module. It appears that the function signature has been corrupted or incomplete, causing the code to fail when trying to remove documents from the database.

### Reproduction

```js
// Attempting to remove documents using removeWhere
await database.removeWhere('request', { workspaceId: 'some-id' });
```

When calling `removeWhere`, the application crashes or behaves unexpectedly. It seems like the function definition got mangled - there's code that looks like it's defining a helper function `_getDescendantsWithDepth` but it's placed in the wrong location, breaking the original `removeWhere` function structure.

### Expected behavior

The `removeWhere` function should properly remove documents matching the query without errors. The function should maintain its original structure and be callable with the standard parameters.

### Additional context

Looking at the code, it appears that:
1. The original simple implementation that checked `db._empty` and called `_send` has been disrupted
2. There's a helper function definition that seems to be inserted in the middle of the `removeWhere` function
3. The function signature appears incomplete or cut off

This is preventing any document removal operations from working correctly in the application.

---
Repository: /testbed
