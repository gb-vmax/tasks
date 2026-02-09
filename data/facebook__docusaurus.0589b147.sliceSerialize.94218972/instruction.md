# Bug Report

### Describe the bug

I'm encountering an issue with text serialization in MDX content. When processing MDX files, the serialization of token streams appears to be producing incorrect output. Specifically, text content that should preserve certain formatting is being altered unexpectedly.

### Reproduction

```js
// Processing MDX content with tabs or special whitespace
const mdxContent = `
# Heading
\tIndented text with tab
Regular text
`;

// After parsing and serialization, the output doesn't match expected format
// Tab expansion behavior seems inverted
```

### Expected behavior

The serialization should correctly handle whitespace and tab expansion based on the `expandTabs` parameter. When `expandTabs` is true, tabs should be expanded; when false, they should be preserved.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
