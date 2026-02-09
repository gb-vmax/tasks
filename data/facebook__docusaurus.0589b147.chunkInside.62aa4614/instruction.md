# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where content isn't being processed correctly in certain cases. The parser seems to be skipping or mishandling chunks of content, particularly when dealing with specific character codes.

### Reproduction

```js
// When parsing MDX content with certain character sequences
const mdxContent = `
# Heading
Some content here
`;

// The parser doesn't handle the content chunks properly
// Content gets truncated or skipped unexpectedly
```

### Expected behavior

The MDX parser should correctly tokenize and process all content chunks, regardless of the character codes encountered. Content should be fully parsed without any truncation or unexpected behavior.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
