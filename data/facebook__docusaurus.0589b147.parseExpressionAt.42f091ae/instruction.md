# Bug Report

### Describe the bug

I'm encountering an issue with `parseExpressionAt` where it seems to be consuming an extra token before parsing the expression. This causes the parser to start at the wrong position and parse the wrong part of the input.

### Reproduction

```js
const parser = Parser.parseExpressionAt('foo + bar', 0, options);
// Expected to parse 'foo' starting at position 0
// But it's actually parsing starting from the next token
```

When calling `parseExpressionAt` with a specific position, the function should parse the expression at that exact position. However, it appears to advance the token position before parsing, which means it skips over the token at the specified position.

### Expected behavior

`parseExpressionAt` should parse the expression starting at the given position without advancing the token first. The expression at position 0 should be parsed correctly, not the expression after the first token.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
