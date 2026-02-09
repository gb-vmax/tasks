# Bug Report

### Describe the bug

I'm encountering an issue where HTML content is not being generated correctly. When processing a tree structure, the first child node seems to be getting skipped entirely, and subsequent nodes are not rendering as expected.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'element', tagName: 'p', children: [{ type: 'text', value: 'First paragraph' }] },
    { type: 'element', tagName: 'p', children: [{ type: 'text', value: 'Second paragraph' }] }
  ]
}

const html = toHtml(tree)
// Expected: <p>First paragraph</p><p>Second paragraph</p>
// Actual: Only the second paragraph appears, or nothing at all
```

### Expected behavior

All child nodes should be processed and converted to HTML, including the first element in the tree. The output should contain all paragraphs in the correct order.

### Additional context

This seems to affect any tree structure where the first child is at index 0. The first element is completely missing from the output, which breaks the rendering of documents that start with important content.

---
Repository: /testbed
