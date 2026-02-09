# Bug Report

### Describe the bug

I'm experiencing an issue with parsing markdown content that spans multiple chunks. When the content is split across buffer boundaries, the parser seems to be dropping or incorrectly slicing parts of the text.

### Reproduction

```js
// When parsing markdown with content that spans multiple internal chunks
const markdown = `
Some text that might be split across internal buffer boundaries.
More content here.
`;

const result = remark.parse(markdown);
// The parsed output is missing characters or has incorrect content
```

This seems to happen specifically when:
1. The markdown content is large enough to be split into multiple internal chunks
2. A token (like a paragraph or code block) spans across chunk boundaries
3. The start and end positions of the token are in different chunks

### Expected behavior

The parser should correctly extract and reconstruct the full content regardless of how it's internally chunked. All characters should be preserved and the output should match the input.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
