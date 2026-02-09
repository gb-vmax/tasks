# Bug Report

### Describe the bug

I'm encountering an issue with expression parsing where the parser seems to be consuming an extra token before returning the parsed expression. This causes the parser state to be incorrect after parsing, leading to unexpected behavior when trying to parse expressions at specific positions.

### Reproduction

```js
const parser = Parser.parseExpressionAt(input, startPosition, options);
// The parser has already consumed the next token
// This means subsequent parsing operations start from the wrong position
```

When calling `parseExpressionAt`, the function appears to advance the token stream one position too far. This becomes problematic when you need to parse multiple expressions in sequence or when the position of the parser after parsing matters for downstream operations.

### Expected behavior

After parsing an expression at a given position, the parser should be positioned immediately after the parsed expression, not one token beyond it. The token stream should only advance as far as necessary to parse the requested expression.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
