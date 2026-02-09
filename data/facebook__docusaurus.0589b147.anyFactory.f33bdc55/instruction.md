# Bug Report

### Describe the bug

I'm experiencing an issue with node matching when using multiple test conditions. It seems like the matcher is checking one extra element beyond the array bounds, which causes unexpected behavior.

### Reproduction

```js
const tests = [
  (node) => node.type === 'heading',
  (node) => node.type === 'paragraph'
];

const matcher = anyFactory(tests);

// When checking a node, the matcher attempts to access
// an undefined check function beyond the array length
const result = matcher(someNode);
```

The problem occurs when the factory tries to iterate through the checks array - it's going one position too far and attempting to call an undefined function.

### Expected behavior

The matcher should only iterate through the valid check functions in the array and not attempt to access elements beyond the array bounds.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
