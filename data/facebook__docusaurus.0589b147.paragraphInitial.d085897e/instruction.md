# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where paragraph content is not being processed correctly. It seems like the order of operations when entering a paragraph block has been changed, causing the content initialization to happen before the paragraph token is properly established.

### Reproduction

```js
// Parse MDX content with a simple paragraph
const mdx = `
This is a simple paragraph.
`;

// The paragraph token structure is incorrect
// Content is being processed before the paragraph context is set up
```

### Expected behavior

When parsing paragraph content, the paragraph token should be entered first, establishing the proper context before processing the line content. The current behavior processes the line before the paragraph token is created, which breaks the expected token hierarchy.

### Additional context

This affects any MDX document with paragraph content. The token tree structure is malformed because `lineStart` is being called before `effects.enter("paragraph")` completes, rather than after the paragraph context has been established.

---
Repository: /testbed
