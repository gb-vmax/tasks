# Bug Report

### Describe the bug

When trying to remove a Git repository, the operation doesn't actually delete the repository from the database. The repository remains in the system even after calling the remove function.

### Reproduction

```js
const repo = await gitRepository.create({
  name: 'test-repo',
  uri: 'https://github.com/user/repo.git'
});

// Try to remove the repository
await gitRepository.remove(repo);

// Repository is still accessible
const allRepos = await gitRepository.all();
console.log(allRepos); // Still contains the "removed" repository
```

### Expected behavior

The repository should be completely removed from the database after calling `remove()`. Subsequent calls to `all()` should not include the removed repository.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
