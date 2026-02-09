# Bug Report

### Describe the bug

After a recent update, I'm getting a runtime error when trying to access remote repository information. The application crashes with `TypeError: this.getRemoteOriginURI is not a function` when performing git sync operations.

### Reproduction

```js
const gitVCS = new GitVCS();
// ... initialize gitVCS with repository

// This throws an error
const remoteURI = await gitVCS.getRemoteOriginURI();
```

The error occurs when:
1. Opening a project that uses git sync
2. Attempting to push/pull changes to/from remote
3. Any operation that tries to retrieve the remote origin URL

### Expected behavior

The `getRemoteOriginURI()` method should return the remote origin URL from the git config, or fall back to the base URI if the config value is not available.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we can't sync with remote repositories anymore. Any help would be appreciated!

---
Repository: /testbed
