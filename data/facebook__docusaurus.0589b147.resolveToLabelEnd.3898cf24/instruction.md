# Bug Report

### Describe the bug

I'm experiencing an issue with parsing MDX content that contains image or link references. The parser seems to be incorrectly calculating offsets when resolving label text, which causes the parsed output to be malformed or include extra/missing characters.

### Reproduction

```js
// Example MDX content with a reference-style link
const mdxContent = `
[link text][ref]

[ref]: https://example.com
`

// When parsing this, the label text boundaries are incorrect
// The start position is off by one event in the events array
```

The problem appears to be related to how the parser resolves label end positions. When processing reference-style links or images, the text extraction doesn't align with the actual content boundaries.

### Expected behavior

The parser should correctly identify the start and end positions of label text in reference-style links and images. The extracted text should match exactly what's between the brackets without any extra or missing characters.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently, possibly related to how events are indexed during the label resolution phase.

---
Repository: /testbed
