# Bug Report

### Describe the bug

I'm encountering an issue with parsing MDX expressions at specific positions. When trying to parse an expression starting at a given position, the parser seems to be off by one character, causing it to start parsing from the wrong location.

### Reproduction

```js
const input = '{someExpression}';
const pos = 0;

// Trying to parse expression at position 0
const result = Parser.parseExpressionAt(input, pos, options);

// The parser starts reading from position 1 instead of position 0
// This causes the opening brace to be skipped
```

This appears to affect any code that relies on `parseExpressionAt` to parse expressions at exact character positions in the input string.

### Expected behavior

The parser should start parsing from the exact position specified by the `pos` parameter, not from `pos + 1`. When `pos = 0`, it should read the character at index 0 first.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
