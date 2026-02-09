# Bug Report

### Describe the bug

When using the plugin data context with an empty string as `activeProjectId`, the function returns `undefined` instead of fetching workspaces. This breaks plugins that rely on workspace data when the project ID is an empty string.

### Reproduction

```js
// When activeProjectId is an empty string
const workspaces = await getWorkspaces('');

// Expected: Should return all workspaces or workspaces for the project
// Actual: Returns undefined
```

### Expected behavior

The function should handle empty string `activeProjectId` the same way it handles `undefined` or `null` - by returning all workspaces. Currently it falls through to the else branch but doesn't execute the `findAll()` call, resulting in `undefined` being returned.

### Steps to reproduce

1. Call `getWorkspaces()` with an empty string parameter
2. Observe that no workspaces are returned (undefined)
3. This affects any plugin trying to access workspace data when the project ID happens to be an empty string

### System Info

- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
