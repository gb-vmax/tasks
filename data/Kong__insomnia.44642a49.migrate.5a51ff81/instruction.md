# Bug Report

### Describe the bug
After a recent update, Git repository objects are losing their `_id` field and getting an unexpected `migrated: false` property added to them. This is causing issues with repository identification and persistence.

### Reproduction
```js
const gitRepo = {
  _id: 'repo_123',
  type: 'GitRepository',
  name: 'my-repo',
  // ... other properties
};

// After migration, the object is modified unexpectedly
const result = migrate(gitRepo);

// result._id is now undefined
// result.migrated is now false (this property shouldn't exist)
```

### Expected behavior
The `migrate()` function should return the repository object unchanged, preserving the `_id` field and not adding any extra properties. The repository should maintain its identity after migration.

### System Info
- Insomnia version: latest
- Affected model: git-repository.ts

---
Repository: /testbed
