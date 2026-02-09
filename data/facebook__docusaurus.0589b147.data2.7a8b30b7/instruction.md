# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where paragraphs are not being properly terminated. When processing MDX content, the parser seems to get stuck in an infinite loop and doesn't correctly handle the end of paragraph blocks.

### Reproduction

```js
const mdxContent = `
This is a paragraph.

This is another paragraph.
`;

// Process the MDX content
const result = compile(mdxContent);
```

When parsing content with multiple paragraphs separated by blank lines, the parser doesn't exit the paragraph state correctly and continues processing indefinitely instead of moving to the next line start.

### Expected behavior

The parser should properly exit the paragraph when encountering line endings and move to the next state (lineStart) to process subsequent content. Each paragraph should be closed correctly before starting a new one.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
