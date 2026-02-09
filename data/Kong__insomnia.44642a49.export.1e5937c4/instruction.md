# Bug Report

### Describe the bug
The `createdLastSort` function is not sorting items correctly. When sorting items by creation date in descending order (newest first), items with the same creation timestamp are being treated incorrectly, and the overall sort order appears broken.

### Reproduction
```js
const items = [
  { created: 1000, name: 'Item A' },
  { created: 2000, name: 'Item B' },
  { created: 1500, name: 'Item C' },
  { created: 2000, name: 'Item D' }, // same timestamp as Item B
];

const sorted = items.sort(createdLastSort);

// Expected: Items sorted by created timestamp, newest first
// [Item B, Item D, Item C, Item A] or [Item D, Item B, Item C, Item A]

// Actual: Incorrect sort order
```

### Expected behavior
Items should be sorted in descending order by their `created` timestamp (most recent first). Items with identical timestamps should maintain their relative order or be treated as equal.

### Additional context
This is affecting the display order in collections and request lists where users expect to see the most recently created items at the top. The sorting behavior seems inconsistent and doesn't match the expected "created last" (newest first) ordering.

---
Repository: /testbed
