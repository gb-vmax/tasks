# Bug Report

### Describe the bug

The `getByParentId` function is not returning the correct API spec when querying by workspace ID. It seems like the function is searching by the wrong field, causing it to return incorrect or no results.

### Reproduction

```js
const workspaceId = 'wrk_123456';

// Try to get API spec by parent workspace ID
const apiSpec = getByParentId(workspaceId);

// Returns wrong result or null instead of the API spec for this workspace
console.log(apiSpec); // Expected: API spec with parentId matching workspaceId
```

### Expected behavior

When calling `getByParentId(workspaceId)`, it should return the API spec document where `parentId` matches the provided workspace ID. Currently it's not finding the correct document.

### Additional context

This is affecting the ability to retrieve API specifications associated with specific workspaces. The query seems to be looking up by the wrong field.

---
Repository: /testbed
