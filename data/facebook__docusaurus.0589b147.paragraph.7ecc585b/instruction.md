# Bug Report

### Describe the bug

I'm encountering an issue with paragraph rendering in MDX where the children of paragraph elements are not being processed correctly. It seems like the `state.all()` function is being called on the wrong node, which results in the paragraph's children not being transformed properly.

### Reproduction

```js
// When processing an MDX document with paragraphs
const mdx = `
This is a paragraph with some text.
`

// The paragraph element's children are empty or incorrect
// instead of containing the expected text nodes
```

### Expected behavior

When rendering a paragraph node, the `children` property should contain the properly transformed child nodes from the original paragraph. The state transformations should be applied in the correct order to ensure the paragraph element and its children are processed correctly.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
