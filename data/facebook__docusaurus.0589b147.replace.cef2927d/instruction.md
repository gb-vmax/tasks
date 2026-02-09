# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX walker when trying to replace nodes at index 0. When `replace()` is called with `index2 = 0`, the replacement doesn't work because the condition `if (index2 != null)` evaluates to false for 0.

### Reproduction

```js
const parent = { children: ['node1', 'node2', 'node3'] };
const walker = new WalkerBase();

// This doesn't work - trying to replace the first element
walker.replace(parent, 'children', 0, 'newNode');
// Expected: parent.children[0] === 'newNode'
// Actual: parent.children[0] === 'node1' (unchanged)

// This works fine - replacing second element
walker.replace(parent, 'children', 1, 'newNode');
// parent.children[1] === 'newNode' ✓
```

The problem is that when `index2` is 0, the falsy check causes it to fall through to the `else` branch instead of treating it as a valid array index.

### Expected behavior

Replacing a node at index 0 should work the same as replacing at any other valid index. The first element in the array should be updated correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
