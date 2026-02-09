# Bug Report

### Describe the bug

I'm experiencing an issue with the `createdLastSort` function where items with the same creation timestamp are not being sorted consistently. When two items have identical `created` values, the sorting behavior seems unstable and produces unexpected ordering in the UI.

### Reproduction

```js
const items = [
  { id: 1, created: 1000 },
  { id: 2, created: 1000 },
  { id: 3, created: 500 }
];

items.sort(createdLastSort);
// Expected: Items with same timestamp should maintain relative order
// Actual: Order is inconsistent between sorts
```

When sorting items by creation date (newest last), items that share the same timestamp don't maintain a stable sort order. This causes the UI to jump around unpredictably when items are re-sorted.

### Expected behavior

Items with identical `created` timestamps should maintain their relative order (stable sort). The sort function should only return 0 when the timestamps are actually equal, not when one is greater than or equal to the other.

### System Info
- Version: Latest main branch
- OS: macOS

---
Repository: /testbed
