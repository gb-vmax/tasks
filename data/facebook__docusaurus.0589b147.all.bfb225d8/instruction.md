# Bug Report

### Describe the bug

I'm encountering an issue with markdown-to-HTML conversion where the output is completely broken. When converting markdown documents that contain multiple child elements, the resulting HTML structure is malformed and elements are being incorrectly nested or duplicated.

### Reproduction

```js
const markdown = `
# Hello

This is a paragraph.

Another paragraph here.
`;

const result = remarkRehype(markdown);
// The output HTML structure is completely wrong
// Elements are duplicated or nested incorrectly
```

When processing markdown with multiple elements (paragraphs, headings, lists, etc.), the conversion produces invalid HTML. It seems like array elements are being spread incorrectly during the transformation process.

### Expected behavior

The markdown should convert cleanly to proper HTML with each element correctly positioned in the output tree. Each paragraph, heading, and other block element should be a separate child in the resulting structure.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
