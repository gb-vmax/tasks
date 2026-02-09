# Bug Report

### Describe the bug

When creating or loading workspaces, the workspace name is being incorrectly set to 'My Workspace' even when a valid name already exists. This appears to be overwriting existing workspace names unexpectedly.

### Reproduction

```js
const workspace = {
  name: 'My Custom Workspace',
  // ... other properties
}

// After migration/processing
// workspace.name is now 'My Workspace' instead of 'My Custom Workspace'
```

### Expected behavior

The workspace name should only be set to the default 'My Workspace' when the name is missing, undefined, or not a string. Valid existing workspace names should be preserved.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
