# Bug Report

### Describe the bug

Git repository initialization is not working properly. When trying to initialize a new git repository, the operation is being skipped and the "Opened repo" message is shown instead of "Initialized repo", even though no repository exists yet.

### Reproduction

1. Set up a new project directory without an existing git repository
2. Call the git init function with the directory path
3. Observe that the repository is not actually initialized
4. The console shows "Opened repo" message instead of "Initialized repo"

### Expected behavior

When `repoExists()` returns `false` (no existing repository), the code should:
1. Log "Initialized repo in {gitDirectory}"
2. Fetch the default branch from remote origin
3. Initialize the repository with the detected default branch

Instead, it appears the logic is inverted and the initialization only happens when a repo already exists.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
