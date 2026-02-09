# Bug Report

### Describe the bug

The descending name sort is not working correctly. When sorting items by name in descending order, the results are inconsistent and don't follow proper descending alphabetical order.

### Reproduction

```js
const items = [
  { name: 'Apple' },
  { name: 'banana' },
  { name: 'Cherry' }
];

items.sort(descendingNameSort);
// Expected: Cherry, banana, Apple (or cherry, banana, apple)
// Actual: Inconsistent ordering that doesn't match descending alphabetical sort
```

The sorting behavior seems to be affected by the length of the names and case sensitivity in unexpected ways. Items with different name lengths are sorted differently than items with the same length, which shouldn't happen in a standard descending alphabetical sort.

### Expected behavior

Items should be sorted in descending alphabetical order (Z to A), with consistent case-insensitive comparison regardless of string length. The current behavior produces unexpected results that don't match standard descending sort expectations.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
