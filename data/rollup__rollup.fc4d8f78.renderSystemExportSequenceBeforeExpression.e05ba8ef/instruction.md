# Bug Report

### Describe the bug

I'm experiencing an issue with SystemJS export rendering where parentheses are being added incorrectly around expressions. It seems like the logic for when to wrap expressions in parentheses has been inverted - expressions that should have parens don't get them, and expressions that shouldn't have parens are getting them added.

### Reproduction

When using SystemJS format with exports, the generated code has incorrect parenthesization:

```js
// Example: exporting a sequence expression
export const result = (foo(), bar());
```

The generated SystemJS output is adding parentheses in the wrong cases, which is breaking the expected output format. Expressions that need to be wrapped to preserve correct evaluation order are left unwrapped, while expressions that don't need wrapping are getting extra parentheses.

### Expected behavior

The code should correctly determine when parentheses are needed around expressions and only add them in those cases. Expressions that already have correct precedence shouldn't get additional wrapping.

### System Info
- Rollup version: latest
- Output format: SystemJS

---
Repository: /testbed
