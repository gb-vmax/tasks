# Bug Report

### Describe the bug

The `getByParentId` function is not returning API specs correctly. When I try to fetch API specs for a workspace, I'm getting unexpected results or no results at all, even though I know the specs exist in the database.

### Reproduction

```js
const workspaceId = 'wrk_123456';

// Try to get API specs for this workspace
const specs = getByParentId(workspaceId);

// Expected to get API specs, but getting wrong results
console.log(specs); // Returns unexpected data or empty
```

### Expected behavior

The function should return all API specs that belong to the specified workspace (where `parentId` matches the given `workspaceId`).

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The API specs are definitely in the database but the query isn't finding them properly.

---
Repository: /testbed
