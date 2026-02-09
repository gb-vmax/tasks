# Bug Report

### Describe the bug
When sorting items in descending order by name, the sort function is not working correctly. Instead of comparing the full names, it appears to only compare the first character of each name, which leads to incorrect sorting results.

### Reproduction
```js
const items = [
  { name: 'apple' },
  { name: 'banana' },
  { name: 'apricot' }
];

// Sort using descendingNameSort
items.sort(descendingNameSort);

// Expected: ['banana', 'apricot', 'apple']
// Actual: Items with same first letter are not sorted correctly
```

### Expected behavior
Items should be sorted in descending alphabetical order by their full name, not just by the first character. For example:
- "banana" should come before "apricot"
- "apricot" should come before "apple"

Currently, items that start with the same letter don't maintain proper descending order.

### System Info
- Version: Latest
- OS: macOS

---
Repository: /testbed
