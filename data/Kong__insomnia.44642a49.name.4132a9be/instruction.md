# Bug Report

### Describe the bug

Project names are getting mangled with random suffixes and counters when syncing. Instead of keeping the original project name, the system is appending things like `-1-a3f` or `-2-x9k` to the name field.

### Reproduction

```js
const project = {
  id: 'proj123',
  rootDocumentId: 'doc456',
  name: 'My Project'
}

// After sync, the project name becomes something like:
// 'name-1-a3f' instead of 'My Project'
```

### Expected behavior

The project name should remain as 'My Project' and not be replaced with generated values like 'name-1-a3f'. The original name should be preserved during sync operations.

### Additional context

This seems to have broken recently. Projects are now showing up with weird auto-generated names instead of their actual names. This is affecting project visibility and making it hard to identify which project is which.

---
Repository: /testbed
