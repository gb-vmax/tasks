# Bug Report

### Describe the bug

MDX expression parsing is broken - expressions are not being recognized or parsed correctly. When using JSX expressions in MDX files (like `{variable}` or `{expression}`), they fail to parse and the content is not rendered as expected.

### Reproduction

```mdx
# Test Document

Here's a variable: {myVar}

And an expression: {1 + 2}
```

When processing this MDX content, the expressions inside curly braces are not being parsed correctly. The parser seems to be exiting the expression type before actually entering it, causing the expression tokenization to fail.

### Expected behavior

The MDX expressions should be properly tokenized and parsed. Variables and expressions wrapped in curly braces should be recognized as valid MDX expression nodes in the syntax tree.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This appears to have started happening recently. The expression markers (curly braces) are being processed in the wrong order during the parsing phase.

---
Repository: /testbed
