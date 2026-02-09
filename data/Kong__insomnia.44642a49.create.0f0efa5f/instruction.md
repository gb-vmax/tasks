# Bug Report

### Describe the bug

When creating a new workspace, I'm getting an error because the parent validation is happening at the wrong time. The `expectParentToBeProject` function is being called with the entire workspace object instead of just the `parentId`, which causes type mismatches and validation failures.

### Reproduction

```js
// Try to create a workspace with a parent ID
const workspace = await create({
  parentId: 'some-project-id',
  name: 'My Workspace'
});
```

The creation fails because the validation function expects a string (parentId) but receives the full workspace object after creation.

### Expected behavior

The workspace should be created successfully and the parent validation should work correctly by checking the `parentId` field.

### Additional context

This seems to have broken after a recent change to the workspace creation flow. The validation logic appears to be receiving the wrong parameter type.

---
Repository: /testbed
