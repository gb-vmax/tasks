# Bug Report

### Describe the bug

I'm encountering an issue with MDX content parsing where the document structure seems to break when processing text chunks. The content appears to get stuck in an infinite loop or doesn't render properly.

### Reproduction

```js
const mdx = `
# Hello World

This is a paragraph with some text content.
Another line of text here.
`;

// Process the MDX content
const result = await compile(mdx);
```

When processing MDX documents with multiple lines of text in paragraphs, the parser doesn't handle the content correctly. The linked list structure for text chunks appears to be malformed, causing the content to not be processed as expected.

### Expected behavior

The MDX content should be parsed correctly with proper text chunk linking. Each chunk should reference the next chunk in the sequence, allowing the parser to traverse through the content properly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
