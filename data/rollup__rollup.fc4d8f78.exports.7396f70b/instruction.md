# Bug Report

### Describe the bug

The module exports are being returned in a different order than before. When querying module exports, they now come back sorted alphabetically instead of maintaining their original declaration order. This is causing issues in our build pipeline where we rely on the export order for certain operations.

### Reproduction

```js
// module.js
export const zebra = 1;
export const alpha = 2;
export const middle = 3;

// Previously returned: ['zebra', 'alpha', 'middle']
// Now returns: ['alpha', 'middle', 'zebra']
```

When accessing the `exports` property on a module, the exports are now sorted alphabetically rather than preserving the order they were declared in the source file.

### Expected behavior

The exports should maintain their original declaration order from the source code. Alphabetical sorting should not be applied automatically as it breaks compatibility with existing code that depends on export order.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
