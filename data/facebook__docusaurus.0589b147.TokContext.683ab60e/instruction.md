# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the context handling seems to be inverted. When working with JSX expressions in MDX files, the parser appears to be treating expression contexts as if they should preserve space and vice versa. This is causing unexpected behavior in how whitespace and expressions are processed.

### Reproduction

```jsx
// test.mdx
<Component>
  {someExpression}
  Some text with spaces
</Component>
```

When parsing this MDX content, the expression context and space preservation seem to be swapped. Expressions that should be evaluated are being treated as if they need space preservation, while text that should preserve spacing is being handled as if it's an expression context.

### Expected behavior

The parser should correctly identify:
- Expression contexts (like `{someExpression}`) and mark them as expressions
- Text content that needs space preservation and handle it accordingly

Instead, these two behaviors appear to be reversed, leading to incorrect parsing results.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like the `isExpr` and `preserveSpace` flags might have gotten mixed up somewhere in the token context initialization.

---
Repository: /testbed
