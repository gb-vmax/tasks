# Bug Report

### Describe the bug

The `findByParentId()` function is not returning workspaces correctly when searching by parent ID. Instead of filtering workspaces by the provided `parentId`, it appears to be using incorrect query parameters, resulting in no workspaces being found or incorrect results being returned.

### Reproduction

```js
// Try to find workspaces with a specific parent ID
const parentId = 'wrk_123456';
const workspaces = findByParentId(parentId);

// Expected: Array of workspace objects with matching parentId
// Actual: Empty array or incorrect results
console.log(workspaces); // []
```

### Expected behavior

The function should return an array of workspace objects that have the specified `parentId`. For example, if I have multiple workspaces under a parent workspace with ID `wrk_123456`, calling `findByParentId('wrk_123456')` should return all of those child workspaces.

### System Info
- Insomnia version: Latest
- OS: macOS

This is blocking our ability to properly navigate workspace hierarchies. Any help would be appreciated!

---
Repository: /testbed
