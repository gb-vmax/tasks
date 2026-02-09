# Bug Report

### Describe the bug

After a recent update, the plugin data context is broken and throwing errors when trying to access workspace data. The `getWorkspaces` function appears to be defined twice in the same scope, causing a syntax error that prevents the plugin system from loading properly.

### Reproduction

```js
// Try to use any plugin that accesses workspace data
const data = context.data;
const workspaces = data.getWorkspaces(projectId);
// This will fail with a syntax error
```

### Expected behavior

The `getWorkspaces` function should work correctly and return the list of workspaces for the given project ID. Plugins should be able to access workspace data without errors.

### System Info
- Insomnia version: latest
- OS: All platforms affected

This seems to have been introduced in a recent commit. The code won't even parse correctly due to the duplicate function definition.

---
Repository: /testbed
