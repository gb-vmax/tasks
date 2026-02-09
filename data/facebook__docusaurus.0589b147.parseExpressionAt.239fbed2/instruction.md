# Bug Report

### Describe the bug

I'm experiencing an issue with MDX expression parsing where expressions are being parsed with an incorrect starting position. When using `parseExpressionAt` to parse an expression at a specific position in the input string, the parser seems to be off by one character, causing it to skip the first character of the expression.

### Reproduction

```js
const input = '{someExpression}';
const pos = 0;

// Try to parse expression starting at position 0
const result = Parser.parseExpressionAt(input, pos, options);

// The parser starts at position 1 instead of 0
// First character '{' is skipped
```

When parsing expressions at a specific position, the parser doesn't start at the correct offset. This leads to parsing errors or incorrect AST nodes being generated, especially when trying to parse expressions that start with special characters.

### Expected behavior

The parser should start parsing exactly at the position specified by the `pos` parameter, not one character after it. The expression should be parsed from the correct starting point without skipping any characters.

### Additional context

This appears to affect any code that relies on precise position-based parsing of MDX expressions. The issue manifests when you need to parse an expression starting at a known offset in the source text.

---
Repository: /testbed
