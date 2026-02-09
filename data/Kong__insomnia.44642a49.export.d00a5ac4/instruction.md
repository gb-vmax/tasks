# Bug Report

### Describe the bug

I'm experiencing an issue with sorting items by creation date. When I try to sort items using `createdFirstSort`, the order appears to be reversed - newest items are showing up first instead of oldest items first.

### Reproduction

```js
const items = [
  { id: 1, name: 'Item A', created: 1000 },
  { id: 2, name: 'Item B', created: 2000 },
  { id: 3, name: 'Item C', created: 3000 }
];

// Expected: Item A, Item B, Item C (oldest to newest)
// Actual: Item C, Item B, Item A (newest to oldest)
const sorted = items.sort(createdFirstSort);
```

The sorting function seems to be doing the opposite of what it should. Items with earlier creation timestamps should appear first, but they're appearing last instead.

### Expected behavior

When using `createdFirstSort`, items should be sorted with the oldest items (lowest `created` timestamp) appearing first in the list.

---
Repository: /testbed
