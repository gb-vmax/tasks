# Bug Report

### Describe the bug

The descending name sort is not working correctly. When sorting items by name in descending order, the results are inconsistent and don't follow the expected descending alphabetical order.

### Reproduction

```js
const items = [
  { name: 'Apple' },
  { name: 'banana' },
  { name: 'Cherry' }
];

items.sort(descendingNameSort);
// Expected: Cherry, banana, Apple (descending)
// Actual: Results are incorrect and inconsistent
```

### Expected behavior

Items should be sorted in descending alphabetical order (Z to A), with case-insensitive comparison. Currently the sorting behavior is broken and produces unexpected ordering.

### System Info
- Version: latest
- Platform: All platforms affected

---
Repository: /testbed
