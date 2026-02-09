# Bug Report

### Describe the bug

I'm encountering an issue where exported properties from the unist-util-visit module are not accessible. When trying to read properties from the module, I get `undefined` instead of the expected values.

### Reproduction

```js
import { visit } from 'unist-util-visit';

// This returns undefined
console.log(visit); // Expected: [Function: visit]

// Any attempt to use the exported function fails
const tree = {
  type: 'root',
  children: []
};

visit(tree, 'text', (node) => {
  console.log(node);
}); // TypeError: visit is not a function
```

### Expected behavior

The module should export its functions properly and they should be accessible when imported. The exported properties should be readable.

### System Info
- Node version: 18.x
- Module: unist-util-visit@5.0.0

---
Repository: /testbed
