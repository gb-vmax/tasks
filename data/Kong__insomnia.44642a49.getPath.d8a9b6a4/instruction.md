# Bug Report

### Describe the bug

After a recent update, the `getPath()` method in the plugin context API is not working correctly. When calling `getPath()` multiple times with the same path name, subsequent calls return cached values even when the actual system path might have changed. This is particularly problematic for paths like 'temp' or 'downloads' that users might change during runtime.

### Reproduction

```js
// In a plugin
const path1 = context.app.getPath('downloads');
console.log(path1); // Returns correct path

// User changes downloads folder location in system settings

const path2 = context.app.getPath('downloads');
console.log(path2); // Still returns old cached path instead of new location
```

### Expected behavior

Each call to `getPath()` should return the current system path, not a cached value. If caching is necessary for performance, there should be a way to invalidate the cache or it should have a reasonable TTL.

### Additional context

This is causing issues in plugins that rely on getting the current system paths, especially for file operations. The paths are being cached indefinitely and don't reflect changes made by the user to their system folder locations.

System Info:
- Insomnia version: latest
- OS: Windows 11

---
Repository: /testbed
