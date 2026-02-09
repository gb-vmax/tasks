# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with git status not reflecting real-time changes to files. It seems like the status is being cached and doesn't update immediately when files are modified or staged.

### Reproduction

```js
// Modify a file
await writeFile('test.json', newContent);

// Check status - shows old status
const status1 = await gitVcs.status('test.json');

// Modify again
await writeFile('test.json', anotherContent);

// Check status again - still shows cached status from before
const status2 = await gitVcs.status('test.json');
```

The status appears to be cached for a period of time (looks like 2 seconds?) and doesn't reflect actual changes to the file system until the cache expires.

### Expected behavior

The `status()` method should always return the current, real-time git status of a file. If a file is modified, staged, or committed, the status should immediately reflect those changes when queried.

### Additional context

This is particularly problematic when:
1. Making rapid changes to files
2. Staging files and then immediately checking their status
3. Running automated workflows that depend on accurate git status

The caching behavior causes the UI to show stale information and can lead to confusion about the actual state of files in the repository.

---
Repository: /testbed
