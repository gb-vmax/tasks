# Bug Report

### Describe the bug

When creating a new WorkspaceMeta object, the `patch` parameter passed to the `create()` function is being ignored. All the properties from the patch (including `parentId`) are not being applied to the created document, which means the WorkspaceMeta is created with default/empty values instead of the provided configuration.

### Reproduction

```js
const workspaceMeta = await models.workspaceMeta.create({
  parentId: 'wrk_123',
  activeRequestId: 'req_456',
  activeEnvironmentId: 'env_789'
});

// The created workspaceMeta doesn't have the expected properties
console.log(workspaceMeta.parentId); // undefined or default value
console.log(workspaceMeta.activeRequestId); // undefined or default value
console.log(workspaceMeta.activeEnvironmentId); // undefined or default value
```

### Expected behavior

The `create()` function should apply all properties from the `patch` parameter to the newly created WorkspaceMeta document. The created object should contain `parentId`, `activeRequestId`, `activeEnvironmentId`, and any other properties passed in the patch.

### Additional context

This appears to be a regression - the function validates that `parentId` exists in the patch but then doesn't actually use the patch when creating the document. This breaks any code that relies on initializing WorkspaceMeta with specific values.

---
Repository: /testbed
