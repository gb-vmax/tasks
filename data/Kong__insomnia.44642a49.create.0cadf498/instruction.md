# Bug Report

### Describe the bug

I'm unable to create a new WorkspaceMeta object without getting an error. When I try to create a WorkspaceMeta with a valid `parentId`, the system throws an error saying "New WorkspaceMeta missing parentId".

### Reproduction

```js
import { create } from './workspace-meta';

// This throws an error even though parentId is provided
const workspaceMeta = create({
  parentId: 'wrk_123456789'
});

// Error: New WorkspaceMeta missing parentId {"parentId":"wrk_123456789"}
```

### Expected behavior

Creating a WorkspaceMeta with a `parentId` should work without throwing an error. The error should only be thrown when `parentId` is actually missing or undefined.

### Additional context

This seems to have broken recently - I was able to create workspace metadata objects before without any issues. Now every attempt to create one with a parentId fails with this confusing error message.

---
Repository: /testbed
