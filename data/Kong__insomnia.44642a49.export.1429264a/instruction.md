# Bug Report

### Describe the bug

When sorting items by name in ascending order, the items are being sorted in the wrong direction. Items appear to be sorted in descending order (Z to A) instead of ascending order (A to Z).

### Reproduction

```js
const items = [
  { name: 'Charlie' },
  { name: 'Alice' },
  { name: 'Bob' }
];

// Sort using ascendingNameSort
items.sort(ascendingNameSort);

// Expected: ['Alice', 'Bob', 'Charlie']
// Actual: ['Charlie', 'Bob', 'Alice']
```

### Expected behavior

When using `ascendingNameSort`, items should be sorted alphabetically from A to Z. Currently they're being sorted in reverse (Z to A).

### Steps to reproduce

1. Create a list of requests/request groups with different names
2. Apply ascending name sort
3. Observe that items are sorted in descending order instead

This affects sorting in the request list and any other places where `ascendingNameSort` is used.

---
Repository: /testbed
