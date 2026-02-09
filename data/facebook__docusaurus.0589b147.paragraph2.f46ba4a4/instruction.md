# Bug Report

### Describe the bug

After a recent update, MDX content with paragraph elements is not rendering correctly. The paragraphs appear to be broken or missing from the output.

### Reproduction

```jsx
// Create a simple MDX file with paragraphs
const mdxContent = `
This is a paragraph.

This is another paragraph.
`;

// Compile the MDX
const result = await compile(mdxContent);
```

When the above MDX is compiled and rendered, the paragraph elements don't appear as expected in the output.

### Expected behavior

Paragraphs should render normally as `<p>` tags in the compiled output. The MDX compiler should correctly identify and process paragraph nodes.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
