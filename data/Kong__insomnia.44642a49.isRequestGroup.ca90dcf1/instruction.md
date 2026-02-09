# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with request group duplication. The problem seems to be related to how the code handles creating duplicate names and cloning data. When I try to duplicate a request group, the application crashes or behaves unexpectedly.

### Reproduction

```js
// Create a request group
const requestGroup = {
  name: 'My API Group',
  parentId: 'workspace_123',
  environment: { apiKey: 'secret' },
  // ... other properties
}

// Try to duplicate it
await duplicate(requestGroup)
// Application crashes or throws an error
```

### Expected behavior

The request group should be duplicated successfully with a name like "My API Group (Copy)" and all the data should be properly cloned.

### Additional context

This was working fine before the recent changes. It looks like some of the core functions that the duplicate operation depends on might have been removed or refactored, causing the duplication feature to break completely.

---
Repository: /testbed
