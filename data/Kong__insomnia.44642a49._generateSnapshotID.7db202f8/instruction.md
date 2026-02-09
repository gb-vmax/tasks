# Bug Report

### Describe the bug

I'm experiencing an issue with snapshot ID generation in the VCS module. When creating snapshots with the same state but different parent IDs, the generated snapshot IDs are identical, which shouldn't be the case since they have different parents.

### Reproduction

```js
const state = [
  { blob: 'abc123' },
  { blob: 'def456' }
];

const snapshot1 = _generateSnapshotID('parent1', 'project1', state);
const snapshot2 = _generateSnapshotID('parent2', 'project1', state);

// These should be different but they're the same
console.log(snapshot1 === snapshot2); // true (unexpected)
```

### Expected behavior

Snapshots with different parent IDs should generate different snapshot IDs, even when the backend project and state are identical. The parent ID should be factored into the hash calculation to ensure uniqueness across different snapshot lineages.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
