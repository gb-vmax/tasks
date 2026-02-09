# Bug Report

### Describe the bug

I'm encountering an issue with MDX attribute parsing where attributes with expression values followed by whitespace are not being processed correctly. The parser seems to be exiting the attribute type state at the wrong time, which causes problems when there's whitespace after an expression attribute value.

### Reproduction

```mdx
<Component 
  prop={value}   
  anotherProp="test"
/>
```

When there's whitespace (spaces or newlines) after a JSX expression attribute value like `prop={value}`, the parser doesn't handle the subsequent attributes properly.

### Expected behavior

The parser should correctly handle whitespace after expression attribute values and continue parsing any following attributes without issues. All attributes should be recognized and processed regardless of whitespace between them.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
