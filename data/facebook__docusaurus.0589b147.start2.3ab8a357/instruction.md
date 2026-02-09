# Bug Report

### Describe the bug

I'm experiencing an issue with blank line tokenization in MDX parsing. When processing markdown content with blank lines that contain spaces, the parser is not handling them correctly. The blank line detection seems to be inverted - it's treating lines with spaces differently than expected.

### Reproduction

```js
const mdx = `
Some content

   
More content
`

// Parse the MDX content
// Expected: blank lines with spaces should be recognized as blank lines
// Actual: parsing behavior is incorrect
```

When I have blank lines that contain whitespace characters (spaces/tabs), they're not being processed as blank lines properly. This affects the overall document structure and can lead to unexpected parsing results.

### Expected behavior

Blank lines with or without whitespace should be tokenized consistently. Lines containing only whitespace characters should be treated as blank lines and processed accordingly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
