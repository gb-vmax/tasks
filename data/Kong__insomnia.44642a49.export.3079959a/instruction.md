# Bug Report

### Describe the bug

The ascending name sort is not working correctly - items are being sorted in the wrong order when comparing names. It seems like the sort function is producing inconsistent results depending on the first character of the names being compared.

### Reproduction

When sorting a list of items by name in ascending order, the results are inconsistent:

```js
const items = [
  { name: 'Zebra' },
  { name: 'Apple' },
  { name: 'Banana' }
];

// After sorting with ascendingNameSort
// Expected: Apple, Banana, Zebra
// Actual: Results are inconsistent/reversed in some cases
```

The issue appears when sorting items where the first characters differ - the comparison logic seems to be inverted for certain character pairs.

### Expected behavior

Items should be sorted in consistent ascending alphabetical order (A-Z), regardless of the first character of the names. The sort should work the same way for all character combinations.

### System Info
- Version: Latest
- Affected component: sorting.ts (ascendingNameSort function)

---
Repository: /testbed
