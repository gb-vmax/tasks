# Bug Report

### Describe the bug

When creating multiple unit test suites with the same name under the same parent, the system doesn't prevent duplicate names. This causes confusion in the UI where multiple test suites appear with identical names, making it impossible to distinguish between them.

### Reproduction

```js
// Create first test suite
const suite1 = create({
  parentId: 'workspace_123',
  name: 'My Test Suite'
});

// Create second test suite with same name
const suite2 = create({
  parentId: 'workspace_123',
  name: 'My Test Suite'
});

// Both suites now have the name "My Test Suite"
// Users can't tell them apart in the UI
```

### Expected behavior

When creating a test suite with a name that already exists under the same parent, the system should automatically generate a unique name (e.g., "My Test Suite (2)", "My Test Suite (3)", etc.) to avoid duplicates.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
