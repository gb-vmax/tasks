# Bug Report

### Describe the bug

The `all()` function in git-repository is only returning a single repository instead of all repositories. When I have multiple git repositories configured, only the first one is being returned.

### Reproduction

```js
// Set up multiple git repositories
const repo1 = await gitRepository.create({ uri: 'https://github.com/user/repo1.git' });
const repo2 = await gitRepository.create({ uri: 'https://github.com/user/repo2.git' });

// Try to get all repositories
const allRepos = await gitRepository.all();

// Expected: array with both repos
// Actual: only returns repo1
console.log(allRepos); // Only shows the first repository
```

### Expected behavior

The `all()` method should return an array containing all git repositories, not just the first one.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
