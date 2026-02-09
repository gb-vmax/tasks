# Bug Report

### Describe the bug

I'm experiencing an issue with syntax extension handling where the first construct in a list is being skipped during processing. When adding custom syntax constructs, the initial element doesn't get properly registered, causing parsing to fail for certain patterns.

### Reproduction

```js
const constructs = [
  { name: 'first', add: 'before' },
  { name: 'second', add: 'before' },
  { name: 'third', add: 'after' }
];

// When processing these constructs, 'first' is not included
// Only 'second' gets added to the 'before' array
```

### Expected behavior

All constructs marked with `add: 'before'` should be collected and inserted at the beginning of the existing constructs array. Currently, the first construct in the list is being missed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
