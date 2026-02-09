# Bug Report

### Describe the bug

I'm encountering an issue with the `wrap` function where it's skipping the first element in the `nodes` array. When I pass an array of nodes to be wrapped, the output is missing the first node entirely.

### Reproduction

```js
const nodes = [
  { type: 'element', name: 'p', children: ['First'] },
  { type: 'element', name: 'p', children: ['Second'] },
  { type: 'element', name: 'p', children: ['Third'] }
];

const result = wrap(nodes, false);

// Expected: All three nodes in the result
// Actual: Only 'Second' and 'Third' are present, 'First' is missing
```

### Expected behavior

All nodes passed to the `wrap` function should be included in the returned result array. The first node should not be skipped.

### Additional context

This seems to affect any array of nodes regardless of size. Even with a single-element array, that element gets skipped and the result is essentially empty (except for any newline text nodes if `loose` is true).

---
Repository: /testbed
