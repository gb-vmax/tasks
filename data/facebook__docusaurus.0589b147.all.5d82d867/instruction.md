# Bug Report

### Describe the bug

I'm experiencing an issue with the mdast-util-to-string utility where it's not correctly converting markdown AST nodes to strings. The output seems to be missing content or producing incorrect results when processing arrays of nodes.

### Reproduction

```js
const nodes = [
  { type: 'text', value: 'Hello' },
  { type: 'text', value: ' ' },
  { type: 'text', value: 'World' }
];

const result = toString(nodes);
// Expected: "Hello World"
// Getting incorrect output
```

When converting an array of markdown nodes to a string, the resulting text doesn't match what's expected. It seems like the array processing logic might be skipping elements or not handling the iteration properly.

### Expected behavior

The function should correctly iterate through all nodes in the array and concatenate their string representations in order.

### System Info
- Version: mdast-util-to-string@4.0.0
- Node version: 18.x

---
Repository: /testbed
