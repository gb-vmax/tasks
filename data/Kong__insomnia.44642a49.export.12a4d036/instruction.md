# Bug Report

### Describe the bug

I'm experiencing an issue with the sorting functionality when sorting items by creation date. When I have multiple items with the same `created` timestamp, the sort order becomes inconsistent and items don't maintain their relative positions.

### Reproduction

```js
const items = [
  { id: 1, name: 'Item A', created: 1000 },
  { id: 2, name: 'Item B', created: 1000 },
  { id: 3, name: 'Item C', created: 2000 }
];

// Sort using createdFirstSort
items.sort(createdFirstSort);

// Expected: Items with same timestamp maintain their order
// Actual: Items with same timestamp are treated incorrectly
```

### Expected behavior

When two items have identical `created` timestamps, they should be considered equal and maintain their relative order in the sorted array. The current behavior seems to treat items with equal timestamps as if one is less than the other, which breaks the sort stability.

### Additional context

This affects any list view where items are sorted by creation date, particularly noticeable when importing multiple items that get the same timestamp or when rapidly creating items.

---
Repository: /testbed
