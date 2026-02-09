# Bug Report

### Describe the bug

I'm experiencing an issue with MDX attribute parsing where expression values followed by whitespace aren't being handled correctly. The parser seems to be exiting the wrong token type when processing attribute value expressions, which causes problems with the AST structure.

### Reproduction

```mdx
<Component
  prop={someValue}
  anotherProp="test"
/>
```

When parsing MDX components with expression-based attribute values (using `{}`), the token exit sequence appears to be incorrect. This affects how the parser handles the transition from the expression value to subsequent whitespace and attributes.

### Expected behavior

The parser should correctly exit the `tagAttributeValueExpression` token type before processing whitespace and moving to the next attribute. The AST should maintain proper token boundaries for attribute value expressions.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This might be related to how the state machine handles token exits in the attribute parsing flow. The issue becomes apparent when you have multiple attributes with expression values separated by whitespace.

---
Repository: /testbed
