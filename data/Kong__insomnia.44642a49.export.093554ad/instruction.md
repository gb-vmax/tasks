# Bug Report

### Describe the bug
The `createdLastSort` function is not sorting items correctly. When sorting by creation date in descending order (newest first), items are appearing in the wrong order.

### Reproduction
```js
const items = [
  { created: 1000 },
  { created: 2000 },
  { created: 1500 }
];

items.sort(createdLastSort);

// Expected: [{ created: 2000 }, { created: 1500 }, { created: 1000 }]
// Actual: Items are in ascending order instead of descending
```

### Expected behavior
When using `createdLastSort`, items should be sorted with the most recently created items first (descending order by creation timestamp). Currently it seems to be sorting in ascending order instead, or treating equal timestamps incorrectly.

### Additional context
This affects any UI that displays items sorted by creation date in reverse chronological order. Users expect to see their newest items at the top but they're appearing at the bottom instead.

---
Repository: /testbed
