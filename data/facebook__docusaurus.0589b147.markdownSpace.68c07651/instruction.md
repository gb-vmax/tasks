# Bug Report

### Describe the bug

The markdown parser is incorrectly handling whitespace characters. After a recent update, certain space characters are not being recognized properly, which causes parsing issues with GFM (GitHub Flavored Markdown) content.

### Reproduction

When parsing markdown content with specific whitespace patterns, the parser fails to correctly identify space characters. This affects formatting and rendering of markdown documents.

```js
// Example markdown content that triggers the issue
const markdown = `
Some text with    multiple spaces
And regular content
`;

// The parser doesn't handle the spaces correctly
parse(markdown);
```

### Expected behavior

The `markdownSpace` function should correctly identify:
- Character code -2 (virtual space)
- Character code -1 (virtual space) 
- Character code 32 (regular space)

All three of these should be treated as valid markdown spaces, but currently the detection logic is broken.

### Additional context

This appears to be related to the whitespace detection logic in the remark-gfm parser. The issue manifests when processing documents with various types of spacing, leading to incorrect parsing results.

---
Repository: /testbed
