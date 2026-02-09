# Bug Report

### Describe the bug

The `all()` function for git repositories is returning an incomplete list - it's missing the last repository in the database. When I have multiple git repositories configured, only N-1 repositories are being returned.

### Reproduction

```js
// Setup: Create multiple git repositories
await create({ name: 'repo1', uri: 'https://github.com/user/repo1' });
await create({ name: 'repo2', uri: 'https://github.com/user/repo2' });
await create({ name: 'repo3', uri: 'https://github.com/user/repo3' });

// Try to fetch all repositories
const repos = await all();

// Expected: 3 repositories
// Actual: 2 repositories (last one is missing)
console.log(repos.length); // Shows 2 instead of 3
```

### Expected behavior

The `all()` function should return ALL git repositories from the database, not drop the last one.

### System Info
- Insomnia version: latest
- Platform: macOS

This is causing issues in the UI where the last configured git repository doesn't show up in the list, making it impossible to interact with it.

---
Repository: /testbed
