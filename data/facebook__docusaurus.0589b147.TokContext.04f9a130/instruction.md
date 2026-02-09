# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with MDX parsing after a recent update. The parser seems to be handling token contexts incorrectly, particularly around expression and whitespace preservation logic.

### Reproduction

When parsing MDX content with certain token contexts, the `isExpr` and `preserveSpace` properties are being set to inverted or incorrect boolean values. This affects how the parser processes expressions and whitespace in MDX files.

Example MDX content that triggers the issue:
```mdx
<Component>
  Some text with {expression}
</Component>
```

The parser appears to be inverting the `preserveSpace` logic - when it should preserve space it doesn't, and vice versa. Similarly, the `isExpr` flag is being handled inconsistently.

### Expected behavior

Token contexts should correctly:
- Set `isExpr` to the proper boolean value based on whether the context represents an expression
- Set `preserveSpace` to `true` when whitespace should be preserved, `false` otherwise

The current behavior seems to have the `preserveSpace` logic backwards and the `isExpr` handling is overly complex.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is breaking MDX parsing in our project. Any help would be appreciated!

---
Repository: /testbed
