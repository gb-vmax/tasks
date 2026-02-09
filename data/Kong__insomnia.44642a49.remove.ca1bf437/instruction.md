# Bug Report

### Describe the bug

I'm experiencing an issue with git repository removal. When trying to remove a git repository, the operation doesn't work as expected and the repository data remains in the database.

### Reproduction

```js
const repo = await models.gitRepository.create({
  _id: 'git_abc123',
  uri: 'https://github.com/user/repo.git',
  // ... other properties
});

// Try to remove the repository
await models.gitRepository.remove(repo);

// Repository still exists in database
const allRepos = await models.gitRepository.all();
console.log(allRepos); // Still contains the "removed" repository
```

### Expected behavior

The `remove()` function should completely delete the git repository from the database. After calling `remove()`, the repository should no longer appear when querying all repositories.

### Additional context

This seems to have broken recently. The remove operation completes without errors, but the repository persists in the database. Other CRUD operations (create, update, etc.) appear to be working fine.

---
Repository: /testbed
