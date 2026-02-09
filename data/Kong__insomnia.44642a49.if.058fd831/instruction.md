# Bug Report

### Describe the bug

I'm experiencing an issue with the `withDescendants` function where it's not returning the expected hierarchical data structure. When I try to fetch a document with all its descendants, the function appears to return an empty result or incorrect data.

### Reproduction

```js
const parentDoc = await database.get('parent-id');
const descendants = await database.withDescendants(parentDoc);

// Expected: [parentDoc, child1, child2, grandchild1, ...]
// Actual: Empty array or missing descendants
```

### Steps to reproduce:
1. Create a parent document in the database
2. Create several child documents that reference the parent
3. Call `withDescendants()` on the parent document
4. Observe that descendants are not included in the result

### Expected behavior

The function should return an array containing the parent document and all of its descendants in the hierarchy, stopping at the specified `stopType` if provided. This was working correctly before but now seems to be broken.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
