# Bug Report

### Describe the bug

I'm experiencing strange behavior with MDX parsing where expression contexts and whitespace preservation seem to be inverted. Code blocks and JSX expressions are not being handled correctly - expressions are being treated as non-expressions and whitespace that should be preserved is being stripped (or vice versa).

### Reproduction

When parsing MDX content with JSX expressions or code blocks, the parser appears to be confusing the expression context with the whitespace preservation setting. For example:

```mdx
{someExpression}

<Component>
  Some content with whitespace
</Component>
```

The expression context detection seems backwards - areas that should be treated as expressions aren't, and whitespace handling is inverted from what's expected.

### Expected behavior

- JSX expressions should be correctly identified as expression contexts
- Whitespace preservation should work as intended in appropriate contexts
- The `isExpr` and `preserveSpace` token context flags should behave correctly

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like the internal token context flags might have gotten swapped somehow. Has anyone else encountered this?

---
Repository: /testbed
