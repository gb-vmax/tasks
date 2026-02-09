# Bug Report

### Describe the bug

When using the plugin API's `data.import.raw()` method to import workspace data, the import silently fails when a workspace with the same name and ID already exists in the project. The method returns without any indication of what happened or why the import didn't complete.

### Reproduction

```js
// In a plugin
const content = JSON.stringify({
  resources: [
    {
      _type: 'workspace',
      _id: 'wrk_123',
      name: 'My Workspace'
    }
  ]
});

// First import works fine
await context.data.import.raw(content);

// Second import with same workspace silently does nothing
await context.data.import.raw(content);
// No error thrown, no feedback provided
```

### Expected behavior

The import should either:
1. Complete successfully and update/merge the existing workspace, OR
2. Throw an error explaining that a duplicate workspace exists, OR
3. Return some indication that the import was skipped

Currently it just silently returns without importing anything, which makes it very difficult to debug import issues in plugins.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
