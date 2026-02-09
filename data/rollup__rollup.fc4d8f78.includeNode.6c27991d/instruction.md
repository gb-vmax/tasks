# Bug Report

### Describe the bug

I'm experiencing an issue with assignment expressions where the deoptimization logic seems to be applied at the wrong time. When an assignment expression is included in the bundle, the deoptimizations are being applied even when they've already been applied previously, which shouldn't happen.

### Reproduction

```js
// Create a module with an assignment expression
const code = `
let x = 5;
x = 10;
export { x };
`;

// Bundle the code
// The assignment expression's includeNode is called
// Deoptimizations get applied multiple times instead of being skipped
```

### Expected behavior

When `includeNode` is called on an assignment expression:
1. The right-hand side path should be included first
2. The node should be marked as included
3. Deoptimizations should only be applied if they haven't been applied yet (when `deoptimized` is `false`)

Currently it seems like deoptimizations might be getting applied when they shouldn't be, or the order of operations is causing unexpected behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
