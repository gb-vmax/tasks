# Bug Report

### Describe the bug

The `getByParentId` function is returning incorrect results when querying API specs. It appears to be filtering by the wrong field, causing it to return specs that don't actually belong to the specified parent workspace.

### Reproduction

```js
// Create an API spec with a specific workspace ID
const spec = await apiSpec.create({
  parentId: 'workspace_123',
  // ... other properties
});

// Try to retrieve specs by parent ID
const results = await apiSpec.getByParentId('workspace_123');

// Results are empty or contain unexpected specs
console.log(results); // Expected to find the created spec, but doesn't
```

### Expected behavior

When calling `getByParentId('workspace_123')`, it should return all API specs that belong to that workspace. Currently, the query seems to be using the wrong field for filtering, so specs aren't being retrieved correctly.

### Additional context

This is affecting workspace-specific API spec retrieval throughout the application. The function should properly filter specs by their parent workspace ID.

---
Repository: /testbed
