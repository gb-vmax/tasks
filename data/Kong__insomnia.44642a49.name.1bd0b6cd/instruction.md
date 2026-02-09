# Bug Report

### Describe the bug
When creating multiple branches in quick succession, they all get assigned the same default name instead of unique names. This causes conflicts when trying to create branches rapidly.

### Reproduction
```js
// Create multiple branches quickly
const branch1 = createBranch();
const branch2 = createBranch();
const branch3 = createBranch();

console.log(branch1.name); // Expected: branch-20240115-143022-001
console.log(branch2.name); // Expected: branch-20240115-143022-002
console.log(branch3.name); // Expected: branch-20240115-143022-003

// Actual: All three branches have the same name
```

### Expected behavior
Each branch created within the same second should get a unique name with an incrementing sequence number (001, 002, 003, etc.). The sequence counter should persist across multiple branch creations to ensure uniqueness.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our workflow where we need to create multiple branches programmatically. Any workaround would be appreciated!

---
Repository: /testbed
