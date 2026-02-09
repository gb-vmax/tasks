# Bug Report

### Describe the bug

I'm experiencing an issue with block statement optimization in Rollup. When setting the `deoptimizeBody` flag on a `BlockStatement`, the behavior seems to be inverted - setting it to `true` appears to disable optimization instead of enabling it, and vice versa.

### Reproduction

```js
// Create a block statement that should be deoptimized
const blockStatement = new BlockStatement(/* ... */);

// Try to enable deoptimization
blockStatement.deoptimizeBody = true;

// Expected: body should be deoptimized
// Actual: body remains optimized
```

This appears to affect how Rollup handles optimization of block statements during the tree-shaking and code generation phases. The flag is being set to the opposite of what's intended.

### Expected behavior

When `deoptimizeBody` is set to `true`, the block statement's body should be deoptimized. When set to `false`, it should remain optimized. Currently this behavior appears to be reversed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
