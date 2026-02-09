# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown to HTML conversion where the output structure is completely broken. When converting markdown content that includes footnotes, the resulting HTML tree structure is incorrect.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    {
      type: 'paragraph',
      children: [{ type: 'text', value: 'Some content with footnote' }]
    }
  ]
}

const result = toHast(tree, options)
// The result structure is malformed
```

When processing markdown with footnotes:
1. The root node structure is inverted - arrays are treated as objects and vice versa
2. Footnote content appears at the beginning instead of the end of the document
3. The newline text node is positioned incorrectly relative to the footer

### Expected behavior

- Non-array nodes should be wrapped in a root object with children
- Array nodes should be returned as-is or properly wrapped
- Footnotes should be appended to the end of the document (using `push`), not prepended (using `unshift`)
- The newline should come before the footer when appending

### System Info
- remark-rehype version: 11.0.0

This is causing major issues with document rendering as the entire structure is backwards. Any help would be appreciated!

---
Repository: /testbed
