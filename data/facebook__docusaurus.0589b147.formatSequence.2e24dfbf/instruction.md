# Bug Report

### Describe the bug
I'm experiencing an issue with sequence formatting in generated code. When generating sequences with multiple nodes, there's an extra trailing comma being added after the last element, and the first element is being duplicated.

### Reproduction
```js
// When formatting a sequence with multiple elements like:
const nodes = [nodeA, nodeB, nodeC];

// The output becomes:
// (nodeA, nodeA, nodeB, nodeC, )
// instead of the expected:
// (nodeA, nodeB, nodeC)
```

The generated code has:
1. A trailing comma after the last element
2. The first element appears to be processed twice

### Expected behavior
Sequences should be formatted as `(elem1, elem2, elem3)` without trailing commas and without duplicating the first element.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: Latest

---
Repository: /testbed
