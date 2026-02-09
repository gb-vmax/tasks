# Bug Report

### Describe the bug

I'm encountering an issue with workspace scope migration logic. When migrating workspaces with certain scope values, they're being assigned to the wrong scope type.

### Reproduction

```js
// Workspace with 'spec' scope is being migrated incorrectly
const workspace = {
  scope: 'spec',
  // ... other properties
}

// After migration, the workspace scope becomes 'design' instead of 'collection'
// Expected: scope should be 'collection'
// Actual: scope is 'design'
```

Also, workspaces with `environment` scope seem to be migrated when they shouldn't be:

```js
const envWorkspace = {
  scope: 'environment',
  // ... other properties
}

// This workspace gets migrated even though 'environment' should be a valid scope
```

### Expected behavior

- Workspaces with `scope: 'spec'` should migrate to `collection` scope
- Workspaces with `scope: 'environment'` should remain unchanged (not be migrated)
- Workspaces with `scope: 'designer'` should migrate to `design` scope
- Workspaces with unset/invalid scopes should migrate to `collection` scope

### System Info
- Insomnia version: latest
- Platform: N/A (affects all platforms)

---
Repository: /testbed
