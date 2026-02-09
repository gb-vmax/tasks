# Bug Report

### Describe the bug

I'm encountering an issue where creating or retrieving branches fails with an error message even when a valid branch name is provided. The error says "No branch name specified for get-or-create operation" but I'm definitely passing a branch name.

### Reproduction

```js
// Trying to get or create a branch with a valid name
const branchName = 'feature/new-feature';
await vcs._getOrCreateBranch(branchName);

// Error thrown: "No branch name specified for get-or-create operation"
```

This happens every time I try to work with branches. The operation fails immediately even though I'm providing a non-empty string as the branch name.

### Expected behavior

The method should successfully retrieve an existing branch or create a new one when a valid branch name is provided. It should only throw the error when the branch name is actually empty, null, or undefined.

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
