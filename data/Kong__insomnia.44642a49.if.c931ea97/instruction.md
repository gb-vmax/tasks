# Bug Report

### Describe the bug

After a recent update, branch creation seems to be stuck in an infinite loop. The application hangs and becomes unresponsive when trying to create or switch to a new branch.

### Reproduction

```js
// Try to create a new branch
await vcs._getOrCreateBranch('feature-branch');

// Application hangs here and never returns
```

The issue happens consistently when:
1. Creating a new branch that doesn't exist yet
2. The branch name gets normalized (e.g., converted to lowercase)
3. The system tries to store the new branch

### Expected behavior

The branch should be created successfully and the method should return the newly created branch object without hanging or causing infinite recursion.

### System Info
- Version: Latest
- Environment: Node.js

This is blocking our workflow as we can't create any new branches anymore. Any help would be appreciated!

---
Repository: /testbed
