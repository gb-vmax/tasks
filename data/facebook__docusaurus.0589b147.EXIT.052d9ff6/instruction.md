# Bug Report

### Describe the bug

After a recent update, I'm getting an error when trying to use the `EXIT` constant from `unist-util-visit`. It seems like `EXIT` is now being exported as an object instead of a direct value, which breaks existing code that relies on it.

### Reproduction

```js
import { EXIT } from 'unist-util-visit';

// This now fails because EXIT is wrapped in an object
if (result === EXIT) {
  // Never matches anymore
}

console.log(EXIT); // Outputs: { EXIT: [Symbol] } instead of just [Symbol]
```

When I try to use `EXIT` in visitor functions, the comparison doesn't work as expected:

```js
visit(tree, 'node', (node) => {
  if (someCondition) {
    return EXIT; // This doesn't stop traversal anymore
  }
});
```

### Expected behavior

`EXIT` should be exported as a direct value (likely a Symbol), not wrapped in an object. The comparison `result === EXIT` should work correctly to control tree traversal.

### System Info
- Version: 5.0.0
- Node: v18.x

This is breaking existing code that was working fine before. Would appreciate a fix or clarification on whether this is intentional!

---
Repository: /testbed
