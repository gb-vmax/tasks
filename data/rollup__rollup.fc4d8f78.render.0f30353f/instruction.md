# Bug Report

### Describe the bug

When using sequence expressions with multiple expressions where the last expression needs to be preserved, the generated code incorrectly removes the trailing comma separator. This causes syntax errors in the output when the sequence expression is part of a larger statement.

### Reproduction

```js
// Input code with sequence expression
const result = (foo(), bar(), baz());

// After bundling, the output incorrectly becomes:
const result = (foo(), bar()baz());
// Notice the missing comma between bar() and baz()
```

This happens specifically when all expressions in the sequence are included and need to be rendered. The trailing separator between the second-to-last and last expression gets removed when it shouldn't be.

### Expected behavior

The sequence expression should maintain all necessary commas between expressions:
```js
const result = (foo(), bar(), baz());
```

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently and breaks the generated output. The bundled code fails to parse due to the missing comma separator.

---
Repository: /testbed
