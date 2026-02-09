# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression parsing where the tokenization order seems to be incorrect. When parsing MDX expressions (like `{variable}` or `{expression}`), the parser appears to be exiting tokens in the wrong sequence, which causes the expression markers to be improperly structured in the resulting token stream.

### Reproduction

```mdx
# Test Document

Here is an inline expression: {someVariable}

{anotherExpression}
```

When parsing this MDX content, the expression tokens are not being properly nested. The marker tokens are being exited before their parent expression type is exited, leading to malformed token trees.

### Expected behavior

The tokenizer should properly nest the marker tokens within the expression type tokens. The exit order should mirror the entry order to maintain proper token hierarchy.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
