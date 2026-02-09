# Bug Report

### Describe the bug

After a recent update, the `app.getPath()` plugin API method is broken. When calling `app.getPath('desktop')` or any other standard path name, it throws an error about the path being unknown.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const desktopPath = context.app.getPath('desktop');
    console.log(desktopPath);
  }
];
```

This code used to work fine but now throws:
```
Error: Unknown path name desktop
```

### Expected behavior

The method should return the desktop path like it did before. Standard path names like 'desktop', 'documents', 'downloads', etc. should be recognized and return the appropriate system paths.

### Additional context

This seems to have broken after some changes to the app context. The error message suggests the path name isn't being recognized even though 'desktop' is a valid option that was working previously.

---
Repository: /testbed
