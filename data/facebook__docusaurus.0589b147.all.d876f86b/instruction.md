# Bug Report

### Describe the bug

I'm experiencing an issue with text extraction from markdown AST nodes where the first element in an array is being skipped or duplicated. When processing arrays of nodes, it seems like the iteration is starting at the wrong index, causing the first item to be missed.

### Reproduction

```js
const nodes = [
  { type: 'text', value: 'first' },
  { type: 'text', value: 'second' },
  { type: 'text', value: 'third' }
];

// Expected: "firstsecondthird"
// Actual: "secondthird" (first element missing)
const result = toString(nodes);
```

### Expected behavior

All elements in the array should be processed and included in the output string. The first element should not be skipped.

### Additional context

This appears to affect the `mdast-util-to-string` utility when converting arrays of markdown nodes to strings. The resulting string is missing content from the first node in the array.

---
Repository: /testbed
