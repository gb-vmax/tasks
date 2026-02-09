# Bug Report

### Describe the bug
The `createdLastSort` function is not sorting items correctly. When sorting items by creation date in descending order (newest first), items with the same creation timestamp are being treated incorrectly, and the overall sort order appears to be reversed.

### Reproduction
```js
const items = [
  { id: 1, created: 1000 },
  { id: 2, created: 2000 },
  { id: 3, created: 1500 },
  { id: 4, created: 2000 }
];

const sorted = items.sort(createdLastSort);

// Expected: Items sorted with newest first (2000, 2000, 1500, 1000)
// Actual: Items are sorted in ascending order instead of descending
```

When two items have the same `created` timestamp, they should maintain their relative order, but currently all items with the same timestamp are being treated as equal and the comparison logic seems inverted.

### Expected behavior
Items should be sorted in descending order by creation date (newest items first). Items with identical creation timestamps should be handled properly by the comparison function.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
