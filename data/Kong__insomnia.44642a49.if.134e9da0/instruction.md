# Bug Report

### Describe the bug

I'm experiencing an issue with local storage initialization where default values aren't being set correctly when a file doesn't exist. When attempting to read from a non-existent storage file, the default object should be written to the file, but it seems like this is not happening consistently.

### Reproduction

```js
// Try to get a value from storage that doesn't exist yet
const storage = new LocalStorage();
const data = storage.getItem('myKey', { default: 'value' });

// Expected: File should be created with the default object
// Actual: File is not created, default object is not set
```

### Steps to reproduce:
1. Initialize LocalStorage instance
2. Call `getItem()` with a key that doesn't exist in the filesystem
3. Pass a default object as the second parameter
4. Check if the file was created with the default value

### Expected behavior

When a storage file doesn't exist (ENOENT error), the system should create the file and write the provided default object to it. This way, subsequent reads will have the correct default value available.

### Actual behavior

The default object is not being written to the file when it doesn't exist, causing issues with storage initialization.

### System Info
- Insomnia version: latest
- OS: Cross-platform issue

---
Repository: /testbed
