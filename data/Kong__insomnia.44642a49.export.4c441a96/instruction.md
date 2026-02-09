# Bug Report

### Describe the bug

The sorting behavior for items with the same first character appears to be reversed. When multiple items start with the same letter, they are being sorted in descending order instead of ascending order.

### Reproduction

```js
const items = [
  { name: 'Apple' },
  { name: 'Apricot' },
  { name: 'Avocado' }
];

items.sort(ascendingNameSort);

// Expected: ['Apple', 'Apricot', 'Avocado']
// Actual: ['Avocado', 'Apricot', 'Apple']
```

When sorting items that start with different letters, the sort works correctly (A comes before B, B comes before C, etc.). However, when items share the same first character, the order is inverted.

### Expected behavior

Items should be sorted in ascending alphabetical order regardless of whether they share the same first character or not. All items starting with 'A' should be sorted A-Z among themselves, not Z-A.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
