# Bug Report

### Describe the bug

Git repository initialization is failing when trying to create test fixtures. The Git class constructor appears to be rejecting successful git operations, causing the initialization process to throw errors unexpectedly.

### Reproduction

```js
// Attempting to initialize a Git instance
const testDir = '/path/to/test/directory';
const git = new Git(testDir);
// Throws: "git init exited with code 0"
```

When creating a new Git instance with a valid directory, the constructor throws an error even though the git command executes successfully (exit code 0).

### Expected behavior

The Git class should successfully initialize a repository when `git init` returns exit code 0 (success). The constructor should only throw an error when git commands actually fail (non-zero exit codes).

### Additional context

This is blocking our ability to set up test environments that require git repositories. The error message also seems to have some typos in the stderr/stdout labels.

---
Repository: /testbed
