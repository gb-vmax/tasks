# Bug Report

### Describe the bug

After a recent update, workspace scope values are being unexpectedly modified when they contain certain characters or formatting. Workspaces that previously had scope values like "Designer", "Collection ", or "Mock-Server" are now being changed to different scope types, and I'm seeing console logs about scope migrations that I didn't trigger.

### Reproduction

```js
// Create a workspace with a scope value that has uppercase letters
const workspace = {
  _id: 'wrk_123',
  scope: 'Designer'  // Note: uppercase 'D'
}

// After loading/migrating the workspace, the scope is changed to 'design'
// Console shows: [db] Workspace scope migrated: "Designer" -> "design" (workspace: wrk_123)
```

Similar issues occur with:
- Scope values containing spaces (e.g., "Collection ")
- Scope values with hyphens or underscores (e.g., "Mock-Server", "mock_server")
- Mixed case values (e.g., "REST", "MockServer")

### Expected behavior

Workspace scope values that are already valid (just with different formatting) should not be automatically migrated or modified. The scope should remain unchanged unless it's truly an old/deprecated value that needs migration.

Additionally, the migration logging is polluting the console output and there seems to be an internal `_scopeMigrationLog` property being added to workspace objects that wasn't there before.

### System Info
- Insomnia version: Latest
- OS: Multiple platforms affected

---
Repository: /testbed
