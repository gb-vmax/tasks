# Bug Report

### Describe the bug

I'm experiencing an issue with MDX paragraph parsing where paragraphs appear to be immediately closed without any content. When I try to render MDX content that contains paragraphs, they're not being processed correctly.

### Reproduction

```jsx
const mdxContent = `
This is a paragraph.

Another paragraph here.
`;

// When parsing this MDX content, paragraphs are empty
// The text content doesn't get associated with the paragraph tokens
```

### Expected behavior

Paragraphs should contain their text content and be properly parsed. The paragraph token should remain open while the content is being processed, then close after the content has been added.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
