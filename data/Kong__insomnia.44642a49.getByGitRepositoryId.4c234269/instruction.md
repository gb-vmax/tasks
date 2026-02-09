# Bug Report

### Describe the bug

After a recent update, the `getByGitRepositoryId` function is now returning an array of workspace metadata objects instead of a single object. This is breaking existing code that expects a single result.

### Reproduction

```js
// This used to return a single WorkspaceMeta object
const meta = await getByGitRepositoryId('repo-123');

// Now it returns an array, causing errors when trying to access properties
console.log(meta.parentId); // TypeError: Cannot read property 'parentId' of undefined
```

The function signature changed but there's no indication in the code that it now returns an array. Code that was working before is now failing because it's trying to access properties on what it expects to be an object, but is actually an array.

### Expected behavior

The function should either:
1. Continue returning a single WorkspaceMeta object like before, or
2. Be renamed to indicate it returns multiple results (e.g., `getAllByGitRepositoryId`)

### System Info
- Version: Latest from main branch
- Node: 18.x

---
Repository: /testbed
