# Bug Report

### Describe the bug

I'm experiencing an issue with the `withAncestors` function where it's not returning the expected ancestor hierarchy for database documents. When I try to fetch a document with its ancestors, I'm getting an empty array instead of the full chain of parent documents.

### Reproduction

```js
const workspace = await database.getById('wrk_123');
const ancestors = await database.withAncestors(workspace);

// Expected: [workspace, parentFolder, rootWorkspace]
// Actual: []
```

This seems to happen when the database is not empty. The function returns an empty array even though the document clearly has parent documents in the hierarchy.

### Expected behavior

The `withAncestors` function should return an array containing the document itself along with all its ancestor documents in the hierarchy, regardless of whether the database is empty or not.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
