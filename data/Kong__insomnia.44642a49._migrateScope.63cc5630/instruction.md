# Bug Report

### Describe the bug

I'm experiencing an issue with workspace scope migration. When I have a workspace with scope set to `'designer'`, it's not being migrated to the `design` scope as expected. Instead, it's being converted to `collection` scope.

### Reproduction

```js
const workspace = {
  scope: 'designer',
  // ... other workspace properties
}

// After migration, scope is incorrectly set to 'collection'
// Expected: scope should be 'design'
```

### Steps to reproduce:
1. Create or load a workspace with `scope: 'designer'`
2. The migration logic runs
3. Workspace scope gets set to `'collection'` instead of `'design'`

### Expected behavior

Workspaces with legacy scope values `'designer'` or `'spec'` should be migrated to `WorkspaceScopeKeys.design`. Currently, only workspaces that somehow have BOTH `'designer'` AND `'spec'` as their scope value (which seems impossible) would be migrated to `design`, while all others default to `collection`.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
