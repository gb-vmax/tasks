# Bug Report

### Describe the bug

The `createdLastSort` function is not sorting items correctly. When I try to sort a list of items by creation date (newest first), the items appear in the wrong order - they're showing up oldest first instead.

### Reproduction

```js
const items = [
  { created: 1000, name: 'oldest' },
  { created: 2000, name: 'middle' },
  { created: 3000, name: 'newest' }
];

items.sort(createdLastSort);

// Expected: newest, middle, oldest
// Actual: oldest, middle, newest
```

The sorting is completely inverted from what it should be. Items with newer creation timestamps should appear first, but they're appearing last.

### Expected behavior

When using `createdLastSort`, items should be ordered with the most recently created items first (descending order by creation timestamp). Currently it's doing the opposite.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
