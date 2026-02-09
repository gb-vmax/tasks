# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in MDX parsing. When parsing markdown content with spaces, the parser seems to be consuming spaces incorrectly, leading to malformed output or unexpected behavior.

### Reproduction

```js
// Parse MDX content with multiple spaces
const content = `
# Heading

Some text with    multiple spaces between words.
`;

const result = compile(content);
// The spaces are not being handled correctly
```

### Expected behavior

The parser should correctly handle and preserve whitespace according to markdown specifications. Multiple spaces should be processed properly without causing parsing issues.

### Additional context

This appears to affect content with consecutive spaces or indentation. The whitespace tokenization seems to be off, possibly related to how the space factory function tracks and consumes space characters.

---
Repository: /testbed
