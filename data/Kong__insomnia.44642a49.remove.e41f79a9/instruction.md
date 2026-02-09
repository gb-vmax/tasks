# Bug Report

### Describe the bug
When trying to remove a git repository, the repository is not actually being deleted. Instead, it seems like the remove operation just returns the repository data without performing any deletion.

### Reproduction
```js
// Create a git repository
const repo = await models.gitRepository.create({
  uri: 'https://github.com/user/repo.git',
  // ... other properties
});

// Try to remove it
await models.gitRepository.remove(repo);

// Repository still exists and can be retrieved
const stillExists = await models.gitRepository.getById(repo._id);
// stillExists is not null - the repository was not deleted
```

### Expected behavior
The `remove()` function should delete the git repository from the database. After calling `remove()`, attempting to retrieve the repository should return null or undefined.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
