# Bug Report

### Describe the bug

I'm experiencing an issue with markdown processing where the first child element in a parent node is being skipped during conversion. This appears to affect the output when converting markdown to HTML.

### Reproduction

When processing a markdown document with multiple child elements, the first element doesn't get processed correctly. For example:

```js
const parent = {
  children: [
    { type: 'text', value: 'First item' },
    { type: 'break' },
    { type: 'text', value: 'Second item' }
  ]
}

// Process the parent node
// Expected: All three children should be processed
// Actual: First child is missing from output
```

### Expected behavior

All child elements in a parent node should be processed and included in the output, including the first element. The conversion should handle the entire array of children starting from index 0.

### Additional context

This seems to be related to how the child nodes are being iterated. The first element in the children array is not being included in the converted output, which leads to incomplete or incorrect HTML generation from the markdown source.

---
Repository: /testbed
