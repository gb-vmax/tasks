# Bug Report

### Describe the bug

I'm experiencing an issue where git repositories aren't being properly removed from the database. When I try to delete a git repository, it appears to succeed but the repository is still present in the database afterward.

### Reproduction

```js
// Create and save a git repository
const repo = await models.gitRepository.create({
  _id: 'test-repo-id',
  uri: 'https://github.com/test/repo.git'
});

// Try to remove it
await models.gitRepository.remove(repo);

// Check if it still exists
const allRepos = await models.gitRepository.all();
// The repository is still in the list!
```

### Expected behavior

After calling `remove()` on a git repository, it should be completely removed from the database and no longer appear in queries. The repository should not be accessible via `all()` or any other lookup methods.

### Additional context

This seems to have started happening recently. The remove function returns successfully but doesn't actually delete the repository from the underlying database. I've verified that the repository object being passed to `remove()` is valid and exists in the database before the call.

---
Repository: /testbed
