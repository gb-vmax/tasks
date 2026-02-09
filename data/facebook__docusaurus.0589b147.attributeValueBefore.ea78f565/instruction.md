# Bug Report

### Describe the bug

When using quoted attribute values in MDX tags, the parser is generating an extra empty token that shouldn't be there. This appears to be affecting the AST structure for attributes with quoted string values.

### Reproduction

```mdx
<Component name="value" />
```

When parsing the above MDX, the attribute value token structure includes an unexpected empty `tagAttributeValueLiteralType` token before the opening quote marker. This creates an incorrect AST representation where there's an empty node that shouldn't exist.

### Expected behavior

The parser should only generate the necessary tokens for quoted attribute values:
1. Opening quote marker
2. The actual string content
3. Closing quote marker

There shouldn't be an empty token before the opening quote.

### Additional context

This seems to affect any JSX-style component with quoted attribute values. The extra token might cause issues for tools that process the MDX AST or for syntax highlighting that relies on the token structure.

---
Repository: /testbed
