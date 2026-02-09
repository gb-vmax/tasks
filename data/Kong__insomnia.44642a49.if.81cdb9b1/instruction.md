# Bug Report

### Describe the bug

The application hangs indefinitely when trying to read from local storage if a file doesn't exist. The UI becomes completely unresponsive and needs to be force-closed.

### Reproduction

1. Delete or move the local storage file for a specific key
2. Try to access that key using `getItem()` with a default object
3. The application freezes and becomes unresponsive

```js
// Assuming the file for 'userSettings' doesn't exist
const settings = localStorage.getItem('userSettings', { theme: 'dark' });
// Application hangs here indefinitely
```

### Expected behavior

The method should return the default object immediately when the file doesn't exist, without causing the application to hang. It should create the file with the default value and continue execution.

### System Info
- Insomnia version: latest
- OS: macOS/Windows/Linux

This is blocking our workflow as we can't use the app after clearing cache or on fresh installs. Any help would be appreciated!

---
Repository: /testbed
