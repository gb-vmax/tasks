# Bug Report

### Describe the bug

The sorting behavior for items by creation date seems to be broken. When sorting items by "created first", items with the same creation timestamp are being treated incorrectly, and the overall sort order appears to be reversed from what's expected.

### Reproduction

```js
const items = [
  { name: 'Item A', created: 1000 },
  { name: 'Item B', created: 2000 },
  { name: 'Item C', created: 1000 },
];

items.sort(createdFirstSort);
// Expected: Item A (1000), Item C (1000), Item B (2000)
// Actual: Item B (2000), Item A (1000), Item C (1000)
```

When multiple items have the same `created` timestamp, they should maintain their relative order and appear before items with later timestamps. Instead, the sort is returning them in reverse order.

### Expected behavior

Items should be sorted with oldest items first (ascending by `created` timestamp). Items with identical timestamps should be considered equal and maintain stable sort order.

### System Info
- Package: insomnia
- Affected module: common/sorting.ts

---
Repository: /testbed
