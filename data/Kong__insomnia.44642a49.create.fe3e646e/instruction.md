# Bug Report

### Describe the bug

After a recent update, creating unit test suites is broken. When trying to create a new test suite, the application hangs and nothing happens. The suite doesn't get created and the UI becomes unresponsive.

### Reproduction

```js
// Try to create a unit test suite
const suite = create({
  parentId: 'workspace_123',
  name: 'My Test Suite'
});

// Application hangs here - suite is never created
```

This seems to happen consistently when creating any new test suite. The issue wasn't present in the previous version.

### Expected behavior

The test suite should be created immediately without any hanging or delays. The function should return the created suite object synchronously.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
