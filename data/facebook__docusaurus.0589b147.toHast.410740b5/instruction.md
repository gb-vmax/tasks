# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown-to-HTML conversion where the output structure is completely broken. When converting markdown content that should produce a root node with children, the result either has the wrong structure or the children array is malformed.

Additionally, when footnotes are present in the markdown, they appear in the wrong position - at the beginning of the content instead of at the end where they should be.

### Reproduction

```js
// Convert markdown with content that produces an array of nodes
const markdown = `
# Heading
Some paragraph text
`;

const result = toHast(markdownTree, options);

// Expected: result should be a root node with children array
// Actual: result structure is incorrect when node is an array

// Also with footnotes:
const markdownWithFootnotes = `
Some text[^1]

[^1]: This is a footnote
`;

const resultWithFootnotes = toHast(markdownTreeWithFootnotes, options);

// Expected: Footnote should be at the end of children array
// Actual: Footnote appears at the beginning of the content
```

### Expected behavior

1. When the converted node is an array, it should be properly wrapped in a root node with a `children` property containing that array
2. Footnotes should be appended to the end of the document (using `push`), not inserted at the beginning (using `unshift`)

### System Info
- remark-rehype version: 11.0.0
- Node version: Latest

---
Repository: /testbed
