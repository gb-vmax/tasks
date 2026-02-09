# Bug Report

### Describe the bug
After a recent update, unit test suites are being returned in an unexpected format. Instead of getting the test suite object directly, it's now wrapped in an object with `migrated` and `version` properties.

### Reproduction
```js
const testSuite = {
  _id: 'suite_1',
  name: 'My Test Suite',
  tests: []
};

const result = migrate(testSuite);
// Expected: { _id: 'suite_1', name: 'My Test Suite' }
// Actual: { migrated: { _id: 'suite_1', name: 'My Test Suite' }, version: 1 }
```

### Expected behavior
The `migrate()` function should return the test suite object in the same format as before, not wrapped in a container object. Other parts of the codebase expect the direct object structure.

### Additional context
This seems to have started happening recently. The wrapped format breaks compatibility with existing code that processes test suites.

---
Repository: /testbed
