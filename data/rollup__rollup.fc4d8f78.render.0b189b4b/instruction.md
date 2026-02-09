# Bug Report

### Describe the bug

Assignment expressions are rendering incorrectly when the left-hand side is excluded from the output. The condition for checking whether to include the left side appears to be inverted, causing the bundler to remove code that should be kept and keep code that should be removed.

### Reproduction

```js
// Example code that triggers the issue
let x;
const result = (x = someValue);

// When x is tree-shaken/excluded, the assignment expression
// renders incorrectly in the output bundle
```

When bundling code with assignment expressions where the left-hand side variable is not included in the final output (e.g., due to tree-shaking), the rendering logic produces incorrect output. The left side is being rendered when it shouldn't be, and the optimization to remove the unused assignment is not being applied.

### Expected behavior

When the left-hand side of an assignment expression is excluded from the bundle:
- The left side should NOT be rendered
- Only the right-hand side expression should remain
- The assignment operator and left operand should be removed from the output

When the left-hand side IS included:
- Both left and right sides should be rendered normally
- The full assignment expression should appear in the output

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a logic error in the rendering condition - the behavior is completely reversed from what it should be.

---
Repository: /testbed
