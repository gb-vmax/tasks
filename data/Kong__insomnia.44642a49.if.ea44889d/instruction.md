# Bug Report

### Describe the bug

When trying to access local storage data that doesn't exist yet, the application fails to initialize the default values properly. Instead of creating the expected default object when a file is not found, the storage system seems to ignore the error and doesn't set up the initial data.

### Reproduction

```js
// Try to get a value from local storage that hasn't been created yet
const data = localStorage.getItem('some-new-key', { default: 'value' });

// Expected: { default: 'value' }
// Actual: undefined or empty
```

### Steps to reproduce
1. Start with a fresh installation (no existing local storage files)
2. Try to access a storage key that doesn't exist
3. Provide a default object as the second parameter
4. The default object is never initialized

### Expected behavior

When a local storage file doesn't exist (ENOENT error), the system should automatically create it with the provided default object. This worked in previous versions but seems to have broken recently.

### System Info
- Insomnia version: latest
- OS: macOS/Linux/Windows

---
Repository: /testbed
