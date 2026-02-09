# Bug Report

### Describe the bug

Workspace scope migration is not working correctly. When migrating old workspace scopes, workspaces with `scope` set to `'designer'` or `'spec'` are being assigned the wrong scope value.

### Reproduction

```js
const workspace = {
  scope: 'designer',
  // ... other workspace properties
};

const migrated = _migrateScope(workspace);
console.log(migrated.scope); // Expected: 'design', but getting 'collection'
```

Similarly for workspaces with `scope: 'spec'`:

```js
const workspace = {
  scope: 'spec',
  // ... other workspace properties
};

const migrated = _migrateScope(workspace);
console.log(migrated.scope); // Expected: 'design', but getting 'collection'
```

### Expected behavior

- Workspaces with scope `'designer'` should be migrated to `WorkspaceScopeKeys.design`
- Workspaces with scope `'spec'` should be migrated to `WorkspaceScopeKeys.design`
- Other unset/unknown scopes should default to `WorkspaceScopeKeys.collection`

### Additional context

This appears to have started happening recently. The migration logic seems to be assigning the opposite scope values - old designer/spec workspaces are becoming collections when they should become design workspaces.

---
Repository: /testbed
