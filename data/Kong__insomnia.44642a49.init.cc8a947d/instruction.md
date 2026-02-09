# Bug Report

### Describe the bug

When initializing a Git repository, the logic appears to be inverted - the system tries to initialize a new repo when one already exists, and opens an existing repo when it doesn't exist. This causes issues when working with Git sync functionality.

### Reproduction

1. Start with a directory that already has a Git repository initialized
2. Call the Git VCS init method with that directory
3. The system attempts to initialize a new repository instead of opening the existing one
4. Console logs show "Initialized repo" message when it should show "Opened repo"

Alternatively:
1. Start with a fresh directory without any Git repository
2. Call the Git VCS init method
3. The system tries to open a non-existent repo instead of initializing a new one
4. Console logs show "Opened repo" message when it should show "Initialized repo"

### Expected behavior

- When a Git repository already exists in the directory, the system should open it and log "Opened repo for {gitDirectory}"
- When no Git repository exists, the system should initialize a new one and log "Initialized repo in {gitDirectory}"

The behavior seems backwards from what it should be.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
