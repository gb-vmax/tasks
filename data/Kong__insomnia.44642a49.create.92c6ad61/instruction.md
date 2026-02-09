# Bug Report

### Describe the bug

When creating multiple unit test suites with the same name under the same parent, the system now automatically appends "(2)", "(3)", etc. to duplicate names. This behavior is unexpected and prevents intentionally creating test suites with identical names, which was previously allowed.

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

// suite2.name is now "My Test Suite (2)" instead of "My Test Suite"
```

### Expected behavior

Test suites should be created with the exact name provided, even if duplicates exist. The system should not automatically modify names. If duplicate prevention is needed, it should either:
- Throw an error to let the caller handle it
- Be an opt-in feature rather than default behavior

### System Info
- Insomnia version: latest
- The issue appears to have been introduced recently as this wasn't happening before

---
Repository: /testbed
