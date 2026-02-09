# Bug Report

### Describe the bug
I'm experiencing an issue with MDX paragraph rendering where the children of paragraph elements are not being processed correctly. It seems like the wrong node is being passed to `state.all()`, which causes the paragraph content to be missing or incorrect in the output.

### Reproduction
```jsx
// Input MDX content
const mdxContent = `
This is a paragraph with some text.

Another paragraph here.
`;

// When processing this through MDX, the paragraph elements 
// are created but their children are not properly populated
```

The issue appears to be in the paragraph handler where `state.all()` is being called with an incorrect node reference, resulting in empty or malformed paragraph elements in the final output.

### Expected behavior
Paragraphs should render with their full text content intact. The children of paragraph elements should be properly transformed and included in the resulting HAST tree.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
