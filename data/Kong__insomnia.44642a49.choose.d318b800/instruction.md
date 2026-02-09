# Bug Report

### Describe the bug

When syncing branches, merge conflicts are not being automatically resolved in cases where one side has content and the other is empty, or when both sides have identical content. The conflict resolution always returns `null` instead of making an intelligent choice.

### Reproduction

```js
// Case 1: Only "mine" has content, "theirs" is empty
const conflict = {
  key: 'some-key',
  mineBlob: 'some content',
  theirsBlob: '',
  // ... other properties
}
// Expected: Should auto-resolve to 'mine'
// Actual: Returns null, requiring manual resolution

// Case 2: Both sides have identical content
const conflict = {
  key: 'some-key',
  mineBlob: 'identical content',
  theirsBlob: 'identical content',
  // ... other properties
}
// Expected: Should auto-resolve to 'mine' (or 'theirs', doesn't matter)
// Actual: Returns null, requiring manual resolution
```

### Expected behavior

The merge conflict resolver should automatically choose a side when:
1. One side has content and the other is empty/whitespace - should choose the side with content
2. Both sides have identical content - should auto-resolve since there's no actual conflict

Currently it always returns `null` forcing manual resolution even when the choice is obvious.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
