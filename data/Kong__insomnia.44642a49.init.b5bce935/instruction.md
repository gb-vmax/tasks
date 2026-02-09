# Bug Report

### Describe the bug

Git repository initialization is not working correctly. When trying to open an existing repository, the code tries to initialize a new one instead, and when trying to initialize a new repository, it just opens the existing one. The behavior seems completely inverted.

### Reproduction

```js
// Case 1: Existing repository
const gitVCS = new GitVCS();
await gitVCS.init({
  directory: '/path/to/existing/repo',
  fs: fsModule,
  gitDirectory: '/path/to/existing/repo/.git',
  gitCredentials: credentials,
  repoId: 'test-repo'
});

// Expected: Console logs "[git] Opened repo for /path/to/existing/repo/.git"
// Actual: Console logs "[git] Initialized repo in /path/to/existing/repo/.git"
// And attempts to run git.init() on an already existing repository

// Case 2: New repository (non-existent)
const gitVCS2 = new GitVCS();
await gitVCS2.init({
  directory: '/path/to/new/repo',
  fs: fsModule,
  gitDirectory: '/path/to/new/repo/.git',
  gitCredentials: credentials,
  repoId: 'new-repo'
});

// Expected: Console logs "[git] Initialized repo in /path/to/new/repo/.git"
// Actual: Console logs "[git] Opened repo for /path/to/new/repo/.git"
// And does NOT initialize the repository
```

### Expected behavior

- When a repository exists, it should be opened (not initialized)
- When a repository doesn't exist, it should be initialized (not just opened)
- The console logs should match the actual operation being performed

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
