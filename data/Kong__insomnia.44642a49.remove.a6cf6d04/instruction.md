# Bug Report

### Describe the bug

When trying to remove a Git repository, the operation fails silently if the repository object passed to the `remove()` function is not the exact same instance that exists in the database. This causes repositories to remain in the system even after attempting to delete them.

### Reproduction

```js
// Get a repository from somewhere (e.g., API response, state management)
const repo = {
  _id: 'repo_123',
  type: 'GitRepository',
  // ... other properties
}

// Try to remove it
await remove(repo)

// Repository is still in the database
const stillExists = db.get(repo._id) // Returns the repository
```

### Expected behavior

The repository should be successfully removed from the database regardless of whether the passed object is the exact instance stored in the database, as long as it has the correct identifier.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
