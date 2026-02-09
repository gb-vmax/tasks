# Bug Report

### Issue with System.js export statement positioning

I've encountered a problem with how System.js export statements are being generated in the output code. The exports and parentheses are appearing in the wrong positions, which breaks the generated code.

### Reproduction

When bundling code with System.js format that has exports before expressions requiring parentheses, the output is malformed:

```js
// Input code (simplified example)
export const foo = someExpression;
```

The generated System.js output has the export statement and parentheses inserted at incorrect positions in the code, causing syntax errors when the bundle is executed.

### Expected behavior

The export statement should be positioned correctly before the expression, and any required parentheses should properly wrap the expression in the right order.

### System Info
- Rollup version: latest
- Output format: system
- Node version: 18.x

This seems to have broken recently as the generated code was working fine before. The parentheses and export statements are just in the wrong spots now.

---
Repository: /testbed
