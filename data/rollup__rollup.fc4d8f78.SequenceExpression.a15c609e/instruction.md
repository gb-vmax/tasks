# Bug Report

### Describe the bug

When using sequence expressions (comma operator), the code generation is producing incorrect output. It appears that all expressions in the sequence are being included when they shouldn't be, or the rendering logic is applying transformations to the wrong expressions.

### Reproduction

```js
// Example with sequence expression
const result = (sideEffect(), computeValue(), finalValue);

// Or in a more realistic scenario:
export default (init(), setup(), render());
```

After bundling, the output seems to include all expressions in the sequence even when only the last one should be kept, or vice versa. The parentheses and line break handling also appears incorrect.

### Expected behavior

For sequence expressions:
- Only expressions with side effects or the final expression should be included in the output
- The first expression in a sequence should have line breaks removed when necessary to prevent ASI issues
- Parent context (like being a call expression callee) should only apply to the last expression in the sequence

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
