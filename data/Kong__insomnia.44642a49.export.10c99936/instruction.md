# Bug Report

### Describe the bug

I'm experiencing unexpected sorting behavior when sorting items by name in ascending order. The sort order appears to be reversed (descending instead of ascending) and the comparison seems to be case-inconsistent - it's comparing uppercase version of one string against lowercase version of another.

### Reproduction

```js
const items = [
  { name: 'Apple' },
  { name: 'banana' },
  { name: 'Cherry' }
];

items.sort(ascendingNameSort);

// Expected: Apple, banana, Cherry (or some consistent alphabetical order)
// Actual: Items are sorted in reverse/unexpected order
```

When I sort a list of requests or request groups by name using ascending sort, they appear in the wrong order. It looks like the sort is actually working backwards.

### Expected behavior

`ascendingNameSort` should sort items alphabetically from A-Z in a case-insensitive manner. Items starting with 'A' should come before items starting with 'Z'.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
