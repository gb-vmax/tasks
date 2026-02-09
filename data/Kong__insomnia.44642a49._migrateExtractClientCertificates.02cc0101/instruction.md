# Bug Report

### Describe the bug

When loading a workspace that has already been migrated (i.e., `certificates` is `null` or not an array), the workspace data gets corrupted. The `certificates` property is being deleted even though the migration should only run for workspaces that haven't been migrated yet.

### Reproduction

```js
const workspace = {
  _id: 'wrk_123',
  name: 'My Workspace',
  certificates: null, // Already migrated
  // ... other properties
}

// Load the workspace
// Expected: workspace remains unchanged
// Actual: certificates property gets deleted and workspace data is corrupted
```

### Steps to reproduce

1. Create a workspace with `certificates: null` (already migrated state)
2. Load/open the workspace
3. The migration function runs incorrectly
4. Workspace data becomes corrupted

### Expected behavior

The migration should only run for workspaces that have NOT been migrated yet (when `certificates` is still an array). Workspaces that have already been migrated (where `certificates` is `null` or not an array) should be left untouched.

### Additional context

This seems to affect workspaces that were previously migrated. The logic appears to be inverted - it's running the migration on already-migrated workspaces instead of skipping them.

---
Repository: /testbed
