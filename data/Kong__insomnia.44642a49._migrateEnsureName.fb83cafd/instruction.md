# Bug Report

### Describe the bug

I'm experiencing an issue where workspaces without a name are not getting the default "My Workspace" name assigned correctly. It seems like the name migration logic is broken - workspaces that should be getting a default name are keeping their invalid name values instead.

### Reproduction

```js
// Create a workspace with an invalid name (not a string)
const workspace = {
  _id: 'wrk_123',
  name: null,
  // ... other properties
}

// After migration, the workspace still has null as name
// Expected: name should be 'My Workspace'
// Actual: name remains null
```

### Steps to reproduce
1. Create or import a workspace that has a non-string name value (null, undefined, number, etc.)
2. The workspace should get migrated with a default name
3. Instead, the invalid name persists

### Expected behavior

Workspaces with invalid (non-string) name values should automatically get assigned the default name "My Workspace" during migration.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when displaying workspace lists since we expect all workspaces to have valid string names.

---
Repository: /testbed
