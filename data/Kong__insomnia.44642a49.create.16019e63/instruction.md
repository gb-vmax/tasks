# Bug Report

### Describe the bug

I'm encountering an issue when trying to create a new WorkspaceMeta object. The creation fails with an error message saying "New WorkspaceMeta missing parentId" even when I'm providing a valid `parentId` in the patch object.

### Reproduction

```js
import * as workspaceMeta from './workspace-meta';

// This throws an error but shouldn't
const meta = workspaceMeta.create({
  parentId: 'wrk_123456',
  // other properties...
});
```

The error message I get is:
```
Error: New WorkspaceMeta missing parentId {"parentId":"wrk_123456",...}
```

### Expected behavior

When calling `create()` with a `parentId` in the patch object, it should successfully create the WorkspaceMeta without throwing an error. The `parentId` is clearly present in the object but the validation is rejecting it.

Also, it seems like the created WorkspaceMeta object is empty and doesn't include any of the properties I passed in the patch parameter, which is unexpected.

### Additional context

This appears to have started happening recently. Previously, creating workspace metadata with a parentId worked fine. Now it's blocking me from creating new workspaces entirely.

---
Repository: /testbed
