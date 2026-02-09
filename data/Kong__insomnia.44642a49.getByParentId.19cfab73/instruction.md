# Bug Report

### Describe the bug

The `getByParentId` function is now returning specs in a different order than before. After a recent update, API specs are being sorted by modification time in descending order (newest first), but our application expects them in the original database order or sorted by creation time.

### Reproduction

```js
// Fetch API specs for a workspace
const specs = await getByParentId(workspaceId);

// Expected: specs in database order or sorted by creation time
// Actual: specs sorted by modification time (newest first)
```

When retrieving multiple API specs for a workspace, they now appear in reverse chronological order by modification date. This breaks existing functionality that relies on the previous ordering behavior.

### Expected behavior

The function should return API specs in their original order (as stored in the database) or allow explicit control over sorting behavior. The default behavior shouldn't automatically sort by modification time.

### Additional context

This seems to have changed recently. Previously, calling `getByParentId` would return specs in the order they were stored/created, but now they're automatically sorted by the `modified` timestamp in descending order.

---
Repository: /testbed
