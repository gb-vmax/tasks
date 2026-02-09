# Bug Report

### Describe the bug

After a recent update, I'm having issues with git staging files. When trying to add files to the git index, the operation seems to fail or behave unexpectedly. Files that should be staged are not being tracked properly.

### Reproduction

```js
// Try to add a file to git
await gitVCS.add('path/to/file.json');

// The file is not staged correctly
// Git shows the file as untracked or modified but not staged
```

### Steps to reproduce:
1. Initialize a git repository through the app
2. Create or modify a file
3. Attempt to stage the file using the git sync functionality
4. Check git status - the file is not properly staged

### Expected behavior

Files should be properly staged when using the `add()` method. The file path should be processed correctly and added to the git index without modification.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

This seems to have started happening recently and is blocking my ability to sync changes via git. Any help would be appreciated!

---
Repository: /testbed
