# Bug Report

### Describe the bug

After a recent update, the VCS branch creation/retrieval functionality appears to be broken. When trying to get or create a branch, the application hangs or enters an infinite loop and becomes unresponsive.

### Reproduction

```js
const vcs = new VCS();

// This call never returns and causes the app to hang
await vcs._getOrCreateBranch('feature-branch');
```

### Expected behavior

The method should either return an existing branch or create a new one and return it without hanging. The operation should complete in a reasonable amount of time.

### Additional context

This seems to have started happening recently. The branch name normalization is working (converting to lowercase and trimming), but something in the flow is causing the process to never complete. I've tried with different branch names but the result is always the same - the application becomes unresponsive.

---
Repository: /testbed
