# Bug Report

### Describe the bug

When trying to remove files from git using the `remove()` method, I'm getting an error. It seems like the file path isn't being passed correctly to the underlying git library.

### Reproduction

```js
const gitVcs = new GitVCS();
await gitVcs.remove('path/to/file.txt');
```

When calling the remove method, the operation fails because the git library doesn't recognize the parameter being passed.

### Expected behavior

The file should be removed from git staging without errors. The remove operation should work the same way as the add operation does.

### Additional context

This appears to have started happening recently. The add() method works fine with the same type of file paths, so I'm not sure why remove() is having issues.

---
Repository: /testbed
