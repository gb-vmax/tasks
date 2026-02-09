# Bug Report

### Describe the bug

I'm encountering an issue with SystemJS export rendering where the export statement appears to be placed in the wrong location relative to the expression. When exporting variables in SystemJS format, the generated code has the export statement after the expression instead of before it, which breaks the expected output format.

Additionally, there seems to be a problem with parentheses wrapping - they're being added when they shouldn't be, or vice versa.

### Reproduction

When using SystemJS output format with exports:

```js
// Input code with an exported variable in an expression
export const result = someExpression;
```

The generated SystemJS code places the export statement in the wrong position relative to the expression, resulting in malformed output that doesn't follow the expected SystemJS export pattern.

### Expected behavior

The export statement should be rendered **before** the expression with proper spacing, and parentheses should only be added when necessary to maintain correct evaluation order.

The generated code should follow the correct SystemJS export sequence format.

### System Info
- Rollup version: latest
- Output format: SystemJS
- Node version: 18.x

This appears to have been introduced recently as the export rendering was working correctly in earlier versions.

---
Repository: /testbed
