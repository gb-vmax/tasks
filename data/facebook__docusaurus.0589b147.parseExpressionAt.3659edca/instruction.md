# Bug Report

### Describe the bug

I'm experiencing an issue with parsing MDX expressions at specific positions. When using `parseExpressionAt` to parse an expression starting at a given position in the input string, the parser seems to be skipping the first character of the expression, leading to incorrect parsing results.

### Reproduction

```js
const input = "x + 1";
const result = Parser.parseExpressionAt(input, 0);
// Expected: Parse "x + 1" correctly
// Actual: Tries to parse " + 1" (missing the 'x')
```

When I try to parse an expression starting at position 0, it appears the parser is starting from position 1 instead, causing the first token to be missed entirely.

### Expected behavior

The parser should start parsing from the exact position specified and include all characters from that position onwards. If I specify position 0, it should parse the entire expression starting with the first character.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
