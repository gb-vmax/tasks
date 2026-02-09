# Bug Report

### Describe the bug

When calling `withDescendants()` on a database document, the function returns immediately without actually fetching any descendants. The method appears to be exiting early and not processing the document hierarchy as expected.

### Reproduction

```js
const workspace = await models.workspace.getById(workspaceId);
const descendants = await database.withDescendants(workspace);

// Expected: Array containing workspace and all its child documents
// Actual: Empty array or incomplete results
```

Steps to reproduce:
1. Get a database document that has child documents
2. Call `database.withDescendants()` with the document
3. Observe that descendants are not included in the returned array

### Expected behavior

The function should return an array containing the document itself plus all its descendants in the hierarchy, stopping at the specified `stopType` if provided.

### System Info

- Insomnia version: latest
- Platform: All platforms affected

This seems to have started happening recently. The function is returning prematurely instead of traversing the document tree.

---
Repository: /testbed
