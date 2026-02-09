# Bug Report

### Describe the bug

After a recent update, MDX expressions are not being parsed correctly when they appear before JSX elements in the document. The order of parsing seems to have changed and expressions that used to work are now being ignored or processed incorrectly.

### Reproduction

```mdx
{/* This expression should be evaluated first */}
{someVariable}

<Component prop="value" />
```

When the above MDX is processed, the expression `{someVariable}` is not being handled properly. It seems like JSX elements are being parsed before expressions, which causes issues when expressions need to be evaluated in a specific order relative to JSX.

### Expected behavior

Expressions should be parsed and evaluated before JSX elements, maintaining the correct order of operations. The expression `{someVariable}` should be processed first, followed by the JSX component.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be a regression from previous behavior where the parsing order was different.

---
Repository: /testbed
