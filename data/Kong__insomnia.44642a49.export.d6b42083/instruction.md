# Bug Report

### Describe the bug

I'm experiencing an issue with the `createdLastSort` function where items with the same `created` timestamp are not being handled correctly. When two items have identical creation times, the sorting behavior is inconsistent and doesn't maintain a stable sort order.

### Reproduction

```js
const items = [
  { id: 1, created: 1000 },
  { id: 2, created: 1000 },
  { id: 3, created: 500 }
];

const sorted = items.sort(createdLastSort);
// Expected: Items with same created time should maintain their relative order
// Actual: Order is unpredictable for items with created: 1000
```

### Expected behavior

When sorting items by creation date (newest first), items with identical `created` timestamps should maintain their original relative order (stable sort). The function should return `0` when comparing items with the same timestamp to indicate they are equal.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
