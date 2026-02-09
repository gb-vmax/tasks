# Bug Report

### Describe the bug

Git repository initialization logic appears to be inverted. When opening an existing repository, the console logs "Initialized repo" instead of "Opened repo", and vice versa. Additionally, when initializing a new repository, the code attempts to fetch the remote origin URL but the variable is not defined, which likely causes the initialization to always fall back to the default 'main' branch instead of using the remote's default branch.

### Reproduction

```js
// Scenario 1: Opening an existing repo
const vcs = new GitVCS();
await vcs.init({
  directory: '/path/to/existing/repo',
  fs: fsClient,
  gitDirectory: '/path/to/existing/repo/.git',
  gitCredentials: credentials,
  uri: 'https://github.com/user/repo.git',
  repoId: 'some-id'
});
// Console shows: "[git] Initialized repo in /path/to/existing/repo/.git"
// Expected: "[git] Opened repo for /path/to/existing/repo/.git"

// Scenario 2: Creating a new repo with a remote that uses 'master' as default
const vcs2 = new GitVCS();
await vcs2.init({
  directory: '/path/to/new/repo',
  fs: fsClient,
  gitDirectory: '/path/to/new/repo/.git',
  gitCredentials: credentials,
  uri: 'https://github.com/user/legacy-repo.git',
  repoId: 'another-id'
});
// The repo is initialized with 'main' branch instead of 'master'
// (the remote's actual default branch)
```

### Expected behavior

1. When opening an existing repository, it should log "Opened repo for..." 
2. When initializing a new repository, it should log "Initialized repo in..."
3. When initializing a new repository with a remote URL, it should detect and use the remote's default branch name

### System Info
- Insomnia version: latest
- OS: macOS/Windows/Linux

---
Repository: /testbed
