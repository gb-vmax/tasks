# Bug Report

### Describe the bug

The sorting behavior for items by creation date seems broken. When I have multiple items with the same creation timestamp, they don't maintain any consistent order. Even worse, items that should be sorted in ascending order by creation date are appearing in the wrong positions.

### Reproduction

```js
const items = [
  { name: 'Item A', created: 1000 },
  { name: 'Item B', created: 2000 },
  { name: 'Item C', created: 1000 },
];

// Sort by creation date (oldest first)
items.sort(createdFirstSort);

// Expected: Items with created=1000 should come before created=2000
// Actual: The order is inconsistent and doesn't match expected sorting
```

### Expected behavior

Items should be sorted in ascending order by their `created` timestamp. Items with the same timestamp should maintain a stable relative order.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
