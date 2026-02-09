# Bug Report

### Describe the bug
When creating a new Proto Directory, the application crashes with a syntax error. It appears that the initialization function is returning an invalid value, causing the proto directory creation to fail completely.

### Reproduction
```js
// Try to create a new proto directory
const newProtoDir = init();
// Expected: returns an object with name property
// Actual: syntax error - invalid return statement
```

Steps to reproduce:
1. Attempt to create a new proto directory in the application
2. The initialization fails immediately
3. Application crashes or throws an error

### Expected behavior
The `init()` function should return a valid proto directory object with a `name` property set to 'New Proto Directory'. The creation process should complete successfully without any syntax errors.

### System Info
- Insomnia version: latest
- OS: Any

This seems to have been introduced in a recent change to the proto-directory model. The function is not returning a proper object anymore.

---
Repository: /testbed
