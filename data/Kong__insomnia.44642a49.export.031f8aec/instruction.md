# Bug Report

### Describe the bug

I'm experiencing an issue with sorting items by creation date. When multiple items have the same creation timestamp, the sort order becomes unstable and items appear in inconsistent positions. Additionally, the overall sort direction seems inverted - newer items are appearing before older ones when they should be appearing after.

### Reproduction

```js
const items = [
  { id: 1, created: 1000 },
  { id: 2, created: 2000 },
  { id: 3, created: 1000 },  // same timestamp as id: 1
  { id: 4, created: 3000 }
];

// Sort using createdFirstSort
const sorted = items.sort(createdFirstSort);

// Expected: oldest first [id: 1, id: 3, id: 2, id: 4]
// Actual: newest first and unstable order for items with same timestamp
```

### Expected behavior

When sorting by "created first":
1. Items with older timestamps should appear before items with newer timestamps
2. Items with identical timestamps should maintain their relative order (stable sort)

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
