# Bug Report

### Describe the bug

I'm experiencing an issue with MDX content parsing where the tokenizer seems to be processing chunks incorrectly. The content flow appears broken and I'm getting unexpected results when parsing certain MDX files.

### Reproduction

```js
// When parsing MDX content with specific patterns
const mdxContent = `
# Heading

Some content here with multiple lines
and continuation across chunks
`;

// The parser seems to lose track of content chunks
// and produces malformed output
```

### Expected behavior

The MDX parser should correctly tokenize and process content chunks, maintaining proper sequencing and state transitions throughout the parsing process. Content should flow naturally from one chunk to the next without losing data or breaking the token stream.

### Additional context

This seems to affect content that spans multiple chunks or has specific line break patterns. The issue appears to be related to how the tokenizer handles chunk transitions and state management during content processing.

---
Repository: /testbed
