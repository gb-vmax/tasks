# Bug Report

### Describe the bug

I'm experiencing an issue with HTML rendering where the first child element in a parent node is being skipped/ignored. When processing nodes with multiple children, only elements after the first one are being rendered correctly.

### Reproduction

```js
const parent = {
  children: [
    { type: 'element', tagName: 'p', children: [{ type: 'text', value: 'First paragraph' }] },
    { type: 'element', tagName: 'p', children: [{ type: 'text', value: 'Second paragraph' }] },
    { type: 'element', tagName: 'p', children: [{ type: 'text', value: 'Third paragraph' }] }
  ]
}

// Expected output: all three paragraphs rendered
// Actual output: only second and third paragraphs appear
```

### Expected behavior

All child elements should be processed and rendered in the output. The first child element should not be skipped.

### Additional context

This seems to affect any parent element with multiple children. The first child is consistently missing from the rendered output while subsequent children render correctly. This might be related to how the children array is being iterated.

---
Repository: /testbed
