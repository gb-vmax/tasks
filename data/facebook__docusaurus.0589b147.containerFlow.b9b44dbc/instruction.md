# Bug Report

### Describe the bug

I'm experiencing an issue where MDX content is being rendered with an extra blank line or unexpected output at the end of container flow elements. It seems like the parser is trying to process one element beyond the actual array length, which causes undefined behavior.

### Reproduction

```js
const mdxContent = `
# Heading

Some paragraph text.

- List item 1
- List item 2

Final paragraph.
`;

// Parse and render the MDX content
// The output includes an unexpected extra newline or attempts to access undefined children
```

When rendering MDX documents with multiple flow elements (headings, paragraphs, lists), the final element seems to be followed by extra spacing or the renderer tries to access a child element that doesn't exist.

### Expected behavior

The container flow should only iterate through the actual children in the array and not attempt to access elements beyond `children.length - 1`. The rendered output should not include extra newlines or attempt to process undefined elements.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
