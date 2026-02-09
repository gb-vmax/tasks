# Bug Report

### Describe the bug

I'm experiencing an issue with the `describeChanges` function where it's now including changes for keys that should be ignored. It seems like the filtering logic isn't working as expected anymore.

### Reproduction

```js
const objA = {
  id: '123',
  name: 'Test',
  modified: 1234567890,
  _ignored: 'should not be tracked'
};

const objB = {
  id: '123',
  name: 'Updated Test',
  modified: 1234567891,
  _ignored: 'different value'
};

// Get the list of changes
const changes = describeChanges(objA, objB);

// Changes now incorrectly includes modifications to keys that should be ignored
// Expected: only 'name' and 'modified' changes
// Actual: includes '_ignored' field changes as well
```

### Expected behavior

The function should skip keys that are meant to be ignored (like internal/private fields) and only report meaningful changes between the two objects. Fields that match the ignore criteria shouldn't appear in the changes list.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
