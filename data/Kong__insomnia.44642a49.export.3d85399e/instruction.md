# Bug Report

### Describe the bug

I'm experiencing unexpected sorting behavior when sorting items by name. Items with the same length names are being sorted incorrectly - it seems like only the second character is being compared instead of the full name.

### Reproduction

```js
const items = [
  { name: 'apple' },
  { name: 'apricot' },
  { name: 'avocado' }
];

// Sort using ascendingNameSort
items.sort(ascendingNameSort);

// Expected order: apple, apricot, avocado
// Actual order: apple, avocado, apricot (sorted by second character only)
```

Another example that shows the issue more clearly:

```js
const items = [
  { name: 'test1' },
  { name: 'test2' },
  { name: 'test3' }
];

items.sort(ascendingNameSort);
// These get sorted by the second character ('e') instead of the full string
```

### Expected behavior

Items should be sorted alphabetically by their full name, not just by a single character. The standard `localeCompare` behavior should apply to all names regardless of their length.

### System Info
- Version: latest
- Affects: Request/RequestGroup/GrpcRequest sorting

---
Repository: /testbed
