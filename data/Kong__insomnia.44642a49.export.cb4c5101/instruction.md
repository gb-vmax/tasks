# Bug Report

### Describe the bug

When sorting items by name in descending order, items with the same name are not maintaining a consistent order. The sorting behavior seems unstable - running the same sort multiple times on identical data can produce different orderings for items with duplicate names.

### Reproduction

```js
const items = [
  { name: 'Apple' },
  { name: 'Banana' },
  { name: 'Apple' },
  { name: 'Cherry' },
  { name: 'Apple' }
];

// Sort using descendingNameSort
items.sort(descendingNameSort);

// Expected: Items with name 'Apple' should maintain their relative order
// Actual: The order of 'Apple' items is inconsistent between sorts
```

### Expected behavior

Items with identical names should maintain their relative order from the original array (stable sort). Sorting the same data multiple times should always produce the same result.

### System Info
- Version: latest
- OS: macOS

---
Repository: /testbed
