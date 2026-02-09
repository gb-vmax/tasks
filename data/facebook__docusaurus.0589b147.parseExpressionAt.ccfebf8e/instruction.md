# Bug Report

### Describe the bug

I'm experiencing an issue with expression parsing where the parser seems to be starting at the wrong position and consuming extra tokens. When parsing expressions at a specific position in the input, the parser appears to be off by one character and is reading beyond the intended expression boundary.

### Reproduction

```js
// Trying to parse an expression starting at a specific position
const input = "some code {expression} more code";
const position = 10; // Should point to start of 'expression'

const result = parseExpressionAt(input, position, options);

// The parsed result includes unexpected characters or 
// starts from the wrong position (position + 1 instead of position)
```

### Expected behavior

The parser should:
1. Start parsing exactly at the specified position
2. Parse only the expression itself without consuming additional tokens
3. Return the correctly parsed expression without any offset

### System Info
- @mdx-js/mdx version: 3.0.0
- Parser: acorn-based

This seems to have broken expression parsing in MDX files where inline expressions need to be extracted at precise positions. The expression boundaries are getting misaligned.

---
Repository: /testbed
