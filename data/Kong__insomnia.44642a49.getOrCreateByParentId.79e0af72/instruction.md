# Bug Report

### Describe the bug

When trying to create a new workspace meta for a workspace that doesn't have one yet, the application crashes with a "Cannot read properties of null" error. This happens when calling `getOrCreateByParentId()` with a valid parent ID.

### Reproduction

```js
// Try to get or create workspace meta for a new workspace
const workspaceMeta = await getOrCreateByParentId('wrk_123456');
// Error: Cannot read properties of null (reading 'parentId')
```

### Steps to reproduce:
1. Create a new workspace without existing meta
2. Call `getOrCreateByParentId()` with the workspace ID
3. Application crashes instead of creating new meta

### Expected behavior

The function should create a new workspace meta document with the provided `parentId` when one doesn't exist yet. It should not throw an error.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
