# Bug Report

### Describe the bug

Workspace scope migration is not working correctly. When loading workspaces with certain scope values, they are being assigned the wrong scope type after migration.

### Reproduction

```js
// Create a workspace with an unset or null scope
const workspace = {
  _id: 'wrk_123',
  name: 'My Workspace',
  scope: null // or undefined
}

// After migration, the workspace gets assigned 'design' scope
// but it should be 'collection'
```

Also affects workspaces with 'designer' or 'spec' scope values - they are now being migrated to 'collection' instead of 'design'.

### Expected behavior

- Workspaces with `scope: 'designer'` or `scope: 'spec'` should migrate to `WorkspaceScopeKeys.design`
- Workspaces with unset/null scope should migrate to `WorkspaceScopeKeys.collection`

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken after a recent update. My existing workspaces are now showing up with incorrect types.

---
Repository: /testbed
